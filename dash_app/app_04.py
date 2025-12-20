
# app_04.py
import dash
from load_process import load_files
from layout_01 import criar_layout
from callbacks import registrar_callbacks
from flask_caching import Cache

# Leitura dos dados
#gdf_m,df_plot,list_feature,feat_options=load_files() #original
gdf_m,df_plot,list_feature,feat_options,gdf_p =load_files(ponto_descarte=True)

descriptions_map = {
    opt['value']: opt['description']
    for opt in feat_options
    if opt.get('description') is not None
}

# APP
app = dash.Dash(__name__)
server = app.server  #to render deploy

# Inicialização do CACHE
cache = Cache(server, config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300  # segundos
})

# Configurar layout
app.layout = criar_layout(feat_options)

# Registrar callbacks
registrar_callbacks(app, df_plot, gdf_m,descriptions_map,gdf_p)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=8050)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8052))
    app.run(debug=False, host='0.0.0.0', port=port)