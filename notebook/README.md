
---

## Descrição dos  Notebooks

### [bairros_IBGE_processa.ipynb](notebooks/EDA.ipynb)
A análise busca identificar padrões que possam explicar a ocorrência de Depósitos Irregulares de Entulho (DIEs) e como esses eventos se distribuem espacialmente em função das condições sociais e estruturais de cada bairro.

### [bairros_IBGE_processa.ipynb](notebooks/Mapa_Bairros_plotly.ipynb)
Cria um mapa interativo que integra dados geográficos dos bairros com indicadores socioeconômicos e pontos de descarte irregular.

### [bairros_IBGE_processa.ipynb](notebooks/Mapa_Setores_coleta_Folium.ipynb)

Cria um mapa interativo dos setores de coleta de lixo, mostrando:

### [bairros_IBGE_processa.ipynb](notebooks/ML_random_forest.ipynb)

O código realiza a imputação de dados faltantes usando machine learning para prever a quantidade de depósitos irregulares em bairros onde essa informação não está disponível. Ele combina dados socioeconômicos do IBGE com informações específicas sobre depósitos irregulares, aplicando um modelo de Random Forest para estimar os valores ausentes com base nas características demográficas e econômicas dos bairros.
### [bairros_IBGE_processa.ipynb](notebooks/preprocessamento_Bairros_IBGE.ipynb)

Padronizar, limpar e organizar os dados de bairros de Belém-PA a partir de múltiplos arquivos CSV.
O código realiza a leitura de múltiplos arquivos CSV contendo dados de bairros de Belém-PA, tanto do conjunto tabela3033 quanto do tabela3170 e salva tabela_total_final.csv* com as principais features.

### [bairros_IBGE_processa.ipynb](notebooks/Processamento_shape.ipynb)
O código realiza o processamento dos dados de setores de coleta obtidos por meio de webscraping. Ele lê arquivos no formato JSON Lines (JSONL) contendo informações sobre setores, horários de coleta, coordenadas de referência e polígonos geográficos que representam a área atendida. A partir dessa leitura inicial, o código organiza, transforma e estrutura esses dados em um GeoDataFrame padronizado para posterior análise espacial e armazenamento em formato geoespacial.