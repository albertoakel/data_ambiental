"""
Script de consulta à API de setores de coleta do Mosaro para um ponto específico.

Este código realiza uma requisição HTTP para obter os dados de coleta de um
setor urbano em Belém-PA, usando latitude e longitude de referência.
Os dados retornados são salvos em um arquivo JSON para posterior análise.

Funcionalidades principais:
- Consulta à API de setores de coleta por coordenada.
- Armazenamento do resultado em arquivo JSON formatado.
- Possibilidade de registro de metadados como dias e turno de coleta.
"""

import requests
import json

# Endpoint da API que retorna a área de coleta para um ponto (lat, lng)
URL = (
    "https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/"
    "buscar-por-endereco-ou-posicao"
)

# Coordenadas de referência para consulta
# Endereço: Avenida João Paulo II, 166
# Setor: 1416
# Dias de coleta: Seg, Ter, Qua, Qui, Sex, Sáb
# Turno de coleta: Noturno (a partir das 18:00)
LAT = -1.4467652
LNG = -48.4614097

# Parâmetros da requisição
params = {
    "count": 1,
    "cod_parque_servico": 164,
    "latitude": LAT,
    "longitude": LNG,
    "is_iframe": "true",
}

# Realiza a requisição GET à API
resp = requests.get(URL, params=params)

# Converte a resposta JSON em dicionário Python
data = resp.json()

# Salva os dados retornados em arquivo JSON formatado
with open("AA_teste_coleta.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
