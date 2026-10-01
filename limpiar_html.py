import re

print("=== LIMPIANDO index.html ===")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print(f"Tamaño original: {len(content)} caracteres")

# 1. Eliminar marcadores de conflicto de Git
# Patrones como: @@ -1,178 +1,178 @@
content = re.sub(r'^@@ -\d+,\d+ \+\d+,\d+ @@.*$', '', content, flags=re.MULTILINE)

# Patrones como: <<<<<<< HEAD, =======, >>>>>>> commit
content = re.sub(r'^<<<<<<< HEAD\s*$', '', content, flags=re.MULTILINE)
content = re.sub(r'^=======\s*$', '', content, flags=re.MULTILINE)
content = re.sub(r'^>>>>>>> [a-f0-9]+\s*$', '', content, flags=re.MULTILINE)

# 2. Eliminar líneas vacías múltiples
content = re.sub(r'\n{3,}', '\n\n', content)

# 3. Eliminar caracteres raros al inicio
content = content.lstrip('@ \n')

print(f"Tamaño después de limpiar: {len(content)} caracteres")

# Guardar
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ index.html limpiado")