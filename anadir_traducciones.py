import json

print("=== AÑADIENDO TRADUCCIONES ===")

with open("translations.json", "r", encoding="utf-8") as f:
    t = json.load(f)

print(f"Total actual: {len(t['exercises'])}")

# Nuevas traducciones a añadir
nuevas = {
    # Pecho - Press de banca variantes
    "barbell wide bench press": "Press de banca agarre ancho con barra",
    "barbell wide reverse grip bench press": "Press de banca agarre inverso ancho con barra",
    "barbell reverse grip bench press": "Press de banca agarre inverso con barra",
    "barbell close grip bench press": "Press de banca agarre cerrado con barra",
    "barbell decline bench press": "Press de banca declinado con barra",
    "barbell incline bench press": "Press de banca inclinado con barra",
    "barbell flat bench press": "Press de banca plano con barra",
    "barbell bench press": "Press de banca con barra",
    
    # Pecho - Estiramientos
    "behind head chest stretch": "Estiramiento de pecho detrás de la cabeza",
    "assisted behind head chest stretch": "Estiramiento de pecho detrás de la cabeza asistido",
    "assisted seated pectoralis major stretch with stability ball": "Estiramiento de pecho asistido con balón",
    "standing chest stretch": "Estiramiento de pecho de pie",
    "standing pectoralis stretch": "Estiramiento de pectoral de pie",
    
    # Pecho - Cable
    "cable bench press": "Press de banca en polea",
    "cable incline bench press": "Press de banca inclinado en polea",
    "cable decline bench press": "Press de banca declinado en polea",
    "cable cross-over variation": "Variación de cruce de poleas",
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
    "cable chest press": "Press de pecho en polea",
    "cable one arm chest press": "Press de pecho a una mano en polea",
    "cable seated chest press": "Press de pecho sentado en polea",
    "cable standing chest press": "Press de pecho de pie en polea",
    "cable incline chest press": "Press de pecho inclinado en polea",
    "cable decline chest press": "Press de pecho declinado en polea",
    
    # Pecho - Máquina
    "machine chest press": "Press de pecho en máquina",
    "machine incline chest press": "Press de pecho inclinado en máquina",
    "machine decline chest press": "Press de pecho declinado en máquina",
    "machine seated chest press": "Press de pecho sentado en máquina",
    "pec deck fly": "Aperturas en máquina pec-deck",
    "pec deck": "Aperturas en máquina pec-deck",
    
    # Pecho - Smith
    "smith machine bench press": "Press de banca en máquina Smith",
    "smith machine incline bench press": "Press de banca inclinado en máquina Smith",
    "smith machine decline bench press": "Press de banca declinado en máquina Smith",
    
    # Pecho - Flexiones
    "push-up": "Flexiones",
    "incline push-up": "Flexiones inclinadas",
    "decline push-up": "Flexiones declinadas",
    "wide-grip push-up": "Flexiones agarre ancho",
    "close-grip push-up": "Flexiones agarre cerrado",
    "diamond push-up": "Flexiones diamante",
    "archer push-up": "Flexiones de arquero",
    "archer push up": "Flexiones de arquero",
    "clap push-up": "Flexiones con aplauso",
    "explosive push-up": "Flexiones explosivas",
    "plyo push-up": "Flexiones pliométricas",
    "one arm push-up": "Flexiones a una mano",
    "clock push-up": "Flexiones reloj",
    
    # Pecho - Fondos
    "chest dip": "Fondos de pecho",
    "wide-grip chest dip": "Fondos de pecho agarre ancho",
    "assisted chest dip": "Fondos de pecho asistidos",
    "assisted chest dip (kneeling)": "Fondos de pecho asistidos (de rodillas)",
    "assisted wide-grip chest dip (kneeling)": "Fondos de pecho agarre ancho asistidos (de rodillas)",
    
    # Pecho - Pullover
    "barbell pullover": "Pullover con barra",
    "dumbbell pullover": "Pullover con mancuerna",
    "barbell bent arm pullover": "Pullover con barra",
    "barbell straight arm pullover": "Pullover con brazos extendidos",
    "jersey barbell": "Pullover con barra",
    "jersey barbell decline": "Pullover con barra en banco declinado",
    "sweater barbell": "Pullover con barra",
    "sweater barbell decline": "Pullover con barra en banco declinado",
    
    # Pecho - Banda
    "band bench press": "Press de banca con banda",
    "band incline bench press": "Press de banca inclinado con banda",
    "band decline bench press": "Press de banca declinado con banda",
    "band fly": "Aperturas con banda",
    "band incline fly": "Aperturas inclinadas con banda",
    "band decline fly": "Aperturas declinadas con banda",
    "band crossover": "Cruce con banda",
    "band pullover": "Pullover con banda",
    "band push-up": "Flexiones con banda",
    "band one arm twisting chest press": "Press de pecho con giro a una mano con banda",
    "band twisting chest press": "Press de pecho con giro con banda",
    
    # Pecho - Mancuernas
    "dumbbell bench press": "Press de banca con mancuernas",
    "dumbbell incline bench press": "Press de banca inclinado con mancuernas",
    "dumbbell decline bench press": "Press de banca declinado con mancuernas",
    "dumbbell fly": "Aperturas con mancuernas",
    "dumbbell incline fly": "Aperturas inclinadas con mancuernas",
    "dumbbell decline fly": "Aperturas declinadas con mancuernas",
    "dumbbell pullover": "Pullover con mancuerna",
    
    # Pecho - Barra
    "barbell bench press": "Press de banca con barra",
    "barbell decline bench press": "Press de banca declinado con barra",
    "barbell incline bench press": "Press de banca inclinado con barra",
    "barbell wide-grip bench press": "Press de banca agarre ancho con barra",
    "barbell close-grip bench press": "Press de banca agarre cerrado con barra",
    "barbell reverse-grip bench press": "Press de banca agarre inverso con barra",
    "barbell guillotine bench press": "Press de banca guillotina con barra",
    "barbell pullover": "Pullover con barra",
    
    # Pecho - Otros
    "svend press": "Press Svend",
    "landmine press": "Press landmine",
    "lever chest press": "Press de pecho en máquina de palanca",
    "lever incline chest press": "Press de pecho inclinado en máquina de palanca",
    "lever decline chest press": "Press de pecho declinado en máquina de palanca",
}

# Añadir solo las que no existen
añadidas = 0
for clave, valor in nuevas.items():
    if clave not in t["exercises"]:
        t["exercises"][clave] = valor
        añadidas += 1
        print(f"  + {clave} -> {valor}")
    else:
        # Si ya existe pero está en inglés, actualizarla
        if t["exercises"][clave] == clave.title() or t["exercises"][clave].lower() == clave:
            t["exercises"][clave] = valor
            añadidas += 1
            print(f"  ~ {clave} -> {valor} (actualizada)")

print(f"\nAñadidas/actualizadas: {añadidas}")
print(f"Total: {len(t['exercises'])}")

with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(t, f, indent=2, ensure_ascii=False)

print("Guardado")