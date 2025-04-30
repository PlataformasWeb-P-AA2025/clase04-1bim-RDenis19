import requests
import json

# Carga el JSON generado
with open('atp_tennis.json', 'r') as f:
    data = json.load(f)

# Nombre de la base CouchDB
base_datos = "personas0005"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar todos los documentos
for doc in data['docs']:
    response = requests.post(url, headers=headers, json=doc)
    # Imprime Player_1 en lugar de 'nombre'
    print(f"Insertando {doc['Player_1']} | {response.status_code}")
