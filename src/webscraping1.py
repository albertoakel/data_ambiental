"""
Script para varredura sistemática de setores de coleta em Belém-PA.

O código gera uma grade de coordenadas dentro de limites geográficos
pré-definidos (latitude e longitude) com passo aproximado de 250 metros.
Para cada ponto, consulta a API de áreas de coleta do Mosaro e registra
os setores únicos encontrados.

Funcionalidades principais:
- Geração de pontos em grade regular na área definida.
- Consulta à API de setores de coleta por coordenada.
- Registro de setores únicos, evitando duplicações.
- Estimativa de progresso e tempo restante durante a varredura.
- Salvamento do resultado final em arquivo JSON com timestamp.
"""

import requests
import json
import time
import math
from datetime import datetime

# Endpoint da API que retorna a área de coleta para um ponto (lat, lng)
URL = (
    "https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/"
    "buscar-por-endereco-ou-posicao"
)

# Limites aproximados de latitude e longitude para varredura
LAT_MIN = -1.2019497060905675  # UFPA (sul)
LAT_MAX = -1.0615901914346855  # CEASA (norte)
LNG_MIN = -48.46737737054456   # Ver-o-Peso (oeste)
LNG_MAX = -48.33449613763752   # Abacatal (leste)

# Definição de passo da grade (~250 metros)
LAT_CENTER = (LAT_MIN + LAT_MAX) / 2
LAT_DEGREE_KM = 111.0
LNG_DEGREE_KM = 111.0 * math.cos(math.radians(abs(LAT_CENTER)))

DELTA_KM = 0.250
STEP_LAT = DELTA_KM / LAT_DEGREE_KM
STEP_LNG = DELTA_KM / LNG_DEGREE_KM

# Gerar listas de latitudes e longitudes da grade
lats = [
    round(LAT_MIN + i * STEP_LAT, 6)
    for i in range(int((LAT_MAX - LAT_MIN) / STEP_LAT))
]
lngs = [
    round(LNG_MIN + i * STEP_LNG, 6)
    for i in range(int((LNG_MAX - LNG_MIN) / STEP_LNG))
]

# Inicializa contadores e tempo
total_points = len(lats) * len(lngs)
processed = 0
start_time = time.time()

# Dicionário para armazenar setores únicos encontrados
setores = {}

# Loop principal percorrendo todas as coordenadas geradas
for lat in lats:
    for lng in lngs:
        processed += 1
        percent = (processed / total_points) * 100

        # Estimativa de tempo restante
        elapsed = time.time() - start_time
        rate = processed / elapsed
        remaining = (total_points - processed) / rate if rate > 0 else 0

        # Exibe status da varredura
        print(
            f"\r🔍 Varredura: {percent:5.1f}%  | "
            f"Ponto: ({lat}, {lng})  | "
            f"Setores coletados: {len(setores)}  | "
            f"Restante: {remaining / 60:5.1f} min",
            end=""
        )

        params = {
            "count": 1,
            "cod_parque_servico": 164,
            "latitude": lat,
            "longitude": lng,
            "is_iframe": "true",
        }

        try:
            resp = requests.get(URL, params=params, timeout=8)
            if resp.status_code != 200:
                continue

            data = resp.json()
            if "seq_area_coleta" not in data:
                continue

            setor_id = data["seq_area_coleta"]

            # Armazena apenas setores novos
            if setor_id not in setores:
                setores[setor_id] = data
                print(f"\n✔️ Novo setor encontrado: {data['nom_area_coleta']}")

        except Exception:
            # Ignora erros de conexão ou parsing
            continue

        # Pequena pausa para não sobrecarregar a API
        time.sleep(0.15)

# Finalização da varredura
print(
    f"\n\n🏁 Varredura concluída! Total de setores coletados: {len(setores)}"
)

# Salva os setores encontrados em arquivo JSON com timestamp
hora_minuto = datetime.now().strftime("%H_%M")
filename = f"setores_{hora_minuto}.jsonl"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(list(setores.values()), f, ensure_ascii=False, indent=2)
