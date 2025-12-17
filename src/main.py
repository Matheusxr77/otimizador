import json
import time
from kubernetes import client, config, watch
import config as cfg
import algorithm

def load_data():
    """Lê o arquivo mock.json"""
    try:
        with open(cfg.MOCK_DATA_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo {cfg.MOCK_DATA_PATH} não encontrado.")
        return {}

def get_best_node(nodes_available):
    data = load_data()
    # Filtra nós válidos
    valid_nodes = {k: v for k, v in data.items() if k in nodes_available}
    if not valid_nodes: return None

    # Encontrar Mínimos e Máximos Globais
    carbons = [v['carbon'] for v in valid_nodes.values()]
    costs = [v['cost'] for v in valid_nodes.values()]
    latencies = [v['latency'] for v in valid_nodes.values()]

    min_max = {
        'min_c': min(carbons), 'max_c': max(carbons),
        'min_e': min(costs), 'max_e': max(costs),
        'min_l': min(latencies), 'max_l': max(latencies)
    }

    scores = {}
    print(f"\n--- Calculando Scores (Pesos: {cfg.WEIGHTS}) ---")
    
    for node, metrics in valid_nodes.items():
        score, n_c, n_e, n_l = algorithm.calculate_score(metrics, cfg.WEIGHTS, min_max)
        scores[node] = score
        print(f"Nó: {node:<15} | Score: {score:.4f}")

    return min(scores, key=scores.get)

def schedule_pod(v1_client, pod_name, node_name):
    print(f"--- AGENDANDO {pod_name} EM {node_name} ---")
    binding = client.V1Binding(
        metadata=client.V1ObjectMeta(name=pod_name),
        target=client.V1ObjectReference(kind="Node", name=node_name)
    )
    try:
        v1_client.create_namespaced_binding(namespace="default", body=binding, _preload_content=False)
        print(f">>> SUCESSO: {pod_name} -> {node_name}\n")
    except Exception as e:
        print(f"!!! ERRO: {e}")

def main():
    print(f"Iniciando {cfg.SCHEDULER_NAME} (Modular)...")
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
            
            print(f"\n📢 Pod Pendente: {pod.metadata.name}")
            available_nodes = [n.metadata.name for n in v1.list_node().items]
            best_node = get_best_node(available_nodes)
            
            if best_node:
                schedule_pod(v1, pod.metadata.name, best_node)

if __name__ == "__main__":
    main()