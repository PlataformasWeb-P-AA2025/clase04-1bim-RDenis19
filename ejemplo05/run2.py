import requests
import json

# Carga el json
with open('atp_tennis.json', 'r') as f:
    data = json.load(f)

# Nombre de la base y configuración para enviar los datos
base_datos = "personas0005"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar todos los documentos (Json) mediante docs
for doc in data['docs']:
    response = requests.post(url, headers=headers, json=doc)
    # Imprime Player_1
    print(f"Insertando {doc['Player_1']} | {response.status_code}")
