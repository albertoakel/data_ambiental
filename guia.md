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
  
8. **Dias de coleta por Bairro**  
   - Resultado final: `Bairros_Ncoleta.csv`.

### Dataset finais

1. `tabela_total_com_DIEs.csv`
2. `shape_bairros.gpkg`
3. `shape_coleta.gpkg`
4. `Pontos_descartes_ML.gpkg`
5. `Bairros_Ncoleta.csv`
---

## 2. Disponibilidade de dados

### 2.1. Dataset 1 – Socioeconômico (`tabela_total_com_DIEs.csv`)
- `Bairro:` Nome do bairro de Belém.
- `area_km2` Aréa do bairro  
- `Hab:` Número total de habitações no bairro.  
- `Mor:` Número total de moradores no bairro.  
- `Mor/Hab:` Média de moradores por habitação (`Moradores ÷ Habitações`).  
- `N_ren:` Número de moradores com renda registrada.  
- `ren_avg:`Renda média dos moradores do bairro.  
- `ren_mdn` Mediana da renda dos moradores do bairro
- `T.A.` Taxa de alfabetização
- `IDH-R` Índice de desenvolvimento humano Renda
- `IDH-L` Índice de desenvolvimento humano Longevidade
- `IDH-E` Índice de desenvolvimento humano Educação
- `IDH` Índice de desenvolvimento humano
- `QTI` Quantidade de Depósitos Irregulares
- `CRA` Mediana da renda dos moradores do bairro
- `PPR` Percentual Populacao_rendimento
- `DIEs` Quantidade de Depósitos Irregulares estimado

### 2.2. Dataset 2 – Geometria dos bairros (`shape_bairros.gpkg`)
- `Bairro:`	Local
- `geometry:` Limites do bairro
  
### 2.3. Dataset 3 – Setores de coleta (`shape_coleta.gpkg`)
- `area_coleta:` Identificação da area
- `setor:` Identificação da area
- `horario:` Horario da coleta( diurno/Noturno)
- `dias	num_dias:` 1,2,3,4,5,6,
- `latitude_ref:` lat referencia do  da webscraping
- `longitude_ref:` long referencia do  da webscraping
- `geometry:` geometria da coleta

### 2.5. Dataset 4 – Pontos de descartes irregulares (`Pontos_descartes_ML.gpkg`)
- `Bairro:`	Local
- `lat:`latitude do ponto de descarte 
- `lon:`longitude do ponto de descarte
- `Cor:` Tipo, se é estimado, ou coletado
- `geometry:` ponto geografico (lat,long)
## 3. Objetivo do estudo

O objetivo é **identificar as regiões de Belém mais vulneráveis ao descarte irregular de lixo**, considerando fatores socioeconômicos, densidade populacional, frequência de coleta e ocorrências de descartes.  

A partir desta análise, a equipe poderá:
- Definir o conjunto de dadaset   
- Priorizar setores para ações de fiscalização e educação ambiental.  
- Avaliar lacunas na coleta de lixo urbano. 
- Apoiar políticas públicas de gestão de resíduos sólidos mais eficazes.  

---

## 4. Possiveis Indicadores de vulnerabilidade 

| Indicador                  | Como calcular                                   | Importância                                                  |
| -------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| **Densidade populacional** | Moradores / área do bairro                      | Bairros mais densos tendem a gerar maior quantidade de lixo irregular |
| **Renda baixa**            | Normalizar renda média e mediana (`avg`, `mdn`) | Menor capacidade de investimento em descarte adequado        |
| **Frequência de coleta**   | 1 - (dias de coleta / 7)                        | Menor frequência aumenta risco de descarte irregular         |
| **Índice de descartes**    | Número de descartes / moradores ou / área       | Direto indicador de ocorrência de descarte irregular         |

---

## 5. Proposta de índice composto ❌

O **Índice de Vulnerabilidade ao Descarte Irregular** pode ser calculado como:

Vulnerabilidade=w1⋅densidade normalizada+w2⋅renda normalizada+w3⋅frequeˆncia de coleta normalizada+w4⋅descartes normalizada

- **Normalização:** todos os indicadores em escala 0–1.  
- **Pesos wiw_i:** podem ser iguais inicialmente ou ajustados conforme prioridade do estudo.  

---

## 6. Passos sugeridos para análise

1. **Preparação dos dados** ✅
   - Importar shapefiles e planilhas.  
   - Limpeza e padronização (nomes de bairros, geometria, datas).  

2. **Criação de indicadores** ✅
   - Calcular densidade populacional.  
   - Normalizar renda média e mediana.  
   - Calcular frequência de coleta relativa.  
   - Mapear pontos de descartes irregulares e calcular índices relativos.  

3. **Construção do índice composto** ❌
   - Normalizar indicadores.  
   - Aplicar pesos e combinar em índice único de vulnerabilidade.  

4. **Visualização** ✅
   - Mapas de calor por bairro/setor usando `geopandas` + `folium` ou `plotly`.  
   - Sobreposição de setores de coleta para identificar lacunas.  

5. **Análise e interpretação** ✅
   - Identificar regiões críticas.  
   - Avaliar correlações entre vulnerabilidade e frequência de descarte irregular.  

6. **Relatórios e recomendações**✅
   - Preparar relatórios para gestores públicos e equipes de campo.  
   - Sugerir medidas preventivas e corretivas. 



---
## Referência Bibliográfica

GONÇALVES, Diego Andrews Hayden. **Uma Cartografia do lixo em Belém (PA): distribuição espacial de depósitos irregulares de lixo e o dever do estado para o desenvolvimento sustentável**. 2023. 206 f. Dissertação (Mestrado em Planejamento do Desenvolvimento) - Núcleo de Altos Estudos Amazônicos, Universidade Federal do Pará, Belém, 2023. Orientador: Hisakhana Pahoona Corbin. Disponível em: https://repositorio.ufpa.br/jspui/handle/2011/16206. Acesso em: [inserir data de acesso].

LIMA, Marlon de Morais. **Análise da gestão dos resíduos sólidos produzidos nas ilhas do Combú e Cotijuba no município de Belém-PA**. 2021. 63 f. Trabalho de Conclusão de Curso (Graduação em Engenharia Ambiental e Energias Renováveis) - Campus Universitário de Belém, Universidade Federal Rural da Amazônia, Belém, 2021. Orientadora: Profa. Dra. Paula Fernanda Pinheiro Ribeiro Paiva.

GOMES, Bárbara; ARAÚJO, José; PONTES, Altem. **Descarte irregular de resíduos sólidos no bairro do Tapanã em Belém/PA: uma análise socioambiental**. Contribuciones a las Ciencias Sociales, [S. l.], v. 18, n. 4, p. e17071, 2025. DOI: [10.55905/revconv.18n.4-180](https://doi.org/10.55905/revconv.18n.4-180). Disponível em: https://www.researchgate.net/publication/390776144_Descarte_irregular_de_residuos_solidos_no_bairro_do_Tapana_em_BelemPA_uma_analise_socioambiental. Acesso em: [inserir data de acesso].

ABREMA - ASSOCIAÇÃO BRASILEIRA DE RESÍDUOS E MEIO AMBIENTE. **Panorama dos Resíduos Sólidos no Brasil 2023**. São Paulo: ABREMA, 2023. Disponível em: https://www.abrema.org.br/wp-content/uploads/dlm_uploads/2024/03/Panorama_2023_P1.pdf. Acesso em: 10 out. 2024.
# Referência das Fontes de Dados do IBGE

## Base de Dados SIDRA/IBGE

Para a composição do perfil socioeconômico e demográfico dos bairros de Belém, foram utilizados dados do acervo do **Sistema IBGE de Recuperação Automática (SIDRA)**, disponível em [https://sidra.ibge.gov.br/](https://sidra.ibge.gov.br/).

### Tabelas Utilizadas

#### **Tabela 3033**
- **Título completo:** "Número de domicílios particulares ocupados, pessoas residentes em domicílios particulares ocupados e média de moradores em domicílios particulares ocupados, por situação e localização da área - Sinopse"
- **Variável utilizada:** "Número de domicílios particulares ocupados (Unidades)"
- **Recorte geográfico:** Bairros de Belém
- **Período de referência:** 2010
- **Campos aplicados:**
  - `Bairro`
  - `2010` (Ano x Situação e localização da área)

#### **Tabela 3170**
- **Título completo:** "Pessoas de 10 anos ou mais de idade, com rendimento, Valor do rendimento nominal médio mensal e Valor do rendimento nominal mediano mensal das pessoas de 10 anos ou mais de idade, com rendimento, por sexo, situação do domicílio e grupos de idade"
- **Variável utilizada:** "Pessoas de 10 anos ou mais de idade, com rendimento (Pessoas)"
- **Recorte geográfico:** Bairros de Belém
- **Período de referência:** 2010
- **Campos aplicados:**
  - `Bairro`
  - `Grupo de idade`
  - `2010` (Ano x Situação do domicílio)
  - `Total`

### Nota Metodológica

Os dados do Censo Demográfico 2010 representam a fonte mais recente e abrangente para análise em nível de bairro, fornecendo a base estatística necessária para:
- Cálculo de densidade populacional
- Análise de distribuição de renda
- Caracterização do perfil domiciliar
- Estratificação socioeconômica territorial

**Fonte:** IBGE. Censo Demográfico 2010. Tabelas 3033 e 3170. SIDRA.


### Fluxo conceitual
```
[DATASETS FINAIS DISPONÍVEIS]
  ├── [Dataset 1: Socioeconômico + DIEs] - tabela_total_com_DIEs.csv
  ├── [Dataset 2: Geometria dos Bairros] - shape_bairros.gpkg  
  ├── [Dataset 3: Setores de Coleta] - shape_coleta.gpkg
  ├── [Dataset 4: Pontos de Descartes] - Pontos_descartes_ML.gpkg
  └── [Dataset 5: Frequência de Coleta] - Bairros_Ncoleta.csv

           |
           v
[PREPARAÇÃO E INTEGRAÇÃO DE DADOS] ✅ CONCLUÍDO
  - Limpeza e padronização de nomes de bairros
  - Merge das tabelas socioeconômicas (3033 + 3170)
  - Organização dos shapes e geometrias
  - Webscraping e estruturação dos dados de coleta

           |
           v
[CRIAÇÃO DE INDICADORES DE VULNERABILIDADE] ✅ PARCIALMENTE CONCLUÍDO
  ├── Densidade populacional (Mor / area_km2)
  ├── Indicadores de renda (ren_avg, ren_mdn, CRA, PPR)
  ├── Frequência de coleta relativa (dias / 7)
  ├── Índice de descartes (QTI, DIEs / população)
  ├── Indicadores de desenvolvimento (IDH, IDH-R, IDH-L, IDH-E)
  └── Taxa de alfabetização (T.A.)

           |
           v
[ANÁLISE ESTATÍSTICA E CORRELAÇÕES] ✅ CONCLUÍDO
  - Correlação renda vs. descartes (r = -0.4406)
  - Correlação IDH vs. descartes (r = -0.4399) 
  - Correlação área vs. DIEs (r = 0.564)
  - Correlação população vs. QTI (r = 0.4847)
  - Correlação densidade vs. descartes (r = 0.420)

           |
           v
[CONSTRUÇÃO DO ÍNDICE COMPOSTO] ❌ PENDENTE
  - Normalização dos indicadores (escala 0-1)
  - Combinação ponderada:
    Vulnerabilidade = w1·densidade + w2·(1-renda) + w3·(1-frequência_coleta) + w4·descartes

           |
           v
[VISUALIZAÇÃO GEOGRÁFICA E MAPAS] ✅ PARCIALMENTE CONCLUÍDO
  ├── Mapa de setores de coleta (Figura 1)
  ├── Mapa de renda mediana por bairro (Figura 2)
  ├── Mapas de correlação IDH vs. QTI (Figura 3)
  ├── Mapas de densidade vs. descartes (Figura 4)
  └── Mapa de frequência de coleta (Figura 5)

           |
           v
[IDENTIFICAÇÃO DE REGIÕES CRÍTICAS] ✅ CONCLUÍDO
  - Bairros com baixa renda (≤ R$605 mediana)
  - Bairros com baixo IDH 
  - Áreas com grande extensão territorial
  - Regiões com alta densidade populacional
  - Setores com baixa frequência de coleta (≤3.5 dias/semana)

           |
           v
[RELATÓRIOS E RECOMENDAÇÕES ESTRATÉGICAS] ✅ CONCLUÍDO
  ├── Ações prioritárias para fiscalização
  ├── Estratégias de coleta e intervenção
  ├── Plataforma interativa proposta
  └── Plano de implementação em fases

           |
           v
[PRÓXIMAS ETAPAS: PLATAFORMA INTERATIVA] 🎯 FUTURO
  ├── Aplicativo móvel de geolocalização
  ├── Painel de gestão pública em tempo real
  └── Sistema de monitoramento participativo
```
