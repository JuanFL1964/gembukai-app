import requests
import json

# Descargar exercises.json desde ExerciseDB
url = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json"
response = requests.get(url)
exercises = response.json()

print(f"✅ Descargados {len(exercises)} ejercicios")

# Traducciones manuales de los más comunes
manual_translations = {
    # Pecho
    "barbell bench press": "Press de banca con barra",
    "dumbbell bench press": "Press de banca con mancuernas",
    "incline barbell bench press": "Press de banca inclinado con barra",
    "incline dumbbell bench press": "Press de banca inclinado con mancuernas",
    "decline barbell bench press": "Press de banca declinado con barra",
    "push-up": "Flexiones",
    "cable crossover": "Cruce de poleas",
    "pec deck fly": "Aperturas en máquina",
    "chest dip": "Fondos en paralelas",
    "dumbbell fly": "Aperturas con mancuernas",
    "cable chest fly": "Cruce de poleas al pecho",
    
    # Espalda
    "pull-up": "Dominadas",
    "chin-up": "Dominadas con agarre supino",
    "lat pulldown": "Jalón al pecho",
    "barbell bent over row": "Remo con barra",
    "dumbbell row": "Remo con mancuerna",
    "seated cable row": "Remo en polea baja",
    "t-bar row": "Remo en barra T",
    "deadlift": "Peso muerto",
    "face pull": "Face Pull",
    "barbell shrug": "Encogimientos con barra",
    "dumbbell shrug": "Encogimientos con mancuernas",
    
    # Piernas
    "barbell squat": "Sentadilla con barra",
    "front squat": "Sentadilla frontal",
    "leg press": "Prensa de piernas",
    "romanian deadlift": "Peso muerto rumano",
    "lunge": "Zancadas",
    "leg extension": "Extensión de cuádriceps",
    "leg curl": "Curl femoral",
    "calf raise": "Elevación de gemelos",
    "hip thrust": "Hip Thrust",
    "goblet squat": "Sentadilla Goblet",
    
    # Hombros
    "barbell shoulder press": "Press militar con barra",
    "dumbbell shoulder press": "Press militar con mancuernas",
    "lateral raise": "Elevaciones laterales",
    "front raise": "Elevaciones frontales",
    "upright row": "Remo al mentón",
    "arnold press": "Press Arnold",
    
    # Brazos
    "barbell curl": "Curl de bíceps con barra",
    "dumbbell curl": "Curl de bíceps con mancuernas",
    "hammer curl": "Curl martillo",
    "tricep pushdown": "Extensión de tríceps en polea",
    "tricep dip": "Fondos de tríceps",
    "preacher curl": "Curl predicador",
    "concentration curl": "Curl concentrado",
    
    # Core
    "plank": "Plancha",
    "crunch": "Crunch abdominal",
    "leg raise": "Elevación de piernas",
    "russian twist": "Giro ruso",
    "cable crunch": "Crunch en polea",
    "mountain climber": "Escalador",
    
    # Cardio
    "running": "Correr",
    "cycling": "Ciclismo",
    "jump rope": "Saltar a la cuerda",
    "burpee": "Burpee",
    "jumping jacks": "Saltos de tijera",
}

# Generar translations.json
translations = {
    "exercises": {},
    "muscles": {
        "chest": "Pecho",
        "back": "Espalda",
        "shoulders": "Hombros",
        "upper arms": "Brazos",
        "upper legs": "Piernas",
        "lower legs": "Pantorrillas",
        "waist": "Core",
        "cardio": "Cardio"
    },
    "equipment": {
        "barbell": "Barra",
        "dumbbell": "Mancuernas",
        "cable": "Polea",
        "machine": "Máquina",
        "body weight": "Peso corporal",
        "kettlebell": "Pesa rusa",
        "band": "Banda elástica"
    }
}

# Añadir traducciones manuales
translations["exercises"].update(manual_translations)

# Para los que no tengan traducción, usar el nombre original
for ex in exercises:
    name = ex['name'].lower()
    if name not in translations["exercises"]:
        translations["exercises"][name] = ex['name']

# Guardar
with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, indent=2, ensure_ascii=False)

print("✅ translations.json generado correctamente")
print(f"📊 Total traducciones: {len(translations['exercises'])}")