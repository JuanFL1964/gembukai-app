import json

print("Intentando reparar translations.json...")

# Leer el archivo
try:
    with open("translations.json", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    print(f"Tamaño: {len(contenido)} caracteres")
    
    # Intentar parsear
    try:
        datos = json.loads(contenido)
        print("✅ El JSON está bien, no necesita reparación")
        exit()
    except json.JSONDecodeError as e:
        print(f"❌ Error en línea {e.lineno}, columna {e.colno}: {e.msg}")
        
        # Mostrar contexto del error
        lineas = contenido.split('\n')
        if e.lineno <= len(lineas):
            print(f"\nLínea problemática ({e.lineno}):")
            print(lineas[e.lineno - 1])
            print(" " * (e.colno - 1) + "^")
        
        # Intentar reparación básica: reemplazar comillas simples por dobles
        print("\nIntentando reparación...")
        reparado = contenido.replace("'", '"')
        
        # Eliminar comas trailing
        import re
        reparado = re.sub(r',\s*([}\]])', r'\1', reparado)
        
        # Intentar parsear de nuevo
        try:
            datos = json.loads(reparado)
            print("✅ Reparado con éxito")
            
            # Guardar
            with open("translations.json", "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            
            print(f"Total traducciones: {len(datos.get('exercises', {}))}")
            print("Archivo guardado")
            
        except json.JSONDecodeError as e2:
            print(f"❌ No se pudo reparar: {e2.msg}")
            print(f"Error en línea {e2.lineno}")
            
            # Mostrar las primeras líneas del archivo
            print("\nPrimeras 10 líneas del archivo:")
            for i, linea in enumerate(lineas[:10], 1):
                print(f"{i}: {linea}")
            
except FileNotFoundError:
    print("❌ No se encontró translations.json")
except Exception as e:
    print(f"❌ Error: {e}")