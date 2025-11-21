import requests
import json
from urllib.parse import urlencode

url = "https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/buscar-por-endereco-ou-posicao"

# coordenadas que você citou
lat = -1.4467652
lng = -48.4614097

# combinações para testar
testes = [
    {"lat": lat, "lng": lng},
    {"lat": str(lat), "lng": str(lng)},
    {"latitude": lat, "longitude": lng},
    {"latitude": str(lat), "longitude": str(lng)},
    {"lat": lat, "lng": lng, "count": 1, "cod_parque_servico": 164},
    {"lat": lat, "lng": lng, "is_iframe": "true"},
    {"lat": lat, "lng": lng, "count": 1, "is_iframe": "true"},
]

resultados = []

print("\n====== INICIANDO VARREDURA ======\n")

for i, params in enumerate(testes, 1):

    # parâmetros obrigatórios **suspeitos**
    params_base = {
        "count": 1,
        "cod_parque_servico": 164,
        "is_iframe": "true"
    }

    params_final = params_base.copy()
    params_final.update(params)

    print(f"\n---- Tentativa {i} ----")
    print("Parâmetros:", params_final)
    print("URL:", url + "?" + urlencode(params_final))

    try:
        resp = requests.get(url, params=params_final, timeout=10)
        status = resp.status_code

        try:
            data = resp.json()
        except:
            data = resp.text

        # Exibir só o começo por segurança
        print("Status HTTP:", status)
        print("Resposta:", str(data)[:200], "...\n")

        resultados.append({
            "tentativa": i,
            "params": params_final,
            "status": status,
            "response": data
        })

    except Exception as e:
        print("Erro:", e)
        resultados.append({
            "tentativa": i,
            "params": params_final,
            "erro": str(e)
        })

# Salva resultados
with open("resultados_teste.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print("\n======= FIM DA VARREDURA =======\n")
print("Arquivo salvo como resultados_teste.json")
