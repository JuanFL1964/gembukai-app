import json

print("=== CORRECCIONES ESPECIFICAS ===")

with open("translations.json", "r", encoding="utf-8") as f:
    traducciones = json.load(f)

print(f"Total traducciones: {len(traducciones['exercises'])}")

# Correcciones específicas (busca por la traducción mala exacta)
correcciones = {
    # Archer push up
    "Archer flexion": "Flexiones de arquero",
    "Archer push up": "Flexiones de arquero",
    "Archer push-up": "Flexiones de arquero",
    
    # Assisted chest dip
    "Asistido chest fondo (de rodillas)": "Fondos de pecho asistidos (de rodillas)",
    "Asistido chest fondo": "Fondos de pecho asistidos",
    "Chest fondo asistido": "Fondos de pecho asistidos",
    "Fondo de pecho asistido": "Fondos de pecho asistidos",
    "Fondos de pecho asistidos (de rodillas)": "Fondos de pecho asistidos (de rodillas)",
    
    # Assisted wide-grip chest dip
    "Asistido agarre ancho chest fondo (de rodillas)": "Fondos de pecho agarre ancho asistidos (de rodillas)",
    "Asistido agarre ancho chest fondo": "Fondos de pecho agarre ancho asistidos",
    
    # Band exercises
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
    
    # Chest stretch
    "Estiramiento de pecho asistido con balon": "Estiramiento de pecho asistido con balon",
    "Estiramiento de pecho asistido": "Estiramiento de pecho asistido",
    
    # Mezclas inglés/español comunes
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
    
    # Twisting
    "Twisting chest press": "Press de pecho con giro",
    "Twisting": "Con giro",
    
    # One arm
    "A una mano": "A una mano",
    "One arm": "A una mano",
    
    # Limpieza de dobles espacios
    "  ": " ",
}

# Buscar y reemplazar
corregidas = 0
for valor_malo, valor_correcto in correcciones.items():
    for clave, valor in list(traducciones["exercises"].items()):
        if valor == valor_malo:
            traducciones["exercises"][clave] = valor_correcto
            corregidas += 1
            print(f"  '{valor_malo}' -> '{valor_correcto}'")

print(f"\nTotal correcciones: {corregidas}")

# Capitalizar todo
def capitalizar(texto):
    if texto and len(texto) > 0:
        return texto[0].upper() + texto[1:]
    return texto

for clave, valor in traducciones["exercises"].items():
    traducciones["exercises"][clave] = capitalizar(valor)

for clave, valor in traducciones.get("equipment", {}).items():
    traducciones["equipment"][clave] = capitalizar(valor)

for clave, valor in traducciones.get("muscles", {}).items():
    traducciones["muscles"][clave] = capitalizar(valor)

with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(traducciones, f, indent=2, ensure_ascii=False)

print(f"Guardado con {len(traducciones['exercises'])} traducciones")