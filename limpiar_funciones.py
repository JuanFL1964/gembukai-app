print("=== LIMPIANDO funciones.js ===")

with open("funciones.js", "r", encoding="utf-8") as f:
    content = f.read()

# Eliminar las declaraciones de variables que ya están en el HTML
lines_to_remove = [
    "let currentUser = null;",
    "let exercisesDB = [];",
    "let translationsDB = { exercises: {}, muscles: {}, equipment: {} };",
    "let usersDB = { users: [] };",
    "let routine = null;",
    "const APPS_SCRIPT_URL",
    "const SHEET_ID",
    "const EXERCISEDB_URL",
    "const EXERCISEDB_BASE_URL",
]

lines = content.split('\n')
cleaned_lines = []
removed = 0

for line in lines:
    stripped = line.strip()
    should_remove = False
    
    for pattern in lines_to_remove:
        if stripped.startswith(pattern):
            should_remove = True
            removed += 1
            break
    
    if not should_remove:
        cleaned_lines.append(line)

content = '\n'.join(cleaned_lines)

with open("funciones.js", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Líneas eliminadas: {removed}")
print("funciones.js limpiado")