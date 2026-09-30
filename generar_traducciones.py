import json

# Leer el archivo actual
with open("translations.json", "r", encoding="utf-8") as f:
    traducciones = json.load(f)

print(f"Total traducciones actuales: {len(traducciones['exercises'])}")

# Correcciones manuales (traducción mala → traducción correcta)
correcciones = {
    # Pecho
    "sweater barbell": "Pullover con barra",
    "sweater barbell decline": "Pullover con barra en banco declinado",
    "jersey barbell": "Pullover con barra",
    "jersey barbell decline": "Pullover con barra en banco declinado",
    "press de banca barbell decline": "Press de banca declinado con barra",
    "prensa de agarre ancho barbell decline": "Press de banca agarre ancho declinado con barra",
    "suéter de brazo doblado con barra": "Pullover con barra",
    
    # Espalda
    "pull-up": "Dominadas",
    "chin-up": "Dominadas agarre supino",
    "lat pulldown": "Jalón al pecho",
    "barbell bent over row": "Remo con barra",
    "deadlift": "Peso muerto",
    "romanian deadlift": "Peso muerto rumano",
    
    # Piernas
    "barbell squat": "Sentadilla con barra",
    "front squat": "Sentadilla frontal",
    "leg press": "Prensa de piernas",
    "lunge": "Zancadas",
    "leg extension": "Extensiones de cuádriceps",
    "leg curl": "Curl femoral",
    "calf raise": "Elevación de gemelos",
    "hip thrust": "Hip thrust",
    
    # Hombros
    "barbell shoulder press": "Press militar con barra",
    "dumbbell shoulder press": "Press militar con mancuernas",
    "lateral raise": "Elevaciones laterales",
    "front raise": "Elevaciones frontales",
    "upright row": "Remo al mentón",
    
    # Brazos
    "barbell curl": "Curl de bíceps con barra",
    "dumbbell curl": "Curl de bíceps con mancuernas",
    "hammer curl": "Curl martillo",
    "tricep pushdown": "Extensión de tríceps en polea",
    
    # Core
    "plank": "Plancha",
    "crunch": "Crunch abdominal",
    "leg raise": "Elevación de piernas",
    "russian twist": "Giros rusos",
    
    # Cardio
    "burpee": "Burpee",
    "running": "Correr",
    "cycling": "Ciclismo",
    "jump rope": "Saltar a la cuerda",
}

# Aplicar correcciones
corregidas = 0
for clave_mala, traduccion_correcta in correcciones.items():
    if clave_mala in traducciones["exercises"]:
        traducciones["exercises"][clave_mala] = traduccion_correcta
        corregidas += 1
        print(f"✅ Corregido: '{clave_mala}' → '{traduccion_correcta}'")

print(f"\nTotal correcciones aplicadas: {corregidas}")

# Guardar
with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(traducciones, f, indent=2, ensure_ascii=False)

print(f"✅ Archivo guardado con {len(traducciones['exercises'])} traducciones")