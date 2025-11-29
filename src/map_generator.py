import geopandas as gpd
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import warnings
warnings.filterwarnings(
    "ignore",
    message=".*choropleth_mapbox.*deprecated.*")
pio.renderers.default = "notebook_connected"


# Define a função principal que retorna o objeto Plotly
def generate_interactive_map():
    path='/home/akel/PycharmProjects/Data_ambiental/data/process/'


    # --- LEITURA E PROCESSAMENTO DE DADOS ---
    # leitura da geometria dos bairros
    gdf = gpd.read_file(path + 'shape_bairros.gpkg').rename(columns={'NM_BAIRRO': 'Bairro'})
    # pontos de descartes
    gpd_p = gpd.read_file(path + 'Pontos_descartes_ML.gpkg')

    # leitura das Features 1
    df = pd.read_csv(path + "tabela_total_com_DIEs.csv")
    # leitura das Features 2
    df2 = pd.read_csv(path + "Bairros_Ncoleta.csv")

    # features1 + features 2
    df = df.merge(df2, on="Bairro", how="left")
    gdf_merged = gdf.merge(df, on="Bairro", how="left")

    # Categorizar
    def categorizar_dies(dies):
        if dies == 0:
            return 1
        elif 1 <= dies <= 3:
            return 2
        elif 4 <= dies <= 6:
            return 3
        else:  # dies >= 7
            return 4

    gdf_merged['Dies_cat'] = gdf_merged['DIEs'].apply(categorizar_dies)

    # --- VARIÁVEIS DE VISUALIZAÇÃO ---
    variaveis = ['area_km2', 'Hab', 'Mor', 'Mor/Hab', 'N_ren', 'ren_avg', 'ren_mdn', 'T.A.', 'IDH-R', 'IDH-L', 'IDH-E',
                 'IDH', 'PPR', 'DIEs', 'Dies_cat', 'nd_med']
    escalas = ["blues", "reds", "reds", "reds", "RdYlGn", "RdYlGn", "RdYlGn", "rdbu", "rdbu", "rdbu", "rdbu", "rdbu",
               "rdbu", 'RdYlGn_r', "RdYlGn_r", "RdYlGn"]

    centro_lat, centro_lon = -1.427897, -48.4162631

    # --- CONSTRUÇÃO DO MAPA INTERATIVO (O restante do seu código) ---
    fig = go.Figure()

    # Adicionar traces Choropleth
    for i, (var, scale) in enumerate(zip(variaveis, escalas)):
        fig.add_trace(go.Choroplethmap(
            geojson=gdf_merged.geometry.__geo_interface__,
            locations=gdf_merged.index,
            z=gdf_merged[var],
            colorscale=scale,
            visible=(i == 0),
            marker_opacity=0.5,
            hovertext=gdf_merged["Bairro"],
            hoverinfo="text+z",
            colorbar_title=var,
            name=var,
            showlegend=False
        ))

    # Adicionar pontos de descarte - DADOS e ESTIMADOS
    pontos_dados = gpd_p[gpd_p["Cor"] == "Dados"]
    fig.add_trace(go.Scattermap(
        lat=pontos_dados["lat"], lon=pontos_dados["lon"], mode='markers',
        marker=dict(size=8, color="darkblue"),
        hovertext=pontos_dados["Bairro"], hoverinfo="text", name="Coletados",
        showlegend=True, visible=True
    ))

    pontos_estimados = gpd_p[gpd_p["Cor"] == "Estimados"]
    fig.add_trace(go.Scattermap(
        lat=pontos_estimados["lat"], lon=pontos_estimados["lon"], mode='markers',
        marker=dict(size=8, color="red"),
        hovertext=pontos_estimados["Bairro"], hoverinfo="text", name="Estimados",
        showlegend=True, visible=True
    ))

    # Criar botões HORIZONTAIS
    buttons = []
    for i, var in enumerate(variaveis):
        visibility = [False] * len(variaveis) + [True, True]
        visibility[i] = True

        buttons.append(
            dict(
                label=var,
                method="update",
                args=[
                    {"visible": visibility},
                    {"title": f"Variável: {var}"}
                ]
            )
        )

    # Configurações de layout
    fig.update_layout(
        map_style="carto-positron",
        map_center={"lat": centro_lat, "lon": centro_lon},
        map_zoom=12,
        updatemenus=[
            dict(
                type="buttons", direction="right", buttons=buttons, x=0.05, y=1.02,
                xanchor="left", yanchor="bottom", bgcolor="lightgray", bordercolor="black",
                borderwidth=1, pad={"r": 10, "t": 10}, showactive=True
            )
        ],
        height=720,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        legend=dict(
            yanchor="top", y=0.99, xanchor="left", x=0.01,
            bgcolor="rgba(255, 255, 255, 0.8)"
        )
    )

    html_output_path = os.path.join(os.getcwd(), 'mapa_bairros_interativo.html')
    fig.write_html(html_output_path)
    return fig

# Note: Remova fig.show() daqui. O .ipynb cuidará disso.