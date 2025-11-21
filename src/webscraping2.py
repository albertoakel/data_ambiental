"""
Script para varredura geoespacial de setores de coleta em Belém-PA.

Este código gera uma grade de coordenadas aleatórias dentro de limites
pré-definidos (latitude e longitude) e consulta a API de áreas de coleta
do Mosaro para cada ponto. Ele identifica setores únicos, evita duplicatas
e armazena os resultados em um arquivo JSON chamado "mosqueiro.json".

Funcionalidades principais:
- Geração de pontos aleatórios dentro de uma área geográfica.
- Consulta à API de setores de coleta por coordenada.
- Registro de setores únicos encontrados.
- Estimativa de progresso e tempo restante durante a varredura.
- Salvamento do resultado final em formato JSON.
"""
import requests
import json
import time
import random
import numpy as np

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

# Semente para reproduzibilidade
random.seed(42)

# Gera 50 valores aleatórios de latitudes e longitudes dentro dos limites
lats = np.round(np.random.uniform(LAT_MIN, LAT_MAX, 50), 6)
lngs = np.round(np.random.uniform(LNG_MIN, LNG_MAX, 50), 6)

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

        # Status da varredura
        print(
            f"\r🔍 Varredura: {percent:5.1f}%  | "
            f"Ponto: ({lat}, {lng})  | "
            f"Setores coletados: {len(setores)}  | "
            f"Restante: {remaining/60:5.1f} min",
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
            continue

        # Pequena pausa para não sobrecarregar a API
        time.sleep(0.15)

print(
    f"\n\n🏁 Varredura concluída! Total de setores coletados: {len(setores)}"
)

# Salva os setores encontrados em arquivo JSON
with open("mosqueiro.json", "w", encoding="utf-8") as f:
    json.dump(list(setores.values()), f, ensure_ascii=False, indent=2)
