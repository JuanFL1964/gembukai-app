import requests
import json
import time

# Descargar exercises.json desde ExerciseDB
url = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json"
response = requests.get(url)
exercises = response.json()

print(f"✅ Descargados {len(exercises)} ejercicios")

# Traducciones manuales de los más comunes (mejor calidad)
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
    "archer push up": "Flexiones de arquero",
    "assisted chest dip (kneeling)": "Fondos de pecho asistidos (de rodillas)",
    "assisted wide-grip chest dip (kneeling)": "Fondos de pecho agarre ancho asistidos (de rodillas)",
    "band bench press": "Press de banca con banda",
    "barbell incline bench press": "Press de banca inclinado con barra",
    "close-grip barbell bench press": "Press de banca agarre cerrado con barra",
    "decline push-up": "Flexiones declinadas",
    "dumbbell incline bench press": "Press de banca inclinado con mancuernas",
    "incline push-up": "Flexiones inclinadas",
    "machine chest press": "Press de pecho en máquina",
    "smith machine bench press": "Press de banca en máquina Smith",
    "wide-grip chest dip": "Fondos de pecho agarre ancho",
    
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
    "wide-grip pull-up": "Dominadas agarre ancho",
    "close-grip pull-up": "Dominadas agarre cerrado",
    "assisted pull-up": "Dominadas asistidas",
    "assisted chin-up": "Dominadas supinas asistidas",
    "one arm dumbbell row": "Remo con mancuerna a una mano",
    "pendlay row": "Remo Pendlay",
    "hyperextension": "Hiperextensiones lumbares",
    "romanian deadlift": "Peso muerto rumano",
    "sumo deadlift": "Peso muerto sumo",
    "rack pull": "Rack Pull",
    "dumbbell pullover": "Pull over con mancuerna",
    "barbell pullover": "Pull over con barra",
    
    # Piernas
    "barbell squat": "Sentadilla con barra",
    "front squat": "Sentadilla frontal",
    "leg press": "Prensa de piernas",
    "lunge": "Zancadas",
    "leg extension": "Extensión de cuádriceps",
    "leg curl": "Curl femoral",
    "calf raise": "Elevación de gemelos",
    "hip thrust": "Hip Thrust",
    "goblet squat": "Sentadilla Goblet",
    "barbell deadlift": "Peso muerto con barra",
    "bulgarian split squat": "Sentadilla búlgara",
    "walking lunge": "Zancadas caminando",
    "step-up": "Step-Up",
    "lying leg curl": "Curl femoral tumbado",
    "seated leg curl": "Curl femoral sentado",
    "standing leg curl": "Curl femoral de pie",
    "hip abduction": "Abducción de cadera",
    "hip adduction": "Aducción de cadera",
    "cable kickback": "Patada de glúteo en polea",
    "machine calf raise": "Elevación de gemelos en máquina",
    "seated calf raise": "Elevación de gemelos sentado",
    "leg press calf raise": "Gemelos en prensa",
    "barbell calf raise": "Elevación de gemelos con barra",
    "single leg calf raise": "Elevación de gemelos a una pierna",
    "good morning": "Buenos días",
    "cable pull through": "Pull Through en polea",
    "single leg deadlift": "Peso muerto a una pierna",
    "lateral lunge": "Desplante lateral",
    "hack squat": "Sentadilla Hack",
    "sled 45° leg press": "Prensa de piernas a 45°",
    "lever alternate leg press": "Prensa de piernas alternada",
    
    # Hombros
    "barbell shoulder press": "Press militar con barra",
    "dumbbell shoulder press": "Press militar con mancuernas",
    "lateral raise": "Elevaciones laterales",
    "front raise": "Elevaciones frontales",
    "upright row": "Remo al mentón",
    "arnold press": "Press Arnold",
    "rear delt fly": "Elevaciones posteriores",
    "barbell upright row": "Remo al mentón con barra",
    "cable lateral raise": "Elevaciones laterales en polea",
    "dumbbell lateral raise": "Elevaciones laterales con mancuernas",
    "dumbbell front raise": "Elevaciones frontales con mancuernas",
    "machine shoulder press": "Press de hombros en máquina",
    "smith machine shoulder press": "Press de hombros en máquina Smith",
    
    # Brazos
    "barbell curl": "Curl de bíceps con barra",
    "dumbbell curl": "Curl de bíceps con mancuernas",
    "hammer curl": "Curl martillo",
    "tricep pushdown": "Extensión de tríceps en polea",
    "tricep dip": "Fondos de tríceps",
    "preacher curl": "Curl predicador",
    "concentration curl": "Curl concentrado",
    "barbell curl (reverse grip)": "Curl inverso con barra",
    "cable curl": "Curl en polea",
    "dumbbell hammer curl": "Curl martillo con mancuernas",
    "ez bar curl": "Curl con barra Z",
    "tricep extension": "Extensión de tríceps",
    "overhead tricep extension": "Extensión de tríceps por encima de la cabeza",
    "skull crusher": "Rompecráneos",
    "close-grip bench press": "Press de banca agarre cerrado",
    "dips": "Fondos",
    "wrist curl": "Curl de muñeca",
    "reverse wrist curl": "Curl inverso de muñeca",
    
    # Core
    "plank": "Plancha",
    "crunch": "Crunch abdominal",
    "leg raise": "Elevación de piernas",
    "russian twist": "Giro ruso",
    "cable crunch": "Crunch en polea",
    "mountain climber": "Escalador",
    "bicycle crunch": "Crunch bicicleta",
    "side plank": "Plancha lateral",
    "hanging leg raise": "Elevación de piernas colgado",
    "ab wheel rollout": "Rueda abdominal",
    "decline crunch": "Crunch declinado",
    "flutter kicks": "Patadas de aleta",
    "reverse crunch": "Crunch inverso",
    "sit-up": "Abdominales",
    "v-up": "V-Up",
    "woodchop": "Leñador",
    
    # Cardio
    "running": "Correr",
    "cycling": "Ciclismo",
    "jump rope": "Saltar a la cuerda",
    "burpee": "Burpee",
    "jumping jacks": "Saltos de tijera",
    "rowing": "Remo",
    "elliptical trainer": "Elíptica",
    "stair climber": "Escaladora",
    "treadmill": "Cinta de correr",
    "stationary bike": "Bicicleta estática",
}

# Función para traducir usando MyMemory API (gratuita, sin API key)
def translate_text(text):
    try:
        url = f"https://api.mymemory.translated.net/get?q={requests.utils.quote(text)}&langpair=en|es"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('responseStatus') == 200:
            return data['responseData']['translatedText']
    except:
        pass
    return text  # Si falla, devolver el original

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
        "band": "Banda elástica",
        "leverage machine": "Máquina de palanca",
        "assisted": "Asistido",
        "smith machine": "Máquina Smith",
        "sled machine": "Máquina de trineo",
        "ez barbell": "Barra Z",
        "trap bar": "Barra trapecio",
        "olympic barbell": "Barra olímpica",
        "bosu ball": "Bosu",
        "medicine ball": "Balón medicinal",
        "stability ball": "Balón de estabilidad",
        "roller": "Rodillo",
        "wheel roller": "Rueda abdominal",
        "rope": "Cuerda"
    }
}

# Añadir traducciones manuales primero
translations["exercises"].update(manual_translations)

# Traducir automáticamente los que no tienen traducción manual
print("🔄 Traduciendo ejercicios automáticamente con MyMemory API...")
count = 0
total = len([ex for ex in exercises if ex['name'].lower() not in translations["exercises"]])
print(f"   Faltan por traducir: {total} ejercicios")

for ex in exercises:
    name = ex['name'].lower()
    if name not in translations["exercises"]:
        translated = translate_text(ex['name'])
        translations["exercises"][name] = translated
        count += 1
        if count % 50 == 0:
            print(f"   ✅ Traducidos {count}/{total} ejercicios...")
            time.sleep(1)  # Pausa para no saturar la API
        else:
            time.sleep(0.3)  # Pequeña pausa entre peticiones

print(f"✅ Traducidos {count} ejercicios automáticamente")

# Guardar
with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, indent=2, ensure_ascii=False)

print("✅ translations.json generado correctamente")
print(f"📊 Total traducciones: {len(translations['exercises'])}")