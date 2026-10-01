import re

print("=== AÑADIENDO FUNCION enterApp() ===")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Verificar si ya existe la función
if "function enterApp()" in content or "const enterApp" in content:
    print("✅ La función enterApp() ya existe")
else:
    print("❌ La función enterApp() NO existe. Añadiéndola...")
    
    # Buscar dónde añadir la función (antes del cierre del body o en el script)
    # Añadir después de las constantes o al inicio del script
    enter_app_code = """
function enterApp() {
    console.log('Entrando a la app...');
    document.getElementById('splash-screen').classList.add('hidden');
    document.getElementById('main-header').style.display = 'block';
    showScreen('screen-login');
}
"""
    
    # Buscar la etiqueta <script> y añadir la función
    if "<script>" in content:
        content = content.replace("<script>", "<script>" + enter_app_code)
        print("✅ Función enterApp() añadida")
    else:
        print("❌ No se encontró la etiqueta <script>")
        exit()

# Guardar
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\nindex.html actualizado")