import json

print("📖 Leyendo exercises.txt...")
with open('exercises.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"✅ Encontrados {len(data)} ejercicios")
print("🔄 Filtrando solo instrucciones en español...")

spanish_exercises = []

for exercise in data:
    spanish_exercise = {
        'id': exercise.get('id'),
        'name': exercise.get('name'),
        'category': exercise.get('category'),
        'body_part': exercise.get('body_part'),
        'equipment': exercise.get('equipment'),
        'instructions': exercise.get('instructions', {}).get('es', ''),
        'instruction_steps': exercise.get('instruction_steps', {}).get('es', []),
        'muscle_group': exercise.get('muscle_group'),
        'secondary_muscles': exercise.get('secondary_muscles'),
        'target': exercise.get('target'),
        'image': exercise.get('image'),
        'gif_url': exercise.get('gif_url'),
        'media_id': exercise.get('media_id')
    }
    spanish_exercises.append(spanish_exercise)

print(f"✅ Procesados {len(spanish_exercises)} ejercicios en español")
print("💾 Guardando exercises_spanish.json...")

with open('exercises_spanish.json', 'w', encoding='utf-8') as f:
    json.dump(spanish_exercises, f, ensure_ascii=False, indent=2)

print("\n✅ ¡Listo!")
print(f"📁 Archivo guardado en: exercises_spanish.json")
print(f"📊 Total: {len(spanish_exercises)} ejercicios")

# Mostrar estadísticas por grupo muscular
from collections import Counter
grupos = Counter(ex['body_part'] for ex in spanish_exercises)
print("\n📋 Ejercicios por grupo muscular:")
for grupo, cantidad in sorted(grupos.items()):
    print(f"  • {grupo}: {cantidad}")