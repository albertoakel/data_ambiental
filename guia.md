# Projeto: Análise de Vulnerabilidade a Descartes Irregulares de Lixo em Belém

## 1. Etapas já realizadas

1. **Coleta das geometrias e frequência de coleta**  
   - Obtidas via **webscraping** e armazenadas no dataset `shape_coleta.gpkg`.  

2. **Coleta das geometrias dos bairros de Belém**  
   - Armazenadas no dataset `shape_bairros.gpkg`.  

3. **Coleta de dados socioeconômicos dos bairros**  
   - Extraídos das tabelas `tabelas_3033.csv` e `tabela_3170.csv`.  

4. **Organização e limpeza dos dados coletados via webscraping**  
   - Resultado: `shape_coleta.gpkg`.  

5. **Organização dos shapes dos bairros**  
   - Resultado: `shape_bairros.gpkg`.  

6. **Organização e limpeza dos dados socioeconômicos**  
   - Resultado: `tabela3033_final.csv` e `tabela3170_final.csv`.  

7. **Merge das tabelas 3033 e 3170**  
   - Resultado final: `tabela_total_final.csv`.  

---

## 2. Disponibilidade de dados

### 2.1. Dataset 1 – Socioeconômico (`tabela_total_final.csv`)
- **Bairro:** Nome do bairro de Belém.  
- **Habitações:** Número total de habitações no bairro.  
- **Moradores:** Número total de moradores no bairro.  
- **Média:** Média de moradores por habitação (`Moradores ÷ Habitações`).  
- **N:** Número de moradores com renda registrada.  
- **avg:** Renda média dos moradores do bairro.  
- **mdn:** Mediana da renda dos moradores do bairro.  

### 2.2. Dataset 2 – Setores de coleta (`shape_coleta.gpkg`)
- **Setor (número):** Identificação do setor de coleta.  
- **geometry:** Limites do setor de coleta.  
- **Dias da semana / Número de dias:** Frequência de coleta em cada setor.  

### 2.3. Dataset 3 – Geometria dos bairros (`shape_bairros.gpkg`)
- Polígonos geográficos dos bairros de Belém, para análises espaciais e cruzamento com setores de coleta.  

### 2.4. Dataset 4 – (duplicado, placeholder para futuras geometrias ou atualizações)

### 2.5. Dataset 5 – Pontos de descartes irregulares (dados sintéticos a iniciar)
- **Lat / Long:** Coordenadas do ponto de descarte.  
- **Data:** Data do registro.  
- **Frequência:** Frequência de ocorrências no mesmo local.  

---

## 3. Objetivo do estudo

O objetivo é **identificar as regiões de Belém mais vulneráveis ao descarte irregular de lixo**, considerando fatores socioeconômicos, densidade populacional, frequência de coleta e ocorrências de descartes.  

A partir desta análise, a equipe poderá:
- Priorizar setores para ações de fiscalização e educação ambiental.  
- Avaliar lacunas na coleta de lixo urbano.  
- Apoiar políticas públicas de gestão de resíduos sólidos mais eficazes.  

---

## 4. Indicadores de vulnerabilidade

| Indicador                  | Como calcular                                   | Importância                                                  |
| -------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| **Densidade populacional** | Moradores / área do bairro                      | Bairros mais densos tendem a gerar maior quantidade de lixo irregular |
| **Renda baixa**            | Normalizar renda média e mediana (`avg`, `mdn`) | Menor capacidade de investimento em descarte adequado        |
| **Frequência de coleta**   | 1 - (dias de coleta / 7)                        | Menor frequência aumenta risco de descarte irregular         |
| **Índice de descartes**    | Número de descartes / moradores ou / área       | Direto indicador de ocorrência de descarte irregular         |

---

## 5. Proposta de índice composto

O **Índice de Vulnerabilidade ao Descarte Irregular** pode ser calculado como:

Vulnerabilidade=w1⋅densidade normalizada+w2⋅renda normalizada+w3⋅frequeˆncia de coleta normalizada+w4⋅descartes normalizada

- **Normalização:** todos os indicadores em escala 0–1.  
- **Pesos \(w_i\):** podem ser iguais inicialmente ou ajustados conforme prioridade do estudo.  

---

## 6. Passos sugeridos para análise

1. **Preparação dos dados** ✅
   - Importar shapefiles e planilhas.  
   - Limpeza e padronização (nomes de bairros, geometria, datas).  

2. **Criação de indicadores** 
   - Calcular densidade populacional.  
   - Normalizar renda média e mediana.  
   - Calcular frequência de coleta relativa.  
   - Mapear pontos de descartes irregulares e calcular índices relativos.  

3. **Construção do índice composto**
   - Normalizar indicadores.  
   - Aplicar pesos e combinar em índice único de vulnerabilidade.  

4. **Visualização**
   - Mapas de calor por bairro/setor usando `geopandas` + `folium` ou `plotly`.  
   - Sobreposição de setores de coleta para identificar lacunas.  

5. **Análise e interpretação** 
   - Identificar regiões críticas.  
   - Avaliar correlações entre vulnerabilidade e frequência de descarte irregular.  

6. **Relatórios e recomendações**
   - Preparar relatórios para gestores públicos e equipes de campo.  
   - Sugerir medidas preventivas e corretivas.  

### Fluxo conceitual
```
[Dataset 1: Socioeconômico - tabela_total_final.csv]   
           | 
           v
[Preparação de Dados]
  - Limpeza e padronização de nomes de bairros e colunas
  - Verificação de consistência
           |
           v
[Criação de Indicadores]
  - Densidade populacional (Moradores / área)        <- tabela_total_final.csv + shape_bairros.gpkg
  - Renda média e mediana normalizada                <- tabela_total_final.csv
  - Frequência de coleta relativa                    <- shape_coleta.gpkg
  - Índice de descartes (descartes / população ou área) <- shape_bairros.gpkg + Dataset 5 (descartes sintéticos)
           |
           v
[Normalização dos Indicadores]  <- todos os indicadores anteriores (0–1)
           |
           v
[Construção do Índice Composto de Vulnerabilidade]
  - Combinação ponderada dos indicadores
           |
           v
[Visualização Geográfica]  
  - Mapas de calor / cor por bairro ou setor         <- shape_bairros.gpkg + shape_coleta.gpkg + Dataset 5
  - Sobreposição de setores de coleta                <- shape_coleta.gpkg
           |
           v
[Análise e Interpretação]
  - Identificação de regiões críticas               <- resultado do índice + mapas
  - Avaliação de correlação com frequência de descarte
           |
           v
[Relatórios e Recomendações]
  - Ações prioritárias para fiscalização            <- todos os resultados anteriores
  - Estratégias de coleta e intervenção
 
```
