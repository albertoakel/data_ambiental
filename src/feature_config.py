import numpy as np
from branca.colormap import LinearColormap



# Paletas de cores
color_palettes = {
    'blues': ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b'],
    'reds': ['#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d'],
    'RdGn': ['#a50026', '#c03c2b','#da6540','#f08e58','#a7cf6a','#78b55d','#4a9a4d','#247d3c','#006837'],
    'RdYlGn':['#a50026',  '#d73027','#f46d43','#fdae61','#fee08b','#ffffbf', '#d9ef8b','#a6d96a','#66bd63','#1a9850','#006837'],
    'RdYlGn_r': ['#006837', '#1a9850', '#66bd63', '#a6d96a', '#ffffbf', '#fdae61', '#f46d43', '#d73027', '#a50026'],
    'RdBu': ['#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7', '#d1e5f0', '#92c5de', '#4393c3', '#2166ac'],
    'blues': ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b'],
    'reds': ['#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d'],
    'default': ['#440154', '#482878', '#3e4989', '#31688e', '#26828e', '#1f9e89', '#35b779', '#6ece58', '#b5de2b'],
    'viridis': ['#440154', '#482475', '#414487', '#355f8d','#2a788e', '#21918c', '#22a884', '#44bf70', '#7ad151'],
    'Spectral': ['#9e0142', '#d53e4f', '#f46d43', '#fdae61','#fee08b', '#e6f598', '#abdda4', '#66c2a5', '#3288bd'],
    'seismic': ['#0000ff', '#3f3fff', '#7f7fff', '#bfbfff','#ffffff','#ffbfbf', '#ff7f7f', '#ff3f3f', '#ff0000'],
    'RdYlBu': ['#a50026', '#d73027', '#f46d43', '#fdae61','#fee090', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4'],
    'default': ['#30123b', '#4145ab', '#4679f2', '#3cafdb','#2ed9a3', '#63eb53', '#a4f11a', '#e3dd12', '#fdae11'],
    'GnYlRdPu': [ "#2ECC71",
        "#6ACB63","#A4C957",
        "#D3C548",
        "#F1C40F",
        "#F79A32",
        "#EF6F39",
        "#E74C3C",
        "#D74337",
        "#B93837",
        "#8B3045",
        "#6C3483"
    ]}

feature_names = {
    'area_km2': '🗺️ Área (km²)',
    'Hab': '🏠 Habitações',
    'Mor': ' 👥 Moradores',
    'Mor/Hab': '👨‍👩‍👧‍👦 Moradores por habitação',
    'N_ren': '💰 Moradores com renda',
    'ren_avg': '📊 Renda Média',
    'ren_mdn': '📈 Renda Mediana',
    'T.A.': '🔤 Taxa de alfabetização',
    'IDH-R': '💵 IDH - Renda',
    'IDH-L': '📚 IDH - Longevidade',
    'IDH-E': '🎓 IDH - Educação',
    'IDH': '🏆 IDH Geral',
    'PPR': '🏙️ % Populacao rendimento',
    'DIEs': '⚠️ Qt.Descartes estimados',
    'Dies_cat': '⚠️ Qt.Descartes est. risco',
    'nd_med': '🚛 Frequência de coleta'
}



# Paletas específicas por feature
feature_palettes = {
'area_km2': 'blues',
    'Hab': 'reds',
    'Mor': 'reds',
    'Mor/Hab': 'reds',
    'N_ren' : 'RdYlGn',
    'T.A.':'RdYlBu',
    'IDH': 'RdBu',
    'IDH-R': 'RdBu',
    'IDH-L': 'RdBu',
    'IDH-E': 'RdBu',
    'ren_avg': 'RdYlGn',
    'ren_mdn': 'RdYlGn',
    'DIEs':'GnYlRdPu',
    'Dies_cat':'RdYlGn_r',
    'PPR':'RdBu',
    'nd_med':'RdYlGn'}

def get_feature_config(gdf_m, features_to_map, color_palettes, feature_names, feature_palettes):
    """
    Configura todas as features para mapeamento
    """
    features_config = {}

    for feature in features_to_map:
        # Nome amigável
        name = feature_names.get(feature, f"📊 {feature}")

        # Escolher paleta
        palette_key = feature_palettes.get(feature, 'default')
        colors = color_palettes[palette_key]

        # Dados
        data = gdf_m[feature]

        # Verificar se há dados válidos
        if data.isnull().all():
            print(f"Aviso: Feature '{feature}' tem todos os valores nulos. Pulando.")
            continue

        # Criar colormap
        try:
            colormap = LinearColormap(
                colors,
                vmin=data.min(),
                vmax=data.max(),
                caption=name
            )

            # Gerar HTML
            gradient = ', '.join(colors)
            html = f"""
            <div style="font-weight: bold; margin-bottom: 5px; font-size: 12px;">
                {colormap.caption}
            </div>
            <div style="width: 200px; height: 15px; 
                        background: linear-gradient(to right, {gradient});
                        margin-bottom: 3px; border-radius: 2px;"></div>
            <div style="display: flex; justify-content: space-between; 
                        font-size: 10px; color: #555;">
                <span>{colormap.vmin:.2f}</span>
                <span>{colormap.vmax:.2f}</span>
            </div>
            """

            # Armazenar configuração
            features_config[feature] = {
                'name': name,
                'colormap': colormap,
                'html': html,
                'colors': colors,
                'show': (feature == 'Hab')  # Primeira feature visível por padrão
            }

        except Exception as e:
            print(f"Erro ao processar feature '{feature}': {e}")

    return features_config