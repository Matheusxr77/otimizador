# 📊 Guia de Visualizações

Este documento descreve todos os gráficos gerados pelo script `visualizations.py`.

## Como Gerar os Gráficos

```bash
python analysis/visualizations.py results/raw_results.csv
```

Ou especifique um diretório customizado:

```bash
python analysis/visualizations.py results/raw_results.csv results/meus_graficos
```

---

## 📈 Gráficos Gerados

Total: **19 gráficos** (visualizações completas para análise científica)

### 1. **comparison_modes_metrics_boxplot.png**
**Comparação de Métricas por Modo Operacional (Box Plots)**

- **Descrição**: Mostra a distribuição de 5 métricas principais para cada modo operacional
- **Métricas incluídas**:
  - Latência (ms)
  - Energia Renovável (%)
  - Carbono (gCO2/kWh)
  - Custo ($/kWh)
  - Score Final
- **Uso**: Identificar rapidamente qual modo performa melhor em cada métrica
- **Interpretação**: Box plots mostram mediana, quartis, outliers e valores médios

---

### 2. **comparison_modes_confidence_intervals.png**
**Comparação de Modos com Intervalos de Confiança (95%)**

- **Descrição**: Gráfico de barras com intervalos de confiança para 4 métricas principais
- **Métricas**: Latência, Renovável, Carbono, Custo
- **Uso**: Análise estatística robusta da diferença entre modos
- **Interpretação**: Barras de erro representam IC de 95% (nível de confiança estatística)

---

### 3. **scores_by_mode_violin.png**
**Distribuição de Scores por Modo Operacional (Violin Plots)**

- **Descrição**: Mostra a distribuição completa dos scores individuais e final
- **Scores incluídos**:
  - Score de Latência
  - Score de Carbono
  - Score de Custo
  - Score Final
- **Uso**: Entender a forma da distribuição dos scores (não apenas média/mediana)
- **Interpretação**: Violinos mais largos = maior variabilidade; linha = mediana

---

### 4-8. **metric_*_detailed.png** (5 gráficos)
**Análise Detalhada de Cada Métrica Individual**

Gráficos separados para cada métrica:
- `metric_latency_detailed.png` - Latência
- `metric_renewable_detailed.png` - Energia Renovável
- `metric_carbon_detailed.png` - Carbono
- `metric_cost_detailed.png` - Custo
- `metric_score_detailed.png` - Score Final

**Cada gráfico contém 2 subplots**:
1. **Esquerda**: Box plot mostrando distribuição completa
2. **Direita**: Barras com média e intervalo de confiança (95%)

**Indicador**: Seta mostrando se "maior é melhor" ou "menor é melhor"

---

### 9. **scenarios_by_category.png**
**Score Final por Categoria de Cenário**

- **Descrição**: Compara performance entre diferentes categorias de cenários científicos
- **Categorias incluídas**:
  - baseline
  - sensitivity_fine / moderate / extreme
  - mode_comparison
  - scale_regions / scale_workloads
  - stress_test
- **Uso**: Identificar quais tipos de cenários levam a melhores/piores resultados
- **Interpretação**: Box plots por categoria de experimento

---

### 10. **sensitivity_variance.png**
**Análise de Sensibilidade à Variância**

- **Descrição**: 4 subplots mostrando como a variância afeta as métricas
- **Subplots**:
  1. Score Final vs Variância
  2. Latência Média vs Variância
  3. Energia Renovável vs Variância
  4. Custo Médio vs Variância
- **Uso**: Entender a robustez do sistema sob incerteza
- **Interpretação**: Linhas com faixas de desvio padrão

---

### 11. **region_selection_distribution.png**
**Distribuição de Seleção de Regiões**

- **Esquerda**: Top 20 regiões mais selecionadas (barras horizontais)
- **Direita**: Top 10 regiões por modo operacional (barras empilhadas)
- **Uso**: Identificar quais regiões são mais/menos escolhidas e por quais modos
- **Interpretação**: Barras maiores = região mais utilizada

---

### 12. **workload_priority_analysis.png**
**Análise por Prioridade de Workload**

- **Descrição**: 4 métricas analisadas por nível de prioridade do workload
- **Métricas**: Score Final, Latência, Renovável, Custo
- **Uso**: Ver se workloads de diferentes prioridades recebem tratamento diferenciado
- **Interpretação**: Box plots agrupados por prioridade (1, 2, 3, etc.)

---

### 13. **scale_analysis.png**
**Análise de Escalabilidade**

- **Esquerda**: Score Final vs Número de Regiões
- **Direita**: Score Final vs Número de Workloads
- **Uso**: Avaliar como o sistema escala com mais recursos ou carga
- **Interpretação**: Linhas com faixas de confiança

---

### 14. **correlation_heatmap.png**
**Mapa de Calor de Correlações**

- **Descrição**: Matriz de correlação entre todas as métricas e scores
- **Variáveis incluídas**:
  - Métricas: Latência, Renovável, Carbono, Custo
  - Scores: Score Lat., Score Carb., Score Custo, Score Final
- **Uso**: Identificar relações lineares entre variáveis
- **Interpretação**: 
  - Valores próximos a +1 = correlação positiva forte
  - Valores próximos a -1 = correlação negativa forte
  - Valores próximos a 0 = sem correlação linear

---

### 15. **success_rate_by_mode.png**
**Taxa de Sucesso de Alocação por Modo**

- **Descrição**: Barras mostrando % de alocações bem-sucedidas por modo
- **Informação adicional**: Values absolutos (sucessos/total) nas barras
- **Uso**: Avaliar a confiabilidade de cada modo operacional
- **Interpretação**: Barras mais altas = mais confiável

---

### 16. **metrics_by_region.png** ⭐ NOVO
**Análise de Métricas por Região Individual**

- **Descrição**: 3 subplots mostrando as principais métricas para as Top 20 regiões
- **Subplots incluídos**:
  1. **Latência por Região** - Regiões ordenadas por latência crescente
  2. **Custo por Região** - Regiões ordenadas por custo crescente
  3. **Sustentabilidade por Região** - Regiões ordenadas por % renovável decrescente
- **Uso**: Identificar quais regiões específicas oferecem melhor performance em cada métrica
- **Interpretação**: Barras horizontais com barras de erro (desvio padrão)
- **Filtro**: Apenas regiões com pelo menos 10 seleções

---

### 17. **tradeoffs_scatter.png** ⭐ NOVO
**Análise de Trade-offs entre Métricas**

- **Descrição**: 3 scatter plots mostrando relações entre pares de métricas
- **Trade-offs analisados**:
  1. **Latência vs Sustentabilidade** - Relação entre performance e energia limpa
  2. **Latência vs Custo** - Relação entre performance e custo
  3. **Custo vs Sustentabilidade** - Relação entre economia e energia limpa
- **Cores**: Cada modo operacional tem cor diferente
- **Uso**: Visualizar compromissos inevitáveis entre objetivos conflitantes
- **Interpretação**: 
  - Pontos no canto inferior esquerdo = melhor em ambas métricas
  - Clusters por modo = diferentes estratégias de otimização
  - Dispersão = variabilidade das decisões
- **Amostragem**: Máximo 5000 pontos para melhor visualização

---

### 18. **metrics_by_scenario_ci.png** ⭐ NOVO
**Distribuição de Métricas por Cenário com Intervalos de Confiança**

- **Descrição**: 3 gráficos de barras com IC 95% para métricas principais por categoria de cenário
- **Métricas incluídas**:
  1. **Latência (ms)** - Performance
  2. **Custo ($/kWh)** - Economia
  3. **Energia Renovável (%)** - Sustentabilidade
- **Categorias de cenário**:
  - baseline
  - sensitivity_fine / moderate / extreme
  - mode_comparison
  - scale_regions / scale_workloads
  - stress_test
- **Uso**: Comparar como diferentes tipos de experimentos afetam as métricas
- **Interpretação**: 
  - Barras de erro = intervalo de confiança 95%
  - IC não sobrepostos = diferença estatisticamente significativa
  - Valores exatos mostrados no topo das barras

---

### 19. **doe_factorial_analysis.png** ⭐ NOVO
**Análise DoE (Design of Experiments) / Análise Fatorial Completa**

- **Descrição**: Análise estatística completa dos efeitos de fatores experimentais
- **6 Subplots incluídos**:

  1. **Efeito Principal: Modo Operacional**
     - Impacto isolado do modo no score final
     - Barras coloridas por modo com desvio padrão
  
  2. **Efeito Principal: Variância**
     - Como a variância afeta o score final
     - Linha com faixa de confiança
     - Variância discretizada em 5 bins
  
  3. **Efeito Principal: Número de Regiões**
     - Impacto da quantidade de regiões disponíveis
     - Linha com faixa de confiança
  
  4. **Interação: Modo × Variância** (Gráfico de linhas)
     - Mostra se o efeito da variância muda para diferentes modos
     - Linhas paralelas = sem interação
     - Linhas cruzadas = forte interação
  
  5. **Heatmap: Modo × Variância**
     - Representação visual da interação entre fatores
     - Cores quentes = score alto
     - Cores frias = score baixo
     - Valores anotados em cada célula
  
  6. **Diagrama de Pareto: Importância dos Fatores**
     - Ranking de importância de cada fator
     - Barras = importância individual (%)
     - Linha vermelha = efeito cumulativo
     - Linha tracejada em 80% = regra de Pareto
     - Identifica os fatores mais críticos

- **Uso**: 
  - Identificar quais fatores têm maior impacto no desempenho
  - Descobrir interações não-óbvias entre fatores
  - Priorizar otimizações baseado em importância
  - Validar hipóteses científicas

- **Interpretação**:
  - **Efeitos Principais**: Quanto cada fator sozinho afeta o resultado
  - **Interações**: Se o efeito de um fator depende do nível de outro
  - **Pareto**: Geralmente 20% dos fatores explicam 80% da variância

- **Estatística utilizada**:
  - Soma dos quadrados (SS) para medir importância
  - Normalização em porcentagem do efeito total
  - Curva acumulativa para identificar fatores críticos

---

## 🎨 Características Técnicas

### Resolução e Formato
- **Formato**: PNG
- **DPI**: 300 (alta resolução, próprio para publicações)
- **Tamanho padrão**: 12x8 polegadas (variável por tipo de gráfico)

### Paleta de Cores
- **Balanced**: Azul (`#2E86AB`)
- **Sustainable**: Verde (`#06A77D`)
- **Emergency Latency**: Vermelho (`#D62839`)
- **Emergency Cost**: Laranja (`#F77F00`)

### Métricas
- **Latência**: Vermelho
- **Carbono/Renovável**: Verde
- **Custo**: Laranja
- **Score**: Azul

---

## 📌 Dicas de Uso

### Para Apresentações
Recomendados:
- `comparison_modes_confidence_intervals.png` - Visão geral robusta
- `metric_*_detailed.png` - Análise específica por métrica
- `scores_by_mode_violin.png` - Distribuições completas
- `tradeoffs_scatter.png` - **NOVO** - Trade-offs visuais entre objetivos

### Para Artigos Científicos
Recomendados:
- Todos os gráficos com intervalos de confiança
- `correlation_heatmap.png` - Análise de relações
- `sensitivity_variance.png` - Análise de robustez
- `scale_analysis.png` - Análise de escalabilidade
- `doe_factorial_analysis.png` - **NOVO** - Análise estatística completa (DoE)
- `metrics_by_scenario_ci.png` - **NOVO** - Comparação estatística por cenário

### Para Análise Exploratória
Recomendados:
- `comparison_modes_metrics_boxplot.png` - Visão rápida
- `region_selection_distribution.png` - Padrões de uso
- `scenarios_by_category.png` - Performance por cenário
- `metrics_by_region.png` - **NOVO** - Performance de regiões específicas

### Para Otimização e Decisão
Recomendados:
- `tradeoffs_scatter.png` - **NOVO** - Identificar compromissos
- `metrics_by_region.png` - **NOVO** - Escolher melhores regiões
- `doe_factorial_analysis.png` - **NOVO** - Priorizar fatores de otimização
- `correlation_heatmap.png` - Entender relações causais

---

## 🔧 Personalização

Para modificar os gráficos, edite `analysis/visualizations.py`:

- **Cores**: Modifique os dicionários `COLORS` e `METRIC_COLORS`
- **Tamanhos**: Ajuste `plt.rcParams['figure.figsize']`
- **Resolução**: Altere `plt.rcParams['savefig.dpi']`
- **Estilos**: Troque `sns.set_style()` (opções: whitegrid, darkgrid, white, dark, ticks)

---

## 📊 Estatísticas Incluídas

### Medidas de Tendência Central
- Média (mean)
- Mediana (linhas nos box plots)

### Medidas de Dispersão
- Desvio padrão (std)
- Quartis (Q1, Q3 nos box plots)
- Mínimo e Máximo

### Inferência Estatística
- Intervalo de Confiança 95% (distribuição t-Student)
- Correlação de Pearson

---

## ❓ Troubleshooting

### Erro: "arquivo CSV não encontrado"
```bash
# Verifique se o caminho está correto
ls results/raw_results.csv
```

### Erro: "coluna XXX não encontrada"
- Alguns gráficos dependem de colunas específicas
- Gráficos serão pulados automaticamente se dados não disponíveis
- Mensagem no console: "⚠️ Coluna 'XXX' não encontrada. Pulando..."

### Gráficos vazios ou estranhos
- Verifique se há dados suficientes no CSV
- Verifique se `allocation_success == True` para maioria dos registros
- Execute `python analysis/analysis.py` primeiro para validar dados

### Novos gráficos não aparecem
- Alguns gráficos novos dependem de colunas específicas:
  - `metrics_by_region.png` requer `best_region_id`
  - `metrics_by_scenario_ci.png` requer `scenario_category`
  - `doe_factorial_analysis.png` requer `mode`, `variance`, e opcionalmente `n_regions`, `n_workloads`
- Se colunas não existirem, gráfico será pulado automaticamente

---

## 🆕 Novidades (v1.0 - Março 2026)

### 4 Novos Gráficos Adicionados:

1. **metrics_by_region.png** - Análise detalhada de latência, custo e sustentabilidade por região
2. **tradeoffs_scatter.png** - Visualização de compromissos entre métricas (scatter plots)
3. **metrics_by_scenario_ci.png** - Distribuição de métricas por cenário com IC 95%
4. **doe_factorial_analysis.png** - Análise Design of Experiments completa

### Total de gráficos: 15 → **19 gráficos**

---

**Última atualização**: Julho 2026  
**Versão do script**: 1.0
