import requests
import json

print("=== CREANDO TRADUCCIONES CON NOMBRES REALES ===")

url = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json"
response = requests.get(url)
exercises = response.json()
print(f"Descargados {len(exercises)} ejercicios")

# Diccionario con traducciones basadas en los nombres REALES del archivo
TRADUCCIONES = {
    # ===== PECHO - Barra =====
    "barbell bench press": "Press de banca con barra",
    "barbell decline bench press": "Press de banca declinado con barra",
    "barbell incline bench press": "Press de banca inclinado con barra",
    "barbell wide bench press": "Press de banca agarre ancho con barra",
    "barbell close-grip bench press": "Press de banca agarre cerrado con barra",
    "barbell reverse grip decline bench press": "Press de banca agarre inverso declinado con barra",
    "barbell reverse grip incline bench press": "Press de banca agarre inverso inclinado con barra",
    "barbell guillotine bench press": "Press de banca guillotina con barra",
    "barbell jm bench press": "Press JM con barra",
    "barbell wide reverse grip bench press": "Press de banca agarre inverso ancho con barra",
    "barbell decline pullover": "Pullover con barra en banco declinado",
    "barbell decline wide-grip press": "Press declinado agarre ancho con barra",
    "barbell front raise and pullover": "Elevacion frontal y pullover con barra",
    "barbell pullover": "Pullover con barra",
    "barbell bent arm pullover": "Pullover con barra",
    "barbell incline reverse-grip press": "Press inclinado agarre inverso con barra",
    
    # ===== PECHO - Mancuernas =====
    "dumbbell bench press": "Press de banca con mancuernas",
    "dumbbell decline bench press": "Press de banca declinado con mancuernas",
    "dumbbell incline bench press": "Press de banca inclinado con mancuernas",
    "dumbbell fly": "Aperturas con mancuernas",
    "dumbbell decline fly": "Aperturas declinadas con mancuernas",
    "dumbbell incline fly": "Aperturas inclinadas con mancuernas",
    "dumbbell pullover": "Pullover con mancuerna",
    "dumbbell tate press": "Press Tate con mancuernas",
    "dumbbell floor press": "Press en suelo con mancuernas",
    
    # ===== PECHO - Cable/Polea =====
    "cable bench press": "Press de banca en polea",
    "cable crossover": "Cruce de poleas",
    "cable chest fly": "Cruce de poleas al pecho",
    "cable decline fly": "Cruce de poleas declinado",
    "cable incline fly": "Cruce de poleas inclinado",
    "cable low fly": "Cruce de poleas bajo",
    "cable middle fly": "Cruce de poleas medio",
    "cable upper chest crossovers": "Cruce de poleas pecho superior",
    "cable cross-over variation": "Variacion de cruce de poleas",
    "cable chest press": "Press de pecho en polea",
    "cable seated chest press": "Press de pecho sentado en polea",
    "cable standing chest press": "Press de pecho de pie en polea",
    "cable incline chest press": "Press de pecho inclinado en polea",
    "cable decline chest press": "Press de pecho declinado en polea",
    "cable one arm chest press": "Press de pecho a una mano en polea",
    "cable pullover": "Pullover en polea",
    
    # ===== PECHO - Máquina =====
    "machine chest press": "Press de pecho en maquina",
    "machine decline chest press": "Press de pecho declinado en maquina",
    "machine incline chest press": "Press de pecho inclinado en maquina",
    "lever chest press": "Press de pecho en maquina de palanca",
    "lever decline chest press": "Press de pecho declinado en maquina de palanca",
    "lever incline chest press": "Press de pecho inclinado en maquina de palanca",
    "pec deck fly": "Aperturas en maquina pec-deck",
    
    # ===== PECHO - Smith Machine =====
    "smith machine bench press": "Press de banca en maquina Smith",
    "smith machine decline bench press": "Press de banca declinado en maquina Smith",
    "smith machine incline bench press": "Press de banca inclinado en maquina Smith",
    
    # ===== PECHO - Banda =====
    "band bench press": "Press de banca con banda",
    "band fly": "Aperturas con banda",
    "band decline fly": "Aperturas declinadas con banda",
    "band incline fly": "Aperturas inclinadas con banda",
    "band crossover": "Cruce con banda",
    "band pullover": "Pullover con banda",
    "band one arm twisting chest press": "Press de pecho con giro a una mano con banda",
    "band twisting chest press": "Press de pecho con giro con banda",
    
    # ===== PECHO - Flexiones =====
    "push-up": "Flexiones",
    "archer push up": "Flexiones de arquero",
    "clap push up": "Flexiones con aplauso",
    "close-grip push-up": "Flexiones agarre cerrado",
    "decline push-up": "Flexiones declinadas",
    "diamond push-up": "Flexiones diamante",
    "explosive push-up": "Flexiones explosivas",
    "incline push-up": "Flexiones inclinadas",
    "one arm push-up": "Flexiones a una mano",
    "plyo push up": "Flexiones pliometricas",
    "wide-grip push-up": "Flexiones agarre ancho",
    "clock push-up": "Flexiones reloj",
    
    # ===== PECHO - Fondos =====
    "chest dip": "Fondos de pecho",
    "assisted chest dip (kneeling)": "Fondos de pecho asistidos (de rodillas)",
    "assisted wide-grip chest dip (kneeling)": "Fondos de pecho agarre ancho asistidos (de rodillas)",
    
    # ===== PECHO - Estiramientos =====
    "assisted seated pectoralis major stretch with stability ball": "Estiramiento de pecho asistido con balon",
    "behind head chest stretch": "Estiramiento de pecho detras de la cabeza",
    "standing chest stretch": "Estiramiento de pecho de pie",
    
    # ===== PECHO - Otros =====
    "svend press": "Press Svend",
    "landmine press": "Press landmine",
    
    # ===== ESPALDA =====
    "pull-up": "Dominadas",
    "assisted pull-up": "Dominadas asistidas",
    "chin-up": "Dominadas agarre supino",
    "assisted chin-up": "Dominadas agarre supino asistidas",
    "wide grip pull-up": "Dominadas agarre ancho",
    "close grip pull-up": "Dominadas agarre cerrado",
    "lat pulldown": "Jalon al pecho",
    "barbell bent over row": "Remo con barra",
    "barbell pendlay row": "Remo Pendlay con barra",
    "dumbbell row": "Remo con mancuerna",
    "dumbbell bent over row": "Remo con mancuerna inclinado",
    "one arm dumbbell row": "Remo con mancuerna a una mano",
    "seated cable row": "Remo en polea sentado",
    "deadlift": "Peso muerto",
    "barbell deadlift": "Peso muerto con barra",
    "romanian deadlift": "Peso muerto rumano",
    "sumo deadlift": "Peso muerto sumo",
    "barbell shrug": "Encogimientos con barra",
    "dumbbell shrug": "Encogimientos con mancuernas",
    "hyperextension": "Hiperextensiones lumbares",
    "good morning": "Buenos dias",
    "face pull": "Face pull",
    
    # ===== PIERNAS =====
    "barbell squat": "Sentadilla con barra",
    "front squat": "Sentadilla frontal",
    "barbell front squat": "Sentadilla frontal con barra",
    "barbell high bar squat": "Sentadilla con barra alta",
    "barbell low bar squat": "Sentadilla con barra baja",
    "goblet squat": "Sentadilla goblet",
    "hack squat": "Sentadilla hack",
    "leg press": "Prensa de piernas",
    "sled 45° leg press": "Prensa de piernas a 45 grados",
    "barbell lunge": "Zancadas con barra",
    "dumbbell lunge": "Zancadas con mancuernas",
    "walking lunge": "Zancadas caminando",
    "reverse lunge": "Zancada hacia atras",
    "lateral lunge": "Zancada lateral",
    "bulgarian split squat": "Sentadilla bulgara",
    "step-up": "Step-up",
    "leg extension": "Extensiones de cuadriceps",
    "lying leg curl": "Curl femoral tumbado",
    "seated leg curl": "Curl femoral sentado",
    "standing leg curl": "Curl femoral de pie",
    "barbell hip thrust": "Hip thrust con barra",
    "glute bridge": "Puente de gluteos",
    "calf raise": "Elevacion de gemelos",
    "barbell calf raise": "Elevacion de gemelos con barra",
    "seated calf raise": "Elevacion de gemelos sentado",
    "donkey calf raise": "Elevacion de gemelos tipo burro",
    "hip abduction": "Abduccion de cadera",
    "hip adduction": "Aduccion de cadera",
    
    # ===== HOMBROS =====
    "barbell shoulder press": "Press militar con barra",
    "dumbbell shoulder press": "Press militar con mancuernas",
    "arnold press": "Press Arnold",
    "lateral raise": "Elevaciones laterales",
    "dumbbell lateral raise": "Elevaciones laterales con mancuernas",
    "cable lateral raise": "Elevaciones laterales en polea",
    "front raise": "Elevaciones frontales",
    "barbell front raise": "Elevaciones frontales con barra",
    "dumbbell front raise": "Elevaciones frontales con mancuernas",
    "rear delt fly": "Pajaros (deltoides posterior)",
    "dumbbell rear delt fly": "Pajaros con mancuernas",
    "cable rear delt fly": "Pajaros en polea",
    "upright row": "Remo al menton",
    "barbell upright row": "Remo al menton con barra",
    "dumbbell upright row": "Remo al menton con mancuernas",
    
    # ===== BRAZOS - Bíceps =====
    "barbell curl": "Curl de biceps con barra",
    "dumbbell curl": "Curl de biceps con mancuernas",
    "ez barbell curl": "Curl con barra Z",
    "hammer curl": "Curl martillo",
    "dumbbell hammer curl": "Curl martillo con mancuernas",
    "cable hammer curl (with rope)": "Curl martillo en polea con cuerda",
    "preacher curl": "Curl predicador",
    "barbell preacher curl": "Curl predicador con barra",
    "dumbbell preacher curl": "Curl predicador con mancuernas",
    "cable preacher curl": "Curl predicador en polea",
    "concentration curl": "Curl concentrado",
    "cable curl": "Curl en polea",
    "incline dumbbell curl": "Curl inclinado con mancuernas",
    "spider curl": "Curl arana",
    "reverse barbell curl": "Curl inverso con barra",
    "reverse dumbbell curl": "Curl inverso con mancuernas",
    "wrist curl": "Curl de muneca",
    "reverse wrist curl": "Curl inverso de muneca",
    
    # ===== BRAZOS - Tríceps =====
    "tricep pushdown": "Extension de triceps en polea",
    "rope pushdown": "Extension de triceps con cuerda",
    "overhead tricep extension": "Extension de triceps sobre la cabeza",
    "cable overhead tricep extension": "Extension de triceps sobre la cabeza en polea",
    "skull crusher": "Rompecranos",
    "lying tricep extension": "Extension de triceps tumbado",
    "tricep dip": "Fondos de triceps",
    "close-grip bench press": "Press de banca agarre cerrado",
    
    # ===== CORE =====
    "plank": "Plancha",
    "side plank": "Plancha lateral",
    "crunch": "Crunch abdominal",
    "decline crunch": "Crunch declinado",
    "cable crunch": "Crunch en polea",
    "reverse crunch": "Crunch inverso",
    "leg raise": "Elevacion de piernas",
    "hanging leg raise": "Elevacion de piernas colgado",
    "russian twist": "Giros rusos",
    "bicycle crunch": "Crunch bicicleta",
    "mountain climber": "Escalador",
    "ab wheel rollout": "Rueda abdominal",
    "sit-up": "Abdominales",
    "3/4 sit-up": "Abdominales 3/4",
    "v-up": "V-up",
    "flutter kicks": "Patadas de aleta",
    "woodchop": "Lenador",
    "cable woodchop": "Lenador en polea",
    
    # ===== CARDIO =====
    "burpee": "Burpee",
    "running": "Correr",
    "cycling": "Ciclismo",
    "jump rope": "Saltar a la cuerda",
    "jumping jacks": "Saltos de tijera",
    "rowing": "Remo",
    "treadmill": "Cinta de correr",
    "stationary bike": "Bicicleta estatica",
    "box jump": "Salto al cajon",
    "battle ropes": "Cuerdas de batalla",
    "kettlebell swing": "Swing con pesa rusa",
    "high knees": "Rodillas al pecho",
    "butt kicks": "Talones al gluteo",
    "squat jump": "Sentadilla con salto",
    "lateral jump": "Salto lateral",
    "power clean": "Cargada de potencia",
}

# Construir traducciones
traducciones = {
    "exercises": {},
    "muscles": {
        "chest": "Pecho",
        "back": "Espalda",
        "shoulders": "Hombros",
        "upper arms": "Brazos",
        "upper legs": "Piernas",
        "lower legs": "Pantorrillas",
        "waist": "Core",
        "cardio": "Cardio",
        "neck": "Cuello",
        "lower arms": "Antebrazos",
    },
    "equipment": {
        "barbell": "Barra",
        "dumbbell": "Mancuernas",
        "cable": "Polea",
        "machine": "Maquina",
        "body weight": "Peso corporal",
        "kettlebell": "Pesa rusa",
        "band": "Banda elastica",
        "leverage machine": "Maquina de palanca",
        "assisted": "Asistido",
        "smith machine": "Maquina Smith",
        "ez barbell": "Barra Z",
        "trap bar": "Barra trapecio",
        "olympic barbell": "Barra olimpica",
        "bosu ball": "Bosu",
        "medicine ball": "Balon medicinal",
        "stability ball": "Balon de estabilidad",
        "roller": "Rodillo",
        "wheel roller": "Rueda abdominal",
        "rope": "Cuerda",
        "sled machine": "Maquina de trineo",
        "hammer machine": "Maquina Hammer",
    }
}

traducidos = 0
en_ingles = 0
for ex in exercises:
    nombre = ex['name'].lower()
    if nombre in TRADUCCIONES:
        traducciones["exercises"][nombre] = TRADUCCIONES[nombre]
        traducidos += 1
    else:
        traducciones["exercises"][nombre] = ex['name']
        en_ingles += 1

print(f"\nTraducidos al espanol: {traducidos}")
print(f"En ingles: {en_ingles}")
print(f"Total: {len(traducciones['exercises'])}")

with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(traducciones, f, indent=2, ensure_ascii=False)

print("\ntranslations.json generado correctamente")