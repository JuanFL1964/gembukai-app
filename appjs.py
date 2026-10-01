print("=== ANADIENDO REFERENCIA A app.js ===")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Buscar </head> y añadir el script antes
if "</head>" in content:
    script_tag = '<script src="app.js"></script>\n'
    content = content.replace("</head>", script_tag + "</head>")
    print("✅ Referencia a app.js añadida antes de </head>")
else:
    print(" No se encontró </head>")
    exit()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\nindex.html actualizado")