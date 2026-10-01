import requests
import json

url = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json"
response = requests.get(url)
exercises = response.json()

# Cargar traducciones actuales
with open("translations.json", "r", encoding="utf-8") as f:
    traducciones = json.load(f)

print(f"Total ejercicios: {len(exercises)}")
print(f"Total traducciones: {len(traducciones['exercises'])}")

# Buscar ejercicios que están en inglés (nombre original = traducción)
faltantes = []
for ex in exercises:
    nombre = ex['name'].lower()
    if nombre in traducciones["exercises"]:
        traduccion = traducciones["exercises"][nombre]
        # Si la traducción es igual al nombre original, está en inglés
        if traduccion.lower() == nombre or traduccion == ex['name']:
            faltantes.append(ex['name'])

print(f"\nEjercicios sin traducir: {len(faltantes)}\n")
for i, nombre in enumerate(faltantes, 1):
    print(f"{i}. {nombre}")

# Guardar en archivo
with open("faltantes.txt", "w", encoding="utf-8") as f:
    for nombre in faltantes:
        f.write(f"{nombre}\n")

print(f"\nLista guardada en 'faltantes.txt'")