import requests

url = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json"
response = requests.get(url)
exercises = response.json()

print(f"Total ejercicios: {len(exercises)}")
print("\nPrimeros 50 nombres en minúsculas:")
for i, ex in enumerate(exercises[:50]):
    nombre = ex['name'].lower()
    print(f"{i+1}. '{nombre}'")

print("\n\nBuscando 'barbell bench press' en diferentes formatos:")
for ex in exercises:
    nombre = ex['name'].lower()
    if 'barbell' in nombre and 'bench' in nombre and 'press' in nombre:
        print(f"  -> '{nombre}'")