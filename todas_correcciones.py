import json
import re

print("=== APLICANDO TODAS LAS CORRECCIONES ===")

with open("translations.json", "r", encoding="utf-8") as f:
    traducciones = json.load(f)

print(f"Total traducciones: {len(traducciones['exercises'])}")

# ============================================
# 1. CORRECCIONES POR CLAVE EN INGLÉS
# ============================================
correcciones_clave = {
    # Pecho - Press
    "barbell bench press": "Press de banca con barra",
    "barbell decline bench press": "Press de banca declinado con barra",
    "barbell incline bench press": "Press de banca inclinado con barra",
    "barbell wide-grip bench press": "Press de banca agarre ancho con barra",
    "barbell close-grip bench press": "Press de banca agarre cerrado con barra",
    "barbell reverse-grip bench press": "Press de banca agarre inverso con barra",
    "barbell guillotine bench press": "Press de banca guillotina con barra",
    "dumbbell bench press": "Press de banca con mancuernas",
    "dumbbell incline bench press": "Press de banca inclinado con mancuernas",
    "dumbbell decline bench press": "Press de banca declinado con mancuernas",
    "dumbbell fly": "Aperturas con mancuernas",
    "dumbbell incline fly": "Aperturas inclinadas con mancuernas",
    "dumbbell decline fly": "Aperturas declinadas con mancuernas",
    "smith machine bench press": "Press de banca en maquina Smith",
    "smith machine incline bench press": "Press de banca inclinado en maquina Smith",
    "smith machine decline bench press": "Press de banca declinado en maquina Smith",
    "machine chest press": "Press de pecho en maquina",
    "machine incline chest press": "Press de pecho inclinado en maquina",
    "machine decline chest press": "Press de pecho declinado en maquina",
    
    # Pecho - Flexiones
    "push-up": "Flexiones",
    "incline push-up": "Flexiones inclinadas",
    "decline push-up": "Flexiones declinadas",
    "wide-grip push-up": "Flexiones agarre ancho",
    "close-grip push-up": "Flexiones agarre cerrado",
    "diamond push-up": "Flexiones diamante",
    "archer push-up": "Flexiones de arquero",
    "clap push-up": "Flexiones con aplauso",
    "explosive push-up": "Flexiones explosivas",
    "plyo push-up": "Flexiones pliometricas",
    "one arm push-up": "Flexiones a una mano",
    "clock push-up": "Flexiones reloj",
    
    # Pecho - Fondos
    "chest dip": "Fondos de pecho",
    "wide-grip chest dip": "Fondos de pecho agarre ancho",
    "assisted chest dip": "Fondos de pecho asistidos",
    "assisted chest dip (kneeling)": "Fondos de pecho asistidos (de rodillas)",
    "assisted wide-grip chest dip (kneeling)": "Fondos de pecho agarre ancho asistidos (de rodillas)",
    
    # Pecho - Poleas
    "cable crossover": "Cruce de poleas",
    "cable chest fly": "Cruce de poleas al pecho",
    "cable incline fly": "Cruce de poleas inclinado",
    "cable decline fly": "Cruce de poleas declinado",
    "cable high fly": "Cruce de poleas alto",
    "cable low fly": "Cruce de poleas bajo",
    "cable middle fly": "Cruce de poleas medio",
    "cable one arm fly": "Cruce de poleas a una mano",
    "cable upper chest crossover": "Cruce de poleas pecho superior",
    "cable lower chest crossover": "Cruce de poleas pecho inferior",
    "cable middle chest crossover": "Cruce de poleas pecho medio",
    "cable standing crossover": "Cruce de poleas de pie",
    "cable seated crossover": "Cruce de poleas sentado",
    "pec deck fly": "Aperturas en maquina pec-deck",
    
    # Pecho - Pullover
    "barbell pullover": "Pullover con barra",
    "dumbbell pullover": "Pullover con mancuerna",
    "barbell bent arm pullover": "Pullover con barra",
    "barbell straight arm pullover": "Pullover con brazos extendidos",
    "jersey barbell": "Pullover con barra",
    "jersey barbell decline": "Pullover con barra en banco declinado",
    "sweater barbell": "Pullover con barra",
    "sweater barbell decline": "Pullover con barra en banco declinado",
    
    # Pecho - Band
    "band bench press": "Press de banca con banda",
    "band incline bench press": "Press de banca inclinado con banda",
    "band decline bench press": "Press de banca declinado con banda",
    "band fly": "Aperturas con banda",
    "band incline fly": "Aperturas inclinadas con banda",
    "band decline fly": "Aperturas declinadas con banda",
    "band crossover": "Cruce con banda",
    "band pullover": "Pullover con banda",
    "band push-up": "Flexiones con banda",
    
    # Espalda
    "pull-up": "Dominadas",
    "wide-grip pull-up": "Dominadas agarre ancho",
    "close-grip pull-up": "Dominadas agarre cerrado",
    "neutral-grip pull-up": "Dominadas agarre neutro",
    "assisted pull-up": "Dominadas asistidas",
    "chin-up": "Dominadas agarre supino",
    "assisted chin-up": "Dominadas agarre supino asistidas",
    "lat pulldown": "Jalon al pecho",
    "wide-grip lat pulldown": "Jalon al pecho agarre ancho",
    "close-grip lat pulldown": "Jalon al pecho agarre cerrado",
    "barbell bent over row": "Remo con barra",
    "barbell pendlay row": "Remo Pendlay con barra",
    "barbell t-bar row": "Remo en barra T",
    "dumbbell row": "Remo con mancuerna",
    "one arm dumbbell row": "Remo con mancuerna a una mano",
    "seated cable row": "Remo en polea baja",
    "deadlift": "Peso muerto",
    "barbell deadlift": "Peso muerto con barra",
    "romanian deadlift": "Peso muerto rumano",
    "sumo deadlift": "Peso muerto sumo",
    "face pull": "Face pull",
    "barbell shrug": "Encogimientos con barra",
    "dumbbell shrug": "Encogimientos con mancuernas",
    "hyperextension": "Hiperextensiones lumbares",
    "good morning": "Buenos dias",
    
    # Piernas
    "barbell squat": "Sentadilla con barra",
    "front squat": "Sentadilla frontal",
    "goblet squat": "Sentadilla goblet",
    "hack squat": "Sentadilla hack",
    "leg press": "Prensa de piernas",
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
    
    # Hombros
    "barbell shoulder press": "Press militar con barra",
    "dumbbell shoulder press": "Press militar con mancuernas",
    "arnold press": "Press Arnold",
    "lateral raise": "Elevaciones laterales",
    "dumbbell lateral raise": "Elevaciones laterales con mancuernas",
    "cable lateral raise": "Elevaciones laterales en polea",
    "front raise": "Elevaciones frontales",
    "dumbbell front raise": "Elevaciones frontales con mancuernas",
    "rear delt fly": "Pajaros (deltoides posterior)",
    "upright row": "Remo al menton",
    
    # Brazos
    "barbell curl": "Curl de biceps con barra",
    "dumbbell curl": "Curl de biceps con mancuernas",
    "ez bar curl": "Curl con barra Z",
    "hammer curl": "Curl martillo",
    "dumbbell hammer curl": "Curl martillo con mancuernas",
    "cable hammer curl": "Curl martillo en polea",
    "preacher curl": "Curl predicador",
    "concentration curl": "Curl concentrado",
    "cable curl": "Curl en polea",
    "spider curl": "Curl arana",
    "reverse barbell curl": "Curl inverso con barra",
    "wrist curl": "Curl de muneca",
    "tricep pushdown": "Extension de triceps en polea",
    "rope pushdown": "Extension de triceps con cuerda",
    "overhead tricep extension": "Extension de triceps sobre la cabeza",
    "skull crusher": "Rompecranos",
    "tricep dip": "Fondos de triceps",
    "close-grip bench press": "Press de banca agarre cerrado",
    
    # Core
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
    "v-up": "V-up",
    "flutter kicks": "Patadas de aleta",
    "woodchop": "Lenador",
    
    # Cardio
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
}

# Aplicar correcciones por clave
c1 = 0
for clave, traduccion in correcciones_clave.items():
    if clave in traducciones["exercises"]:
        traducciones["exercises"][clave] = traduccion
        c1 += 1
print(f"1. Correcciones por clave: {c1}")

# ============================================
# 2. CORRECCIONES POR VALOR (traducciones malas)
# ============================================
correcciones_valor = {
    "Archer flexion": "Flexiones de arquero",
    "Asistido chest fondo (de rodillas)": "Fondos de pecho asistidos (de rodillas)",
    "Asistido chest fondo": "Fondos de pecho asistidos",
    "Asistido agarre ancho chest fondo (de rodillas)": "Fondos de pecho agarre ancho asistidos (de rodillas)",
    "Asistido agarre ancho chest fondo": "Fondos de pecho agarre ancho asistidos",
    "Band bench press": "Press de banca con banda",
    "Band a una mano twisting chest press": "Press de pecho con giro a una mano con banda",
    "Band chest press": "Press de pecho con banda",
    "Band incline chest press": "Press de pecho inclinado con banda",
    "Band decline chest press": "Press de pecho declinado con banda",
    "Band fly": "Aperturas con banda",
    "Band incline fly": "Aperturas inclinadas con banda",
    "Band decline fly": "Aperturas declinadas con banda",
    "Band crossover": "Cruce con banda",
    "Band pullover": "Pullover con banda",
    "Band push-up": "Flexiones con banda",
    "Band squat": "Sentadilla con banda",
    "Band lunge": "Zancadas con banda",
    "Band deadlift": "Peso muerto con banda",
    "Band row": "Remo con banda",
    "Band curl": "Curl con banda",
    "Band tricep extension": "Extension de triceps con banda",
    "Band shoulder press": "Press de hombros con banda",
    "Band lateral raise": "Elevaciones laterales con banda",
    "Band front raise": "Elevaciones frontales con banda",
    "Band calf raise": "Elevacion de gemelos con banda",
    "Band leg extension": "Extensiones de cuadriceps con banda",
    "Band leg curl": "Curl femoral con banda",
    "Band hip thrust": "Hip thrust con banda",
    "Band glute bridge": "Puente de gluteos con banda",
    "Band pull-up": "Dominadas con banda",
    "Band chin-up": "Dominadas agarre supino con banda",
    "Band dip": "Fondos con banda",
    "Band plank": "Plancha con banda",
    "Band crunch": "Crunch con banda",
    "Band woodchop": "Lenador con banda",
    "Chest fondo": "Fondos de pecho",
    "Chest press": "Press de pecho",
    "Chest fly": "Aperturas de pecho",
    "Chest dip": "Fondos de pecho",
    "Shoulder press": "Press de hombros",
    "Shoulder fly": "Aperturas de hombros",
    "Bicep curl": "Curl de biceps",
    "Tricep extension": "Extension de triceps",
    "Tricep pushdown": "Extension de triceps en polea",
    "Leg press": "Prensa de piernas",
    "Leg extension": "Extensiones de cuadriceps",
    "Leg curl": "Curl femoral",
    "Calf raise": "Elevacion de gemelos",
    "Hip thrust": "Hip thrust",
    "Glute bridge": "Puente de gluteos",
    "Lat pulldown": "Jalon al pecho",
    "Face pull": "Face pull",
    "Rack pull": "Rack pull",
    "Good morning": "Buenos dias",
    "Step-up": "Step-up",
    "V-up": "V-up",
    "Thruster": "Thruster",
    "Clean and jerk": "Cargada y jerk",
    "Snatch": "Arranque",
    "Power clean": "Cargada de potencia",
    "Twisting chest press": "Press de pecho con giro",
}

c2 = 0
for valor_malo, valor_correcto in correcciones_valor.items():
    for clave, valor in list(traducciones["exercises"].items()):
        if valor == valor_malo:
            traducciones["exercises"][clave] = valor_correcto
            c2 += 1
print(f"2. Correcciones por valor: {c2}")

# ============================================
# 3. PATRONES REGULARES (reemplazos automáticos)
# ============================================
PATRONES = [
    (r'\bPrensa de\b', 'Press de'),
    (r'\bprensa de\b', 'Press de'),
    (r'\bcrossover\b', 'cruce'),
    (r'\bCrossover\b', 'Cruce'),
    (r'\bCrossovers\b', 'Cruces'),
    (r'\bcrossovers\b', 'cruces'),
    (r'\bdecline\b', 'declinado'),
    (r'\bDecline\b', 'Declinado'),
    (r'\bincline\b', 'inclinado'),
    (r'\bIncline\b', 'Inclinado'),
    (r'\bflat\b', 'plano'),
    (r'\bFlat\b', 'Plano'),
    (r'\bbarbell\b', 'con barra'),
    (r'\bBarbell\b', 'Con barra'),
    (r'\bdumbbell\b', 'con mancuernas'),
    (r'\bDumbbell\b', 'Con mancuernas'),
    (r'\bcable\b', 'en polea'),
    (r'\bCable\b', 'En polea'),
    (r'\bmachine\b', 'en maquina'),
    (r'\bMachine\b', 'En maquina'),
    (r'\bsmith machine\b', 'en maquina Smith'),
    (r'\bSmith machine\b', 'En maquina Smith'),
    (r'\bassisted\b', 'asistido'),
    (r'\bAssisted\b', 'Asistido'),
    (r'\bwide[- ]?grip\b', 'agarre ancho'),
    (r'\bWide[- ]?grip\b', 'Agarre ancho'),
    (r'\bclose[- ]?grip\b', 'agarre cerrado'),
    (r'\bClose[- ]?grip\b', 'Agarre cerrado'),
    (r'\breverse[- ]?grip\b', 'agarre inverso'),
    (r'\bReverse[- ]?grip\b', 'Agarre inverso'),
    (r'\bneutral[- ]?grip\b', 'agarre neutro'),
    (r'\bNeutral[- ]?grip\b', 'Agarre neutro'),
    (r'\bone arm\b', 'a una mano'),
    (r'\bOne arm\b', 'A una mano'),
    (r'\btwo arm\b', 'a dos manos'),
    (r'\bTwo arm\b', 'A dos manos'),
    (r'\bstanding\b', 'de pie'),
    (r'\bStanding\b', 'De pie'),
    (r'\bseated\b', 'sentado'),
    (r'\bSeated\b', 'Sentado'),
    (r'\blying\b', 'tumbado'),
    (r'\bLying\b', 'Tumbado'),
    (r'\bhanging\b', 'colgado'),
    (r'\bHanging\b', 'Colgado'),
    (r'\bkneeling\b', 'de rodillas'),
    (r'\bKneeling\b', 'De rodillas'),
    (r'\bwith stability ball\b', 'con balon de estabilidad'),
    (r'\bwith ball\b', 'con balon'),
    (r'\bwith band\b', 'con banda'),
    (r'\bwith rope\b', 'con cuerda'),
    (r'\bwith bar\b', 'con barra'),
    (r'\bwith dumbbell\b', 'con mancuerna'),
    (r'\bwith barbell\b', 'con barra'),
    (r'\bwith kettlebell\b', 'con pesa rusa'),
    (r'\bwith weight\b', 'lastrado'),
    (r'\bwith medicine ball\b', 'con balon medicinal'),
    (r'\bwith bosu ball\b', 'con bosu'),
    (r'\bwith roller\b', 'con rodillo'),
    (r'\bjersey\b', 'pullover'),
    (r'\bJersey\b', 'Pullover'),
    (r'\bsweater\b', 'pullover'),
    (r'\bSweater\b', 'Pullover'),
    (r'\bfly\b', 'aperturas'),
    (r'\bFly\b', 'Aperturas'),
    (r'\bExtension\b', 'Extension'),
    (r'\braise\b', 'elevacion'),
    (r'\bRaise\b', 'Elevacion'),
    (r'\brow\b', 'remo'),
    (r'\bRow\b', 'Remo'),
    (r'\bsquat\b', 'sentadilla'),
    (r'\bSquat\b', 'Sentadilla'),
    (r'\blunge\b', 'zancada'),
    (r'\bLunge\b', 'Zancada'),
    (r'\bdeadlift\b', 'peso muerto'),
    (r'\bDeadlift\b', 'Peso muerto'),
    (r'\bshrug\b', 'encogimiento'),
    (r'\bShrug\b', 'Encogimiento'),
    (r'\bdip\b', 'fondo'),
    (r'\bDip\b', 'Fondo'),
    (r'\bpush[- ]?up\b', 'flexion'),
    (r'\bPush[- ]?up\b', 'Flexion'),
    (r'\bpush[- ]?ups\b', 'flexiones'),
    (r'\bPush[- ]?ups\b', 'Flexiones'),
    (r'\bplank\b', 'plancha'),
    (r'\bPlank\b', 'Plancha'),
    (r'\bleg raise\b', 'elevacion de piernas'),
    (r'\bLeg raise\b', 'Elevacion de piernas'),
    (r'\brussian twist\b', 'giros rusos'),
    (r'\bRussian twist\b', 'Giros rusos'),
    (r'\bmountain climber\b', 'escalador'),
    (r'\bMountain climber\b', 'Escalador'),
    (r'\bab wheel\b', 'rueda abdominal'),
    (r'\bAb wheel\b', 'Rueda abdominal'),
    (r'\bsit[- ]?up\b', 'abdominal'),
    (r'\bSit[- ]?up\b', 'Abdominal'),
    (r'\bflutter kicks\b', 'patadas de aleta'),
    (r'\bFlutter kicks\b', 'Patadas de aleta'),
    (r'\bwoodchop\b', 'lenador'),
    (r'\bWoodchop\b', 'Lenador'),
    (r'\brunning\b', 'correr'),
    (r'\bRunning\b', 'Correr'),
    (r'\bcycling\b', 'ciclismo'),
    (r'\bCycling\b', 'Ciclismo'),
    (r'\bjump rope\b', 'saltar a la cuerda'),
    (r'\bJump rope\b', 'Saltar a la cuerda'),
    (r'\bjumping jacks\b', 'saltos de tijera'),
    (r'\bJumping jacks\b', 'Saltos de tijera'),
    (r'\browing\b', 'remo'),
    (r'\bRowing\b', 'Remo'),
    (r'\btreadmill\b', 'cinta de correr'),
    (r'\bTreadmill\b', 'Cinta de correr'),
    (r'\bstationary bike\b', 'bicicleta estatica'),
    (r'\bStationary bike\b', 'Bicicleta estatica'),
    (r'\bkettlebell swing\b', 'swing con pesa rusa'),
    (r'\bKettlebell swing\b', 'Swing con pesa rusa'),
    (r'\bbox jump\b', 'salto al cajon'),
    (r'\bBox jump\b', 'Salto al cajon'),
    (r'\bbattle ropes\b', 'cuerdas de batalla'),
    (r'\bBattle ropes\b', 'Cuerdas de batalla'),
    (r'\bhigh knees\b', 'rodillas al pecho'),
    (r'\bHigh knees\b', 'Rodillas al pecho'),
    (r'\bbutt kicks\b', 'talones al gluteo'),
    (r'\bButt kicks\b', 'Talones al gluteo'),
    (r'\bsquat jump\b', 'sentadilla con salto'),
    (r'\bSquat jump\b', 'Sentadilla con salto'),
    (r'\blateral jump\b', 'salto lateral'),
    (r'\bLateral jump\b', 'Salto lateral'),
    (r'\bclock push[- ]?up\b', 'flexiones reloj'),
    (r'\bClock push[- ]?up\b', 'Flexiones reloj'),
    (r'  +', ' '),
]

def aplicar_patrones(texto):
    for patron, reemplazo in PATRONES:
        texto = re.sub(patron, reemplazo, texto)
    return texto.strip()

def capitalizar(texto):
    if texto and len(texto) > 0:
        return texto[0].upper() + texto[1:]
    return texto

c3 = 0
for clave, valor in traducciones["exercises"].items():
    nuevo = aplicar_patrones(valor)
    nuevo = capitalizar(nuevo)
    if nuevo != valor:
        traducciones["exercises"][clave] = nuevo
        c3 += 1
print(f"3. Correcciones por patrones: {c3}")

# Capitalizar equipos y músculos
for clave, valor in traducciones.get("equipment", {}).items():
    traducciones["equipment"][clave] = capitalizar(valor)
for clave, valor in traducciones.get("muscles", {}).items():
    traducciones["muscles"][clave] = capitalizar(valor)

with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(traducciones, f, indent=2, ensure_ascii=False)

print(f"✅ Guardado con {len(traducciones['exercises'])} traducciones")