import requests
import sys

# Forzar codificación UTF-8 para la salida
sys.stdout.reconfigure(encoding='utf-8')

url = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json"
response = requests.get(url)
exercises = response.json()

print(f"Total ejercicios en el archivo: {len(exercises)}\n")

# Mostrar todos los nombres en minúsculas
for i, ex in enumerate(exercises, 1):
    nombre = ex['name'].lower()
    print(f"{i}. {nombre}")