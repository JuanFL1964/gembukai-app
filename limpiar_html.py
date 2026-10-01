import re

print("=== LIMPIANDO index.html COMPLETAMENTE ===")

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total líneas: {len(lines)}")

# Filtrar líneas problemáticas
cleaned_lines = []
removed = 0

for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Eliminar líneas que empiecen con @@ (marcadores de diff)
    if stripped.startswith('@@'):
        removed += 1
        continue
    
    # Eliminar líneas que empiecen con <<<<<<<
    if stripped.startswith('<<<<<<<'):
        removed += 1
        continue
    
    # Eliminar líneas que sean exactamente =======
    if stripped == '=======':
        removed += 1
        continue
    
    # Eliminar líneas que empiecen con >>>>>>>
    if stripped.startswith('>>>>>>>'):
        removed += 1
        continue
    
    # Eliminar líneas que empiecen con + o - (marcadores de diff)
    if stripped.startswith('+') or stripped.startswith('-'):
        # Pero no si son parte del código HTML normal
        if len(stripped) > 1 and stripped[1] not in [' ', '\t']:
            removed += 1
            continue
    
    cleaned_lines.append(line)

print(f"Líneas eliminadas: {removed}")
print(f"Líneas restantes: {len(cleaned_lines)}")

# Unir y guardar
content = ''.join(cleaned_lines)

# Eliminar caracteres raros al inicio
content = content.lstrip('@ \n+-')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ index.html limpiado")
print(f"Tamaño final: {len(content)} caracteres")