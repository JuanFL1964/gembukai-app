print("=== AÑADIENDO REFERENCIA A app.js ===")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Buscar </body> y añadir el script antes
if "</body>" in content:
    script_tag = '<script src="app.js"></script>\n'
    content = content.replace("</body>", script_tag + "</body>")
    print("✅ Referencia a app.js añadida antes de </body>")
else:
    print("❌ No se encontró </body>")
    exit()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\nindex.html actualizado")