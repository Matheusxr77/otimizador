import random
import numpy as np
import algorithm 

SLA_LATENCY = 400
NUM_SCENARIOS = 1000  

def generate_scenario():
    nodes = ["geo-cluster-m02", "geo-cluster-m03", "geo-cluster-m04"]
    data = {}
    
    ranges = {
        "m02": {"c": (400, 600), "e": (0.12, 0.18), "l": (20, 50)},    # US
        "m03": {"c": (200, 400), "e": (0.20, 0.30), "l": (140, 160)},  # EU
        "m04": {"c": (50, 150),  "e": (0.08, 0.12), "l": (280, 320)}   # ASIA
    }
    
    for n in nodes:
        key = "m02" if "m02" in n else "m03" if "m03" in n else "m04"
        r = ranges[key]
        data[n] = {
            "carbon": random.randint(*r["c"]),
            "cost": round(random.uniform(*r["e"]), 3),
            "latency": random.randint(*r["l"])
        }
    return data

def find_optimal_weights():
    print("   [Otimizador] Gerando 1.000 cenários de simulação...")
    scenarios = [generate_scenario() for _ in range(NUM_SCENARIOS)]
    
    all_c = [m['carbon'] for s in scenarios for m in s.values()]
    all_e = [m['cost'] for s in scenarios for m in s.values()]
    all_l = [m['latency'] for s in scenarios for m in s.values()]
    
    min_max = {
        'min_c': min(all_c), 'max_c': max(all_c),
        'min_e': min(all_e), 'max_e': max(all_e),
        'min_l': min(all_l), 'max_l': max(all_l)
    }
    
    print("   [Otimizador] Testando combinações matemáticas...")
    best_weights = None
    lowest_carbon = float('inf')
    
    for c in np.arange(0, 1.1, 0.1):
        for e in np.arange(0, 1.1, 0.1):
            for l in np.arange(0, 1.1, 0.1):
                if abs((c + e + l) - 1.0) > 0.01: continue 
                
                weights = {"carbon": c, "cost": e, "latency": l}
                
                total_carbon = 0
                sla_violations = 0
                
                for s in scenarios:
                    scores = {n: algorithm.calculate_score(m, weights, min_max)[0] for n, m in s.items()}
                    winner = min(scores, key=scores.get)
                    
                    total_carbon += s[winner]['carbon']
                    if s[winner]['latency'] > SLA_LATENCY:
                        sla_violations += 1
                
                avg_carbon = total_carbon / NUM_SCENARIOS
                sla_compliance = 1 - (sla_violations / NUM_SCENARIOS)
                
                if sla_compliance >= 0.95 and avg_carbon < lowest_carbon:
                    lowest_carbon = avg_carbon
                    best_weights = weights

    if not best_weights:
        return {"carbon": 0.5, "cost": 0.2, "latency": 0.3}
        
    return best_weights