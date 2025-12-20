
# load_process.py
import pandas as pd
import geopandas as gpd
import os

def load_files(ponto_descarte=None):
    # Leitura dos DADOS & organização

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)

    DATA_DIR = os.path.join(ROOT_DIR, "data", "process")
    #print('Debug BASE_DIR:',BASE_DIR)
    #print('Debug PARENT_DIR:',PARENT_DIR)

    gdf = gpd.read_file(os.path.join(DATA_DIR, "shape_bairros.gpkg")).rename(columns={'NM_BAIRRO': 'Bairro'})
    df1 = pd.read_csv(os.path.join(DATA_DIR, "tabela_total_com_DIEs.csv"))
    df2 = pd.read_csv(os.path.join(DATA_DIR, "Bairros_Ncoleta.csv"))

    path = '/home/akel/PycharmProjects/Dash_apps/data/process/'
    #gdf = gpd.read_file(path + 'shape_bairros.gpkg').rename(columns={'NM_BAIRRO': 'Bairro'})
    #df1 = pd.read_csv(path + 'tabela_total_com_DIEs.csv')
    #df2 = pd.read_csv(path + 'Bairros_Ncoleta.csv')

    df = df1.merge(df2, on='Bairro', how='left')
    gdf_m = gdf.merge(df, on='Bairro', how='left')

    #add % de Moradores sem renda
    gdf_m['NS']=(gdf_m['Mor']-gdf_m['N_ren'])/gdf_m['Mor']
    colunas = list(gdf_m.columns)
    colunas.remove('NS')
    colunas.insert(7, 'NS')
    gdf_m = gdf_m[colunas]
    # Função de categorização

    def categorizar_dies(dies):
        if dies == 0:
            return 1
        elif 1 <= dies <= 3:
            return 2
        elif 4 <= dies <= 6:
            return 3
        else:
            return 4

    gdf_m['Risco'] = gdf_m['DIEs'].apply(categorizar_dies)

    df_plot = gdf_m.drop(columns=['geometry','V_setores_val'])

    list_feature = df_plot.drop(columns='Risco').select_dtypes(include=['number']).columns

    feat_options = []
    for feature in list_feature:
        feat_options.append({'label': feature, 'value': feature, 'description': None})

    feat_options[0]['description'] = 'Área do Bairro (km²)'
    feat_options[1]['description'] = 'Número Total de Habitações'
    feat_options[2]['description'] = 'Número Total de Moradores'
    feat_options[3]['description'] = 'relação Moradores/Habitação'
    feat_options[4]['description'] = 'Números totais de Moradores com Renda'
    feat_options[5]['description'] = '% de moradores sem renda'
    feat_options[6]['description'] = 'Renda média do Morador'
    feat_options[7]['description'] = 'Mediana da renda do Morador'
    feat_options[8]['description'] = 'Taxa de alfabetização'
    feat_options[9]['description'] = 'IDH Renda'
    feat_options[10]['description'] = 'IDH Longevidade'
    feat_options[11]['description'] = 'IDH Educação'
    feat_options[12]['description'] = 'Indice de desenvolvimento Humano'
    feat_options[13]['description'] = 'Quantidade de Deposito Irregulares '
    feat_options[14]['description'] = 'Concentração Riqueza por area( Ren_avg x (Mor/Hab)/Area_km)'
    feat_options[15]['description'] = 'Percentual da populção com rendimento'
    feat_options[16]['description'] = 'Quantidade de Depósitos Irregulares estimado'
    feat_options[17]['description'] = 'Média de dias de coleta de lixo'
    feat_options[18]['description'] = 'Quantidade de setores/rotas de coleta'

    if ponto_descarte is not None:
        gdf_p = gpd.read_file(os.path.join(DATA_DIR, "Pontos_descartes_ML.gpkg"))
        #gdf_p = gpd.read_file(path + 'Pontos_descartes_ML.gpkg')
        return gdf_m,df_plot,list_feature, feat_options, gdf_p
    else:
        print('debub: sem arquivo descartes')
        return gdf_m,df_plot,list_feature, feat_options
