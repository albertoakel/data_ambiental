import numpy as np
import requests
import time

# Área da cidade
lat_min = -1.2019497060905675
lat_max = -1.0615901914346855
lng_min = -48.46737737054456
lng_max = -48.33449613763752

url = "https://apisgi.mosaro.com.br/external/parqueservico/area-coleta"

# Quantidade de pontos aleatórios
N = 3500  # pode aumentar para 5000 ou 8000 se quiser

# Gerar pontos aleatórios sem repetição
lats = np.random.uniform(lat_min, lat_max, N)
lngs = np.random.uniform(lng_min, lng_max, N)

setores = {}
start_time = time.time()
processed = 0

for lat, lng in zip(lats, lngs):

    processed += 1
    percent = processed / N * 100

    print(
        f"\r🔎 Varredura: {percent:5.1f}%  | "
        f"Setores encontrados: {len(setores)}",
        end=""
    )

    params = {
        "count": 1,
        "cod_parque_servico": 164,
        "latitude": float(lat),
        "longitude": float(lng),
        "is_iframe": "true"
    }

    try:
        resp = requests.get(url, params=params, timeout=4)
        if resp.status_code != 200:
            continue

        data = resp.json()

        if "seq_area_coleta" not in data:
            continue

        setor_id = data["seq_area_coleta"]

        if setor_id not in setores:
            setores[setor_id] = data
            print(f"\n✔️ Novo setor encontrado: {data['nom_area_coleta']}")

    except:
        continue

# Fim
print("\n\n🏁 Finalizado!")
print(f"⏱ Tempo total: {time.time() - start_time:.1f} segundos")
print(f"📌 Total de setores encontrados: {len(setores)}")
# salvar arquivo final
with open("mosqueiro2.json", "w", encoding="utf-8") as f:
    json.dump(list(setores.values()), f, ensure_ascii=False, indent=2)