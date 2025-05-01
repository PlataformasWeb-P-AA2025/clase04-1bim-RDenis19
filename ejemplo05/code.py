import csv
import json

# Abre el CSV en modo lectura con encoding que evite errores
csv_file = open("atp_tennis.csv", encoding="latin-1", newline="")
reader = csv.DictReader(csv_file)

# Construye la lista de documentos que debe imprimir
docs = []
for fila in reader:
    docs.append(fila)

csv_file.close()

# Vuelca al JSON con la estructura que quieres
json_file = open("atp_tennis.json", "w", encoding="utf-8")
json.dump({"docs": docs}, json_file, ensure_ascii=False, indent=4)
json_file.close()

print("Creado")
