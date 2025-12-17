# Nome do Agendador
SCHEDULER_NAME = "carbon-aware-scheduler"

# Caminho para o arquivo de dados
MOCK_DATA_PATH = "src/mock.json"

# PESOS (Altere aqui para mudar os Cenários A, B, C, D)
# Cenário D (Balanced)
WEIGHTS = {
    "carbon": 0.5,
    "cost": 0.2,
    "latency": 1.0
}

# SLA Máximo (Hard Constraint)
MAX_LATENCY = 400