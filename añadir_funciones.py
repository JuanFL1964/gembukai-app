print("Añadiendo funciones.js al HTML...")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if "funciones.js" not in content:
    if "</head>" in content:
        content = content.replace("</head>", '<script src="funciones.js"></script>\n</head>')
        print("Referencia añadida")
    else:
        print("No se encontró </head>")
        exit()
else:
    print("Ya existe la referencia")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("HTML actualizado")