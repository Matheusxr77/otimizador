import time
import random
from kubernetes import client, config, watch
import config as cfg
import algorithm
import optimizer

CURRENT_OPTIMAL_WEIGHTS = {}

def get_real_time_metrics():
    regions = {
        "geo-cluster-m02": {"base_carbon": 500, "base_cost": 0.15, "latency": 20},
        "geo-cluster-m03": {"base_carbon": 250, "base_cost": 0.25, "latency": 150},
        "geo-cluster-m04": {"base_carbon": 50,  "base_cost": 0.10, "latency": 300}
    }
    data = {}
    for node, profile in regions.items():
        data[node] = {
            "carbon": max(0, profile["base_carbon"] + random.randint(-50, 50)),
            "cost": max(0.01, round(profile["base_cost"] + random.uniform(-0.02, 0.02), 3)),
            "latency": profile["latency"]
        }
    return data

def get_best_node(nodes_available):
    global CURRENT_OPTIMAL_WEIGHTS
    
    data = get_real_time_metrics()
    valid_nodes = {k: v for k, v in data.items() if k in nodes_available}
    if not valid_nodes: return None

    carbons = [v['carbon'] for v in valid_nodes.values()]
    costs = [v['cost'] for v in valid_nodes.values()]
    latencies = [v['latency'] for v in valid_nodes.values()]

    min_max = {
        'min_c': min(carbons), 'max_c': max(carbons),
        'min_e': min(costs), 'max_e': max(costs),
        'min_l': min(latencies), 'max_l': max(latencies)
    }

    scores = {}
    scores = {}
    print(f"\nANÁLISE (Pesos Dinâmicos: {CURRENT_OPTIMAL_WEIGHTS})")
    
    print(f"{'NÓ':<20} | {'CO2 (g)':<8} | {'CUSTO ($)':<10} | {'LAT (ms)':<8} | {'SCORE'}")
    print("-" * 75)
    
    for node, metrics in valid_nodes.items():
        if metrics['latency'] > cfg.MAX_LATENCY:
            print(f"{node:<20} | {metrics['carbon']:<8} | {metrics['cost']:<10.3f} | {metrics['latency']:<8} | ⛔ SLA")
            continue

        score, _, _, _ = algorithm.calculate_score(metrics, CURRENT_OPTIMAL_WEIGHTS, min_max)
        scores[node] = score
        
        print(f"{node:<20} | {metrics['carbon']:<8} | {metrics['cost']:<10.3f} | {metrics['latency']:<8} | {score:.4f}")

    if not scores: return None
    return min(scores, key=scores.get)

def schedule_pod(v1_client, pod_name, node_name):
    print(f"AGENDANDO {pod_name} EM {node_name}...")
    binding = client.V1Binding(
        metadata=client.V1ObjectMeta(name=pod_name),
        target=client.V1ObjectReference(kind="Node", name=node_name)
    )
    try:
        v1_client.create_namespaced_binding("default", binding, _preload_content=False)
        print(f"SUCESSO.\n")
    except Exception as e:
        print(f"ERRO: {e}")

def main():
    global CURRENT_OPTIMAL_WEIGHTS
    
    print(f"🔥 Iniciando Sistema Autônomo v3.0...")
    print("1. Inicializando Motor de Otimização...")
    
    start_time = time.time()
    best_w = optimizer.find_optimal_weights()
    CURRENT_OPTIMAL_WEIGHTS = {k: round(v, 1) for k, v in best_w.items()}
    
    elapsed = time.time() - start_time
    print(f"Calibração Concluída em {elapsed:.2f}s.")
    print(f"Pesos Otimizados Definidos: {CURRENT_OPTIMAL_WEIGHTS}")
    print("="*60)
    
    print("   Aguardando Pods...")
    
    try:
        config.load_kube_config()
    except:
        config.load_incluster_config()
    
    v1 = client.CoreV1Api()
    w = watch.Watch()

    for event in w.stream(v1.list_namespaced_pod, "default"):
        pod = event['object']
        if pod.status.phase == "Pending" and pod.spec.scheduler_name == cfg.SCHEDULER_NAME:
            if pod.spec.node_name: continue
            
            print(f"\n🔔 DEMANDA: {pod.metadata.name}")
            available = [n.metadata.name for n in v1.list_node().items]
            best = get_best_node(available)
            if best: schedule_pod(v1, pod.metadata.name, best)

if __name__ == "_main_":
    main()