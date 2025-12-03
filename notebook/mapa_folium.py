import folium
from branca.colormap import LinearColormap
import numpy as np
import json
import os

import geopandas as gpd
import pandas as pd
# Importar configurações de features
from setup_notebook import setup_path
from src.feature_config import *

# Importar configurações de features
#from feature_config import get_feature_config, color_palettes, feature_names, feature_palettes

# leitura da geometria dos bairros
path='/home/akel/PycharmProjects/Data_ambiental/data/process/'
gdf = gpd.read_file(path+'shape_bairros.gpkg').rename(columns={'NM_BAIRRO': 'Bairro'})


# pontos de descartes
gpd_p = gpd.read_file(path+'Pontos_descartes_ML.gpkg')

# leitura das Features 1
df = pd.read_csv(path + "tabela_total_com_DIEs.csv")
#leitura das Features2
df2 = pd.read_csv(path + "Bairros_Ncoleta.csv")


#f eatures1+features 2
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
gdf1=gdf_merged[['Bairro','geometry','Hab','IDH']]
#gdf1.info()

gdf_m=gdf_merged.copy()

# Função para carregar templates
def load_template(template_name):
    template_path = os.path.join('templates', template_name)
    print(template_path)
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()


centro_lat, centro_lon = -1.427897, -48.4162631
m = folium.Map(location=[centro_lat, centro_lon],     tiles="CartoDB Positron",
zoom_start=13)

# 1. Carregar container HTML
colormap_container = load_template('colormap_container.html')
m.get_root().html.add_child(folium.Element(colormap_container))

# 2. Definir features para mapear
features_to_map=['area_km2', 'Hab', 'Mor', 'Mor/Hab', 'N_ren', 'ren_avg', 'ren_mdn', 'T.A.', 'IDH-R', 'IDH-L', 'IDH-E', 'IDH', 'PPR', 'DIEs', 'Dies_cat','nd_med']

print(f"Total de features disponíveis para mapeamento: {len(features_to_map)}")
print("Features:", features_to_map)

# 3. Configurar features
features_config = get_feature_config(gdf_m, features_to_map, color_palettes, feature_names, feature_palettes)

print(f"\nFeatures configuradas com sucesso: {len(features_config)}")

tooltip_fields = ['Bairro'] + list(features_config.keys())
tooltip_aliases = ['Bairro: '] + [features_config[f]['name'] + ': ' for f in features_config.keys()]
# 4. Criar camadas para cada feature
for feature, config in features_config.items():
    layer = folium.FeatureGroup(name=config['name'], show=config['show'])

    folium.GeoJson(
        gdf_m,
        style_function=lambda x, feat=feature, cmap=config['colormap']: {
            'fillColor': cmap(x['properties'][feat]) if x['properties'][feat] is not None else "#808080",
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.6
        },
        tooltip=folium.GeoJsonTooltip(
                     fields=tooltip_fields,
                    aliases=tooltip_aliases,
                     localize=True,
                     style="background-color: white; border: 1px solid black; padding: 8px; max-width: 300px;")
    ).add_to(layer)

    layer.add_to(m)

# Add nome dos bairro no mapa.
rotulos_layer = folium.FeatureGroup(name="Nomes Bairros", show=True)
# Adiciona todos os rótulos de uma vez
for _, row in gdf_m.iterrows():
    centroid = row.geometry.centroid
    folium.Marker(
        location=[centroid.y, centroid.x],
        icon=folium.DivIcon(
            html=f'''
            <div style="
                font-size: 10px; 
                background-color: rgba(255, 255, 255, 0.3);
                text-align: center;
                padding: 2px 20 px;
                border-radius: 3px;
                white-space: nowrap;
                display: inline-block;
            ">
                {row["Bairro"]}
            </div>
            '''
        )
    ).add_to(rotulos_layer)
rotulos_layer.add_to(m)

# # 5. Tooltip
# tooltip_fields = ['Bairro'] + list(features_config.keys())
# tooltip_aliases = ['Bairro: '] + [features_config[f]['name'] + ': ' for f in features_config.keys()]
#
# folium.GeoJson(
#     gdf_m,
#     style_function=lambda x: {'color': 'transparent', 'fillColor': 'transparent', 'weight': 0},
#     tooltip=folium.GeoJsonTooltip(
#         fields=tooltip_fields,
#         aliases=tooltip_aliases,
#         localize=True,
#         style="background-color: white; border: 1px solid black; padding: 8px; max-width: 300px;"
#     )
# ).add_to(m)

# 6. Preparar dados JavaScript
colormap_data_js = {}
for feature, config in features_config.items():
    clean_name = ''.join(c for c in config['name'] if c.isalnum() or c.isspace())
    colormap_data_js[clean_name] = config['html']

# 7. Carregar e injetar JavaScript dinâmico
dynamic_js = load_template('dynamic_colormap.js')
# Substituir placeholder pelos dados
dynamic_js = dynamic_js.replace('{{COLORMAP_DATA}}', json.dumps(colormap_data_js, ensure_ascii=False))
dynamic_js = dynamic_js.replace('{{NAME_MAPPING}}', json.dumps(
    {config["name"]: name for name, config in zip(colormap_data_js.keys(), features_config.values())},
    ensure_ascii=False
))

m.get_root().html.add_child(folium.Element(dynamic_js))

# 8. Controle de camadas
folium.LayerControl(collapsed=False).add_to(m)

# 9. Carregar controle de legenda
legend_control = load_template('legend_control.html')
m.get_root().html.add_child(folium.Element(legend_control))

# 10. Carregar JavaScript da legenda
legend_js = load_template('legend_control.js')
m.get_root().html.add_child(folium.Element(legend_js))

print(f"\n✅ Mapa criado com {len(features_config)} features temáticas!")
print("🎯 Controles:")
print("   • Use o controle de camadas (canto superior direito) para alternar entre features")
print("   • Use a lista de legendas (canto superior esquerdo) para seleção rápida")
print("   • Passe o mouse sobre os bairros para ver todos os dados")

m.save('/home/akel/PycharmProjects/Data_ambiental/docs/mapa_interativo_teste.html')