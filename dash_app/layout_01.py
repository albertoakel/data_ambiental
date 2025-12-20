
# layout_01.py
from dash import dcc, html
def criar_layout(feat_options):
    """
    Cria o layout do aplicativo Dash
    """
    return  html.Div(

    # ===== CONTAINER GERAL =====
    style={
        'background': '#eef2f7',
        'padding': '20px 30px',
        'fontFamily': 'Roboto'
    },

    children=[

        # ======================================================
        # HEADER (TÍTULO + DROPDOWN)
        # ======================================================
        html.Div(
            style={
                'display': 'grid',
                'gridTemplateColumns': '1fr 300px',
                'alignItems': 'center',
                'marginBottom': '20px'            },
            children=[

                # TÍTULO
                html.Div(
                    style={
                        'background': '#1f2933',
                        'padding': '25px 20px',
                        'borderRadius': '6px'
                    },
                    children=[
                        html.H2(
                            'Painel de Diagnóstico Ambiental Urbano',
                            style={'margin': '0', 'color': 'white'}
                        ),
                        html.P(
                            'Distribuição, ranking, dispersão e análise espacial por bairro',
                            style={'margin': '0', 'color': '#9ca3af', 'fontSize': '13px'}
                        )
                    ]
                ),
                html.Div(
                    style={
                        'justifySelf': 'end',
                        'paddingRight': '20px',
                        'width': '260px',                    },
                    children=[
                        dcc.Dropdown(
                            id='variavel',
                            options=[{'label': opt['label'], 'value': opt['value']} for opt in feat_options],
                            value=feat_options[0]['value'],
                            clearable=False,
                            className='dropdown-alto'
                        ),
                        html.Div(
                            id='descricao-variavel',
                            style={
                                'marginTop': '10px',
                                'padding': '10px',
                                'borderLeft': '3px solid #007bff',
                                'backgroundColor': '#f8f9fa',
                                'fontSize': '10px'  # Opcional: ajustar tamanho da fonte
                            }
                        )
                    ]
                )

            ]
        ),

        html.Div(
            id='kpis',
            style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(4, 1fr)',
                'gap': '15px',  # Mínimo
                'marginBottom': '10px',
                'padding': '0px',  # Remove padding interno
            }
        ),

        # ======================================================
        # MAPA + RANKING
        # ======================================================
        html.Div(
            style={
                'display': 'grid',
                'gridTemplateColumns': '3fr 1.2fr',
                'gap': '20px',
                'marginBottom': '25px'
            },
            children=[

                # MAPA
                html.Div(
                    style={
                        'background': 'white',
                        'padding': '10px',
                        'borderRadius': '8px'
                    },
                    children=[
                        html.Iframe(
                            id='mapa',
                            style={
                                'width': '100%',
                                'height': '520px',
                                'border': 'none'
                            }
                        )
                    ]
                ),

                # RANKING TOP 10
                html.Div(
                    style={
                        'background': 'None',
                        'padding': '10px',
                        'borderRadius': '8px'
                    },
                    children=[
                        dcc.Graph(
                            id='fig_rank',
                            style={'height': '520px'}
                        )
                    ]
                )
            ]
        ),

        # ======================================================
        # GRÁFICOS ANALÍTICOS (3 COLUNAS)
        # ======================================================
        html.Div(
            style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(3, 1fr)',
                'gap': '20px',
                'marginBottom': '25px'
            },
            children=[

                html.Div(
                    style={'background': 'None', 'padding': '10px', 'borderRadius': '8px'},
                    children=[dcc.Graph(id='fig_hist')]
                ),

                html.Div(
                    style={'background': 'None', 'padding': '10px', 'borderRadius': '8px'},
                    children=[dcc.Graph(id='fig_box')]
                ),

                html.Div(
                    style={'background': 'None', 'padding': '10px', 'borderRadius': '8px'},
                    children=[dcc.Graph(id='fig_scatter')]
                )
            ]
        ),

        # ======================================================
        # RODAPÉ ANALÍTICO
        # ======================================================
        html.Div(
            style={
                'background': 'white',
                'padding': '15px',
                'borderRadius': '8px'
            },
            children=[
                html.P(
                    'Estatísticas complementares, observações analíticas e notas metodológicas.',
                    style={'margin': '0', 'fontSize': '13px', 'color': '#374151'}
                )
            ]
        )

    ]
)
