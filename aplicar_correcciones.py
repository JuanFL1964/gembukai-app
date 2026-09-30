import json
import re

print("Aplicando correcciones...")

with open("translations.json", "r", encoding="utf-8") as f:
    traducciones = json.load(f)

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

def aplicar_correcciones(texto):
    for patron, reemplazo in PATRONES:
        texto = re.sub(patron, reemplazo, texto)
    return texto.strip()

def capitalizar(texto):
    if texto and len(texto) > 0:
        return texto[0].upper() + texto[1:]
    return texto

corregidas = 0
for clave, valor in traducciones["exercises"].items():
    nuevo = aplicar_correcciones(valor)
    nuevo = capitalizar(nuevo)
    if nuevo != valor:
        traducciones["exercises"][clave] = nuevo
        corregidas += 1

print(f"Corregidas: {corregidas}")

for clave, valor in traducciones.get("equipment", {}).items():
    traducciones["equipment"][clave] = capitalizar(valor)
for clave, valor in traducciones.get("muscles", {}).items():
    traducciones["muscles"][clave] = capitalizar(valor)

with open("translations.json", "w", encoding="utf-8") as f:
    json.dump(traducciones, f, indent=2, ensure_ascii=False)

print(f"Guardado con {len(traducciones['exercises'])} traducciones")