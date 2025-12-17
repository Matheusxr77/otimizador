def normalize(value, min_v, max_v):
    if max_v == min_v: return 0
    return (value - min_v) / (max_v - min_v)

def calculate_score(metrics, weights, min_max_values):
    """Calcula o Score WSM para um único nó"""
    # Normalização
    n_c = normalize(metrics['carbon'], min_max_values['min_c'], min_max_values['max_c'])
    n_e = normalize(metrics['cost'], min_max_values['min_e'], min_max_values['max_e'])
    n_l = normalize(metrics['latency'], min_max_values['min_l'], min_max_values['max_l'])
    
    # Weighted Sum Model
    score = (weights['carbon'] * n_c) + \
            (weights['cost'] * n_e) + \
            (weights['latency'] * n_l)
            
    return score, n_c, n_e, n_l