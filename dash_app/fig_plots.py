
# fig_plots
import folium
import numpy as np
import pandas as pd
import plotly.colors
import plotly.graph_objects as go
from dash import html
from scipy.stats import pearsonr
from scipy.stats import t


def get_paleta(x,cor_unica=None):
    paletas = {
        'area_km2': 'Blues',
        'Hab': 'YlOrRd',
        'Mor': 'YlOrRd',
        'Mor/Hab': 'YlOrRd',
        'N_ren': 'Reds',
        'NS': 'Reds',
        'ren_avg': 'RdYlGn',
        'ren_mdn': 'RdYlGn',
        'T.A.': 'RdBu',
        'IDH-R': 'RdBu',
        'IDH-L': 'RdBu',
        'IDH-E': 'RdBu',
        'IDH': 'RdBu',
        'QTI': 'RdYlGn',
        'CRA': 'Blues',
        'PPR': 'Reds',
        'nd_med': 'RdYlGn',
        'DIEs': 'RdYlGn_r',
        'N_setores': 'Blues'}

    # Obtém a paleta ou usa padrão
    paleta_name = paletas.get(x, 'Greys')
    if cor_unica is not None:
        scale_cor={'area_km2':0.50,
                   'Hab':0.4,
                   'ren_avg':0.2,
                   'ren_mdn':0.15,
                   'Mor/Hab':0.75,
                   'T.A.':0.80,
                    'IDH-R': 0.75,
                    'IDH-L':0.75,
                    'IDH':0.75,
                    'CRA': 0.50,
                    'IDH-E':0.75,
                    'nd_med':0.80,
                    'N_setores':0.5}
        idx=scale_cor.get(x,0.25)
        paleta_name = plotly.colors.sample_colorscale(paleta_name, [idx])[0]
    return paleta_name

def kpis_out(df,x):
    serie = df[x].dropna()

    # Estilo compacto
    card_style = {
        'background': 'white',
        'padding': '8px 5px',  # Menor padding
        'borderRadius': '6px',
        'textAlign': 'center',
        'minHeight': '80px',  # Altura controlada
    }

    kpis = [
        html.Div([
            html.H4(f'{serie.mean():.2f}', style={'margin': '5px 0', 'fontSize': '26px'}),
            html.P('Média', style={'margin': '0', 'fontSize': '18px'})
        ], style=card_style),

        html.Div([
            html.H4(f'{serie.median():.2f}', style={'margin': '5px 0', 'fontSize': '26px'}),
            html.P('Mediana', style={'margin': '0', 'fontSize': '18px'})
        ], style=card_style),

        html.Div([
            html.H4(f'{serie.max():.2f}', style={'margin': '5px 0', 'fontSize': '26px'}),
            html.P('Máximo', style={'margin': '0', 'fontSize': '18px'})
        ], style=card_style),

        html.Div([
            html.H4(f'{serie.min():.2f}', style={'margin': '5px 0', 'fontSize': '26px'}),
            html.P('Mínimo', style={'margin': '0', 'fontSize': '18px'})
        ], style=card_style)
    ]
    return kpis

def add_pontos_descartes(map,gdf_d):

    ponto_colors = {
        "Estimados": "gray",
        "Dados": "back"}

    layer_pontos = folium.FeatureGroup(name="Pontos (⚪Estimados/⚫ coletados)", show=False)

    if gdf_d is not None and gdf_d.empty:
        print("AVISO: GeoDataFrame de pontos está vazio!")

    for _, row in gdf_d.iterrows():
        try:
            bairro = row["Bairro"]
            lat = row["lat"]
            lon = row["lon"]
            cor = row["Cor"]

            # Verificar coordenadas válidas
            if pd.isna(lat) or pd.isna(lon):
                print(f"AVISO: Coordenadas inválidas para bairro {bairro}")
                continue

            marker_color = ponto_colors.get(cor, "black")
            popup_html = f"""
            <b>Bairro:</b> {bairro}<br>
            <b>Tipo:</b> {cor}<br>
            <b>Lat:</b> {lat:.5f}<br>
            <b>Lon:</b> {lon:.5f}
            """

            # Adicionar ao layer_pontos
            folium.CircleMarker(
                location=[lat, lon],
                radius=3,
                color=marker_color,
                fill=True,
                fill_color=marker_color,
                fill_opacity=1,
                popup=popup_html,
                tooltip=f"{bairro} — {cor}"
            ).add_to(layer_pontos)

        except Exception as e:
            print(f"Erro ao processar ponto: {e}")
            continue

    layer_pontos.add_to(map)              # Adicionar layer_pontos ao mapa
    folium.LayerControl().add_to(map)     # Adicionar controle de camadas

    return map

MAP_CACHE = {}  # cache LOCAL do módulo
def mapa_folium(gdf, x,gdf_d=None):
    if x in MAP_CACHE:

        return MAP_CACHE[x]

    paleta_name = get_paleta(x)

    # Criar mapa
    map = folium.Map(location=[-1.43, -48.42], zoom_start=12, tiles='CartoDB Positron')

    # Choropleth
    choropleth = folium.Choropleth(
        geo_data=gdf,
        data=gdf,
        columns=['Bairro', x],
        key_on='feature.properties.Bairro',
        fill_color=paleta_name,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=x
    ).add_to(map)

    # Tooltip
    tooltip = folium.features.GeoJsonTooltip(
        fields=['Bairro', x],
        aliases=['Bairro', x],
        style="font-size: 12px;"
    )
    choropleth.geojson.add_child(tooltip)

    if gdf_d is not None:
        map=add_pontos_descartes(map,gdf_d)
        MAP_CACHE[x] = map

        return map
    else:
        MAP_CACHE[x] = map

        return map

def toptop_bairro(df,x):
    paleta_name=get_paleta(x)

    rank=15
    top = df.nlargest(rank, x).sort_values(x, ascending=True)

    # Define limites da escala de cores
    cmin_val = df[x].min()  # ou df[x].min() para escala global
    cmax_val = df[x].max()  # ou df[x].max() para escala global

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=top['Bairro'],
            x=top[x],
            orientation='h',
            texttemplate='%{x:.2f}',
            marker=dict(
                color=top[x],  # Valores para o gradiente
                colorscale=paleta_name,
                cmin=cmin_val,
                cmax=cmax_val,
                opacity=0.7,
                line=dict(width=1, color='white')),
            hovertemplate=f'<b>%{{y}}</b><br>{x}: %{{x}}<extra></extra>',
            name=x
        )
    )
    fig.update_layout(title='Bairros com maiores valores')
    return fig


def histplot_bairro_px(df,x):

    cor_hist=get_paleta(x,cor_unica=1)

    nb=10
    fig = go.Figure()
    fig.add_trace(
        go.Histogram(
            x=df[x],
            nbinsx=nb,
            histnorm='percent',
            texttemplate='%{y:.1f}%',
            textposition='inside',
            marker=dict(color=cor_hist,
                        line=dict(width=1, color='white')) ),
    )
    fig.update_layout(xaxis_title=x,yaxis_title='percentual(%)')

    return fig

def boxplot_bairro_px(df,x):
    cor_box=get_paleta(x,cor_unica=1)

    fig = go.Figure()

    fig.add_trace(
        go.Box(
            y=df[x],
            boxpoints='all',
            name=x,
            opacity=1,
            marker=dict(color=cor_box,
                        line=dict(width=1, color='white'),
                        opacity=0.99)) )

    return fig


def scatterplot_bairro_px(df, x, hue_var=None, teste=None):
    palette = {
        "Ideal": "#02a84f",
        "Baixo": "#f7e305",
        "Alto": "#f7870f",
        "Critico": "#f01707"}
    cor_fill = get_paleta(x, cor_unica=1)

    # =========================
    # Colunas necessárias
    # =========================
    y = 'QTI'
    cols = [x, y]

    if hue_var:
        cols.append(hue_var)

    if "Bairro" in df.columns:
        cols.append("Bairro")

    dados = df[cols].dropna()

    if x == hue_var:
        dados.columns.values[0] = 'Risco'
        x = 'Risco'
    dados = dados.loc[:, ~dados.columns.duplicated()]  # remover colunas duplicadas

    if 'Risco' in dados.columns:
        mapeamento = {
            1: 'Ideal',
            2: 'Baixo',
            3: 'Alto',
            4: 'Critico'}
        dados['Risco'] = dados['Risco'].map(mapeamento)

    if len(dados) < 2:
        print('dados insuficientes')
        return None
    else:
        x_vals = dados[x].values
        y_vals = dados[y].values
        correlacao, p_valor = pearsonr(x_vals, y_vals)

        coef_angular, intercepto = np.polyfit(x_vals, y_vals, 1)

        stats = {
            "variavel_x": x,
            "variavel_y": y,
            "correlacao": correlacao,
            "p_valor": p_valor,
            "r_quadrado": correlacao ** 2,
            "coef_angular": coef_angular,
            "intercepto": intercepto,
            "equacao": f"y = {coef_angular:.4f}x + {intercepto:.4f}",
            "n": len(dados)}

        # 1. Primeiro: CRIAR FIGURA VAZIA
        fig = go.Figure()

        # 2. SEGUNDO: Banda de confiança (camada mais baixa)
        # Preparar dados da banda
        x_range = np.linspace(x_vals.min(), x_vals.max(), 100)
        y_pred = coef_angular * x_range + intercepto

        n = len(x_vals)
        x_mean = np.mean(x_vals)

        # Resíduos e erro padrão
        y_hat = coef_angular * x_vals + intercepto
        residuos = y_vals - y_hat
        s_err = np.sqrt(np.sum(residuos ** 2) / (n - 2))

        # Inicializar variáveis
        y_upper = None
        y_lower = None
        p_perm = None

        if teste is None:
            # Intervalo de confiança clássico
            t_val = t.ppf(0.975, df=n - 2)
            Sxx = np.sum((x_vals - x_mean) ** 2)
            conf = t_val * s_err * np.sqrt(1 / n + (x_range - x_mean) ** 2 / Sxx)
            y_upper = y_pred + conf
            y_lower = y_pred - conf

        elif teste == "bootstrap":
            # Intervalo de confiança via bootstrap
            B = 5000
            y_boot = np.zeros((B, len(x_range)))
            r_perm = np.zeros(B)

            r_obs, _ = pearsonr(x_vals, y_vals)

            for b in range(B):
                idx = np.random.randint(0, n, n)
                xb = x_vals[idx]
                yb = y_vals[idx]
                m_b, c_b = np.polyfit(xb, yb, 1)
                y_boot[b, :] = m_b * x_range + c_b

                y_perm = np.random.permutation(y_vals)
                r_perm[b], _ = pearsonr(x_vals, y_perm)

            p_perm = np.mean(np.abs(r_perm) >= abs(r_obs))
            y_lower = np.percentile(y_boot, 2.5, axis=0)
            y_upper = np.percentile(y_boot, 97.5, axis=0)

        # Adicionar banda de confiança (PRIMEIRA camada)
        if y_upper is not None and y_lower is not None:
            fig.add_trace(
                go.Scatter(
                    x=np.concatenate([x_range, x_range[::-1]]),
                    y=np.concatenate([y_upper, y_lower[::-1]]),
                    fill='toself',
                    fillcolor=cor_fill,
                    opacity=0.5,
                    line=dict(color='rgba(255,255,255,0)'),
                    hoverinfo="skip",
                    showlegend=False,
                    name='IC 95%'))

        # 3. TERCEIRO: Linha de regressão (camada intermediária)
        fig.add_trace(
            go.Scatter(
                x=x_range,
                y=y_pred,
                mode='lines',
                line=dict(color='black', width=2, dash='solid'),
                name='Linha de regressão',
                showlegend=True,
                legendgroup="regressao"
            )
        )

        # 4. QUARTA: Pontos do scatterplot (camada mais ALTA/sobreposta)
        if hue_var and hue_var in dados.columns:
            categorias = dados[hue_var].unique()
            for categoria in categorias:
                dados_cat = dados[dados[hue_var] == categoria]

                fig.add_trace(
                    go.Scatter(
                        x=dados_cat[x],
                        y=dados_cat[y],
                        mode='markers',
                        marker=dict(
                            size=12,
                            color=palette.get(categoria, '#888888'),
                            opacity=1
                        ),
                        name=str(categoria),
                        text=dados_cat['Bairro'] if 'Bairro' in dados_cat.columns else None,
                        hoverinfo='text+x+y',
                        showlegend=True
                    )
                )
        else:
            # Sem categoria
            fig.add_trace(
                go.Scatter(
                    x=dados[x],
                    y=dados[y],
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='blue',
                        opacity=0.9,
                        line=dict(width=1, color='black')
                    ),
                    name='Dados',
                    text=dados['Bairro'] if 'Bairro' in dados.columns else None,
                    hoverinfo='text+x+y',
                    showlegend=True
                )
            )

    # =========================
    # Layout e formatação
    # =========================
    texto_stats = (
        f"<b>Estatísticas</b><br>"
        f"r = {stats['correlacao']:.4f}<br>"
        f"r² = {stats['r_quadrado']:.4f}<br>"
        f"n = {stats['n']}<br>"
        f"{stats['equacao']}")

    if p_perm is not None:
        texto_stats += f"<br>p-perm = {p_perm:.4f}"

    fig.add_annotation(
        x=0.01,
        y=0.99,
        xref="paper",
        yref="paper",
        showarrow=False,
        align="left",
        text=texto_stats,
        bgcolor="#eef2f7",
        opacity=0.85
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title=x,
        yaxis_title=y,
        legend_title=hue_var)

    fig.update_traces(marker_size=12, marker_opacity=0.8)

    # Interpretação da correlação
    r_abs = abs(correlacao)
    if r_abs >= 0.8:
        força = "MUITO FORTE"
    elif r_abs >= 0.6:
        força = "FORTE"
    elif r_abs >= 0.4:
        força = "MODERADA"
    elif r_abs >= 0.2:
        força = "FRACA"
    else:
        força = "MUITO FRACA"

    direcao = "POSITIVA" if correlacao > 0 else "NEGATIVA"
    alpha = 0.05

    if p_perm is not None:
        significancia = f"ESTATISTICAMENTE SIGNIFICATIVA Valor-perm: {p_perm:.4f}" if p_perm < alpha else f"NÃO SIGNIFICATIVA Valor-perm: {p_perm:.4f}"
    else:
        significancia = f"ESTATISTICAMENTE SIGNIFICATIVA Valor-p: {p_valor:.4f}" if (isinstance(p_valor, (int,
                                                                                                          float)) and p_valor < 0.05) else f"NÃO SIGNIFICATIVA Valor-p: {p_valor:.4f}"
    #print(f"Interpretação: {força} correlação {direcao} ({significancia})")

    return fig
