# 📊📉 Dashboard de Diagnóstico Ambiental Urbano

Dashboard interativo em **Python + Dash** para análise ambiental e socioeconômica por **bairro**, integrando dados tabulares e geoespaciais.

---

## 🎯 Objetivo

Explorar indicadores urbanos, identificar padrões espaciais e apoiar a tomada de decisão por meio de visualizações interativas.

---

## 🧱 Estrutura

```

Dash_apps/
├── app_04.py          # Entrypoint
├── load_process.py   # Leitura e processamento de dados
├── callbacks.py      # Lógica reativa
├── fig_plots.py      # Análises e gráficos
├── layout.py         # Interface
├── assets/
│   └── style.css

````

---

## 📊 Funcionalidades

- Mapa coroplético por bairro (Folium)
- KPIs automáticos (média, mediana, min, max)
- Ranking dos bairros
- Histogramas e boxplots
- Scatter com regressão linear e correlação

---

## ▶️ Como executar

```bash
pip install dash pandas geopandas plotly folium scipy
python app_04.py
````

## Acesse [aqui](https://dash-apps-1.onrender.com/)


---

## 📜 Licença

Uso acadêmico e institucional para análise ambiental urbana.


