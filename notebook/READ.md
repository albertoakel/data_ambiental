
---

## Descrição dos  Notebooks

### [bairros_IBGE_processa.ipynb](notebooks/bairros_IBGE_processa.ipynb)
- Padroniza, limpa e organiza os dados de bairros de Belém-PA a partir de múltiplos arquivos CSV (`tabela3033` e `tabela3170`).  
- Consolida informações de diferentes fontes para análise posterior.

### [plota_mapa_setores.ipynb](notebooks/plota_mapa_setores.ipynb)
- Carrega setores de coleta processados armazenados em GeoPackage (GPKG).  
- Cria mapas interativos com Folium mostrando polígonos e coordenadas de referência de cada setor.

### [plota_bairros_belem.ipynb](notebooks/plota_bairros_belem.ipynb)
- Lê o shapefile `PA_bairros_CD2022.shp` usando GeoPandas.  
- Filtra apenas bairros do município de Belém (código IBGE 1501402).  
- Cria mapas interativos mostrando os limites municipais.

### [processamento_shape.ipynb](notebooks/processamento_shape.ipynb)
- Processa arquivos JSONL com informações sobre setores de coleta (horários, coordenadas, polígonos).  
- Organiza os dados em GeoDataFrame padronizado para análise espacial e armazenamento geoespacial.
