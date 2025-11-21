import requests
import json
import time
import math
import random
import numpy as np


url = "https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/buscar-por-endereco-ou-posicao"


lat_min = -1.2019497060905675 # UFPA (mais ao sul)
lat_max = -1.0615901914346855  # ceasa (mais ao norte)
lng_min = -48.46737737054456 # Veropa (mais a oeste)
lng_max = -48.33449613763752 # Abacatal (mais a leste)

-1.1708387623533947, -48.45679020794048

random.seed(42)

lats = np.round(np.random.uniform(lat_min, lat_max, 50), 6)
lngs = np.round(np.random.uniform(lng_min, lng_max, 50), 6)

total_points = len(lats) * len(lngs)
processed = 0
start_time = time.time()

setores = {}

for lat in lats:
    for lng in lngs:

        processed += 1
        percent = (processed / total_points) * 100

        elapsed = time.time() - start_time
        rate = processed / elapsed
        remaining = (total_points - processed) / rate if rate > 0 else 0

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
            "is_iframe": "true"
        }

        try:
            resp = requests.get(url, params=params, timeout=8)
            if resp.status_code != 200:
                continue

            data = resp.json()

            if "seq_area_coleta" not in data:
                continue

            setor_id = data["seq_area_coleta"]

            if setor_id not in setores:
                setores[setor_id] = data
                print(f"\n✔️ Novo setor encontrado: {data['nom_area_coleta']}")

        except Exception:
            continue

        time.sleep(0.15)

print(f"\n\n🏁 Varredura concluída! Total de setores coletados: {len(setores)}")


# salvar arquivo final
with open("mosqueiro.json", "w", encoding="utf-8") as f:
    json.dump(list(setores.values()), f, ensure_ascii=False, indent=2)

