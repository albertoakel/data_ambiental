import aiohttp
import asyncio
import json
import numpy as np
import time
import random

random.seed(42)

url = "https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/buscar-por-endereco-ou-posicao"

# Limites de Mosqueiro
lat_min = -1.2055736529580825
lat_max = -1.0623956432339052
lng_min = -48.45679020794048
lng_max = -48.357058421723494

# -------------------------------------
# Função assíncrona para buscar setor
# -------------------------------------
async def fetch(session, lat, lng):
    params = {
        "count": 1,
        "cod_parque_servico": 164,
        "latitude": lat,
        "longitude": lng,
        "is_iframe": "true"
    }

    try:
        async with session.get(url, params=params, timeout=6) as r:
            if r.status != 200:
                return None
            data = await r.json()

            if "seq_area_coleta" not in data:
                return None

            return data["seq_area_coleta"], data

    except:
        return None

# -------------------------------------
# Loop principal
# -------------------------------------
async def main():

    setores = {}
    total_requests = 30000
    batch_size = 30
    batches = total_requests // batch_size

    start = time.time()

    connector = aiohttp.TCPConnector(limit=40)

    async with aiohttp.ClientSession(connector=connector) as session:

        for b in range(batches):

            # Gerar lote de pontos
            lats = np.random.uniform(lat_min, lat_max, batch_size)
            lngs = np.random.uniform(lng_min, lng_max, batch_size)

            tasks = [
                fetch(session, float(lat), float(lng))
                for lat, lng in zip(lats, lngs)
            ]

            results = []
            for coro in asyncio.as_completed(tasks):
                results.append(await coro)

            novos = 0
            for result in results:
                if result:
                    setor_id, data = result
                    if setor_id not in setores:
                        setores[setor_id] = data
                        novos += 1

            await asyncio.sleep(0.15)
            elapsed = time.time() - start
            rate = (b + 1) * batch_size / elapsed

            print(
                f"\r🔎 Lote {b+1}/{batches} | "
                f"Setores encontrados: {len(setores)} | "
                f"Novos neste lote: {novos} | "
                f"Velocidade: {rate:5.1f} req/s",
                end=""
            )

        print("\n\n🏁 Finalizado!")
        print("Total de setores coletados:", len(setores))

    return setores


# -------------------------------------
# Executar
# -------------------------------------
setores = asyncio.run(main())

# -------------------------------------
# Salvamento EXATAMENTE no mesmo formato
# -------------------------------------
with open("mosqueiro.json", "w", encoding="utf-8") as f:
    json.dump(list(setores.values()), f, ensure_ascii=False, indent=2)

print("\n📁 Arquivo salvo como mosqueiro.json")
