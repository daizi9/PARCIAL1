titulos = ["50 sombras de grey", "Hush Hush", "Los juegos del hambre"]
ejemplares = [8, 2, 4]

while True:
    print("\n--- SISTEMA DE GESTION DE BIBLIOTECA ---")
    print("1. Ingresar titulos")
    print("2. Ingresar ejemplares(titulos existentes)")
    print("3. Mostrar catalogo completo")
    print("4. Consultar disponibilidad")
    print("5. Lista agotados")
    print("6. Agregar titulo (y ejemplares)")
    print("7. Actualizar ejeemplares (Prestamo/Devolucion)")
    print("8. Salir")

 
    seleccion = input("Seleccione opción: ").strip()


    if not seleccion.isdigit():
        print("Opción inválida. Ingrese un número del 1 al 8.")
        continue

  
    if seleccion == "8":
        print("Saliendo del sistema. ¡Nos vemos!")
        break


    if seleccion =="1":
        print("\n--- 1. Ingresar Títulos---")
        
        cantidad_valida = False
        cantidad = 0
        
        while not cantidad_valida:
            cant_str = input("Cuantos titulos ingresara? ").strip()

            if cant_str.isdigit() and int(cant_str) > 0:
                cantidad = int(cant_str)
                cantidad_valida = True
            else:
                print("Cantidad invalida.Intente de nuevo")
        
        titulos_agregados = 0
        i = 0
        
        while i < cantidad:
            nuevo_titulo = input(f"\nIngrese título {i + 1}/{cantidad}: ").strip()
            
            if nuevo_titulo == "": 
                print("El titulo no puede ser vacio.Intente nuevamente")
                continue

            nombre_normalizado = nuevo_titulo.lower()

            es_duplicado = False
            j = 0
            while j < len(titulos):
                if titulos[j].lower() == nombre_normalizado:
                    es_duplicado = True
                    break
                j += 1
                
            if es_duplicado:
                print(f"El titulo '{nuevo_titulo}' ya existe en el catalogo")
                i += 1 
                continue 
                
            titulos.append(nuevo_titulo)
            ejemplares.append(0)
            titulos_agregados += 1
            i += 1 
            
        print(f"\nProceso completado. Se agregaron {titulos_agregados}. Use la Opcion 2 para agregar ejemplares")
        
    elif seleccion == "2":
        print("\n--- 2. Ingresar ejemplares disponibles ---")
        if not titulos:
            print ("Primero debe ingresar títulos usando la Opción 1 o 6.")
        else:
            k=0
            while k < len(titulos):
                print(f"\nLibro: '{titulos[k]}'. ejemplares actuales: {ejemplares[k]}")
                cant_valida=False

                while not cant_valida:
                    ejemplares_str = input("Ingrese la cantidad de ejemplares a añadir: ").strip()
                    if ejemplares_str.isdigit() and int(ejemplares_str) >=0:
                        ejemplares[k] += int(ejemplares_str)
                        cant_valida= True
                    else:
                        print("Cantidad inválida. Debe ser un número entero positivo o cero.")

                k +=1
            print("Actualización completada.")
        
    elif seleccion =="3":
        print("\n--- 3. Ver Catálogo Completo ---")
        if not titulos:
            print("El catalogo esta vacio")
        else:
            print(f"{'TÍTULO':<40} | {'STOCK':>5}")
            print("=" * 47)
            i = 0
            while i < len(titulos):
                print(f"{titulos[i]:<40} | {ejemplares[i]:>5}")
                i += 1

    elif seleccion =="4":
        print("\n--- 4. Consultar disponibilidad ---")
        if not titulos:
            print("El catalogo está vacio")
        else:
            nomb_busco = input("Ingrese el titulo a consultar: ").strip()

            if nomb_busco == "":
                print("La búsqueda no puede estar vacia.")
            else:
                indice_encontrado = -1
                nomb_busco_normalizada = nomb_busco.lower()
                i = 0
                while i < len(titulos):
                    if titulos[i].lower() == nomb_busco_normalizada: 
                        indice_encontrado = i
                        break
                    i += 1

                if indice_encontrado != -1:
                    print(f"Título: '{titulos[indice_encontrado]}'")
                    print(f"Ejemplares disponibles: {ejemplares[indice_encontrado]}")
                else:
                    print(f"Título '{nomb_busco}' no encontrado en el catálogo.")
                    
    elif seleccion =="5":
        print("\n--- 5. Titulos agotados ---")
        if not titulos:
            print("El catálogo esta vacio.")
        else:
            agotados = False
            i = 0
            print("--- Títulos con stock 0 ---")
            while i < len(titulos):
                if ejemplares[i] == 0:
                    print(f"- {titulos[i]}")
                    gotados = True
                i += 1

            if not agotados:
                print("No hay titulos agotados")

    elif seleccion =="6":
        print("\n--- 6. Agregar nuevo titulo y ejemplares ---")
        nuevo_titulo = input("Ingrese el nuevo titulo").strip()
        if nuevo_titulo == "":
            print("El titulo no puede estar vacio")
        else:
            titulo_normalizado = nuevo_titulo.lower()
            es_duplicado = False
            i = 0
            while i < len(titulos):
                if titulos[i].lower() == titulo_normalizado:
                    es_duplicado = True
                    break
                i += 1
                
            if es_duplicado:
                print(f"El titulo '{nuevo_titulo}' ya existe en el catalogo.")
            else:
                cant_valida = False
                nueva_cantidad = 0
                while not cant_valida:
                    ejemplares_str = input("Ingrese la cantidad inicial de ejemplares (>= 0)").strip()
                    if ejemplares_str.isdigit() and int(ejemplares_str) >= 0:
                        nueva_cantidad = int(ejemplares_str)
                        cant_valida = True
                    else:
                        print("Cantidad inválida. Intente de nuevo.")
                        
                titulos.append(nuevo_titulo)
                ejemplares.append(nueva_cantidad)
                print(f"Título '{nuevo_titulo}' agregado con {nueva_cantidad} ejemplares.")
                
    elif seleccion =="7":
        print("\n--- 7. Actualizar Ejemplares (Prestamo/Devolución) ---")
        if not titulos:
            print("El catalogo esta vacio.")
        else:
            busqueda = input("Ingrese el titulo del libro para actualizar:").strip()
            indice_encontrado = -1
            busqueda_normalizada = busqueda.lower()
            i = 0
            while i < len(titulos):
                if titulos[i].lower() == busqueda_normalizada:
                    indice_encontrado = i
                    break
                i += 1

            if indice_encontrado == -1:
                print(f"Titulo'{busqueda}'no encontrado.")
            else:
                print(f"\nLibro: '{titulos[indice_encontrado]}'Stock actual:{ejemplares[indice_encontrado]}")
                print("¿Que desea realizar?")
                print("P-Prestamo (disminuye en 1)")
                print("D-Devolución (aumenta en 1)")
                
                hacer = input("Ingrese 'P' o 'D': ").strip().upper()

                if hacer== 'P':
                    if ejemplares[indice_encontrado] > 0:
                        ejemplares[indice_encontrado] -= 1 
                        print(f"Préstamo registrado para '{titulos[indice_encontrado]}'.Nuevo stock:{ejemplares[indice_encontrado]}")
                    else:
                        print(f"Prestamo no valido. Stock de'{titulos[indice_encontrado]}'esta agotado.")
                
                elif hacer == 'D':3
                    ejemplares[indice_encontrado] += 1 
                    print(f"Devolución registrada para '{titulos[indice_encontrado]}'.Nuevo stock:{ejemplares[indice_encontrado]}")
                    
                else:
                    print("Opción de acción inválida. Solo se permite 'P' o 'D'.")
else:
    print("Opción invalida. Ingrese un número del 1 al 8.")