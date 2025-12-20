
# callbacks.py
from dash import  Input, Output
from fig_plots import *



def registrar_callbacks(app, df_plot, gdf_m,descriptions_map,gdf_p=None,cache=None ):
    """
        df_plot : DataFrame analítico sem geometria
                  Usado para gráficos estatísticos
        gdf_m   : GeoDataFrame com geometria
                  Usado exclusivamente para mapas
        gdp_p   : GeoDataFrama com pontos de descartes(opcional)
        cache   : Flask-Caching (opcional)
        """


    if cache is not None:
        decorator = cache.memoize()
        #print("Cache ATIVADO nos callbacks")
    else:
        decorator = lambda f: f
        #print("Cache DESATIVADO nos callbacks")

    if gdf_p is not None:
        pass

    @app.callback(
        [Output('kpis', 'children'),
         Output('descricao-variavel', 'children'),  # <<< 2º OUTPUT ADICIONADO
         Output('mapa', 'srcDoc'),
         Output('fig_rank', 'figure'),
         Output('fig_hist', 'figure'),
         Output('fig_box', 'figure'),
         Output('fig_scatter', 'figure')],
        Input('variavel', 'value')
    )
    @decorator
    def atualizar(var):

        # métrica KPIS
        kpis =kpis_out(df=df_plot,x=var)

        # Descrição da variavel Dropdown
        description_text = descriptions_map.get(var,"Descrição não disponível para a variável: " + str(var))
        descricao_componente = html.P([description_text], style={'margin': '0'})

        # Mapa
        #mapa=mapa_folium(gdf=gdf_m, x=var)
        mapa=mapa_folium(gdf=gdf_m, x=var,gdf_d=gdf_p)


        #Rank
        fig_rank=toptop_bairro(df=df_plot,x=var)

        #Histograma
        fig_hist=histplot_bairro_px(df=df_plot,x=var)

        #Boxplot
        fig_box=boxplot_bairro_px(df=df_plot,x=var)

        #dispersão
        fig_scatter = scatterplot_bairro_px(df=df_plot, x=var,hue_var='Risco')

        # FUNDO TRANSPARENTE PARA TODOS
        for fig in [fig_hist, fig_box, fig_rank, fig_scatter]:
            fig.update_layout(
                paper_bgcolor='rgba(0.0,0,0,0)',
                plot_bgcolor='rgba(0.0,0,0,0)',
                font=dict(size=12)
            )

        return kpis,descricao_componente,mapa._repr_html_(), fig_rank,fig_hist, fig_box, fig_scatter

    return atualizar
