import json

with open("translations.json", "r", encoding="utf-8") as f:
    t = json.load(f)

nuevas = {
    # Pecho - variantes de barra que faltan
    "barbell decline pullover": "Pullover con barra en banco declinado",
    "barbell decline wide-grip press": "Press declinado agarre ancho con barra",
    "barbell front raise and pullover": "Elevacion frontal y pullover con barra",
    "barbell incline pullover": "Pullover con barra en banco inclinado",
    "barbell wide-grip pullover": "Pullover agarre ancho con barra",
    "barbell close-grip pullover": "Pullover agarre cerrado con barra",
    "barbell reverse-grip pullover": "Pullover agarre inverso con barra",
    "barbell decline reverse-grip press": "Press declinado agarre inverso con barra",
    "barbell incline reverse-grip press": "Press inclinado agarre inverso con barra",
    "barbell wide-grip incline press": "Press inclinado agarre ancho con barra",
    "barbell close-grip incline press": "Press inclinado agarre cerrado con barra",
    "barbell wide-grip decline press": "Press declinado agarre ancho con barra",
    "barbell close-grip decline press": "Press declinado agarre cerrado con barra",
    "barbell floor press": "Press en suelo con barra",
    "barbell pin press": "Press de pasador con barra",
    "barbell board press": "Press de tabla con barra",
    "barbell jm press": "Press JM con barra",
    "barbell Tate press": "Press Tate con barra",
    "barbell pullover on exercise ball": "Pullover con barra en balon",
    "barbell pullover with feet on bench": "Pullover con barra y pies en banco",
    
    # Dumbbell variantes
    "dumbbell decline pullover": "Pullover con mancuerna en banco declinado",
    "dumbbell incline pullover": "Pullover con mancuerna en banco inclinado",
    "dumbbell wide-grip pullover": "Pullover agarre ancho con mancuerna",
    "dumbbell front raise and pullover": "Elevacion frontal y pullover con mancuerna",
    "dumbbell floor press": "Press en suelo con mancuernas",
    "dumbbell Tate press": "Press Tate con mancuernas",
    
    # Cable variantes
    "cable pullover": "Pullover en polea",
    "cable incline pullover": "Pullover inclinado en polea",
    "cable decline pullover": "Pullover declinado en polea",
    "cable front raise and pullover": "Elevacion frontal y pullover en polea",
    "cable floor press": "Press en suelo en polea",
    "cable Tate press": "Press Tate en polea",
    
    # Machine variantes
    "machine pullover": "Pullover en maquina",
    "machine incline pullover": "Pullover inclinado en maquina",
    "machine decline pullover": "Pullover declinado en maquina",
    "machine front raise and pullover": "Elevacion frontal y pullover en maquina",
    
    # Smith variantes
    "smith machine pullover": "Pullover en maquina Smith",
    "smith machine incline pullover": "Pullover inclinado en maquina Smith",
    "smith machine decline pullover": "Pullover declinado en maquina Smith",
    "smith machine front raise and pullover": "Elevacion frontal y pullover en maquina Smith",
    "smith machine floor press": "Press en suelo en maquina Smith",
    "smith machine Tate press": "Press Tate en maquina Smith",
    
    # Band variantes
    "band pullover": "Pullover con banda",
    "band incline pullover": "Pullover inclinado con banda",
    "band decline pullover": "Pullover declinado con banda",
    "band front raise and pullover": "Elevacion frontal y pullover con banda",
    "band floor press": "Press en suelo con banda",
    
    # Lever variantes
    "lever pullover": "Pullover en maquina de palanca",
    "lever incline pullover": "Pullover inclinado en maquina de palanca",
    "lever decline pullover": "Pullover declinado en maquina de palanca",
    "lever front raise and pullover": "Elevacion frontal y pullover en maquina de palanca",
    "lever floor press": "Press en suelo en maquina de palanca",
}

anadidas = 0
for clave, valor in nuevas.items():
    if clave in t["exercises"]:
        viejo = t["exercises"][clave]
        # Solo actualizar si esta en ingles o es igual a la clave
        if viejo.lower() == clave or viejo == clave.title():
            t["exercises"][clave] = valor
            anadidas += 1
            print(f"  ~ {clave} -> {valor}")

print(f"\nActualizadas: {anadidas}")
print(f"Total: {len(t['exercises'])}")

with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(t, f, indent=2, ensure_ascii=False)

print("Guardado")