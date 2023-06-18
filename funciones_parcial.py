import json
import re

#1
def cargar_pokemones(nombre_archivo) -> list:
      
    '''
    Lee un archivo CSV con información de Pokemones y retorna una lista de diccionarios
    con los datos de cada uno.
    
    Retorna: lista de diccionarios, donde cada diccionario representa un Pokemon y contiene las 
    siguientes claves: N° Pokedex, Nombre, Tipo, Poder de Ataque, Poder de Defensa y Habilidades.
    '''
    

    pokemones = []

    with open(nombre_archivo, 'r') as archivo:
        # Leer todas las líneas del archivo y almacenarlas en una lista
        lineas_archivo = archivo.readlines()

        # Saltamos la primera línea del archivo, que contiene los encabezados de las columnas
        encabezados = lineas_archivo[0].strip().split(',')

        # Procesamos cada línea del archivo y la agregamos a la lista de pokemones
        for linea in lineas_archivo[1:]:
            # Dividimos la línea en una lista de valores
            valores = linea.strip().split(',')

            # Creamos un diccionario para almacenar los datos del Pokémon
            pokemon = {}
            # Recorremos los valores en la línea del archivo y los agregamos al diccionario
            for i in range(len(valores)):
                clave = encabezados[i]
                valor = valores[i]
                # Agregamos los valores de tipo y habilidades a una lista
                if clave == "Habilidades":
                    # Si la clave ya existe, agregamos el valor a la lista existente
                    if clave in pokemon:
                        pokemon[clave].append(valor)
                    # Si la clave no existe, creamos una lista vacía y agregamos el valor
                    else:
                        pokemon[clave] = [valor]
                else:
                    pokemon[clave] = valor

            # Agregamos el diccionario a la lista de pokemones
            pokemones.append(pokemon)

    return pokemones

#2
def listar_cantidad_pokemon_por_tipo(pokemones):
    '''
    Brief: la funcion muestra la cantidad de pokemones por tipo.
    Parametros:
    -pokemones: Una lista de diccionarios de pokémones. Cada diccionario representa un pokémon y tiene una clave
    llamada 'Tipo' que contiene una cadena de texto con uno o varios tipos separados por '/'.
    '''
    # Diccionario para almacenar la cantidad de pokemones por tipo
    cantidad_por_tipo = {}
    
    # Se itera sobre la lista de pokemones para contar la cantidad de pokemones por tipo
    for pokemon in pokemones:
        # Se verifica si el tipo del pokemon ya se encuentra en el diccionario
        if pokemon['Tipo'] in cantidad_por_tipo:
            cantidad_por_tipo[pokemon['Tipo']] += 1
            tipos = pokemon.get('Tipo', '').split('/')
            for tipo in tipos:
                if tipo in cantidad_por_tipo:
                    cantidad_por_tipo[tipo] += 1
                else:
                    cantidad_por_tipo[tipo] = 1
        else:
            cantidad_por_tipo[pokemon['Tipo']] = 1
    
    # Se muestra la cantidad de pokemones por tipo
    print("Cantidad de pokemones por tipo:")
    for tipo, cantidad in cantidad_por_tipo.items():
        print(f"{tipo}: {cantidad}")

#3
def listar_pokemones_por_tipo(pokemones):
    '''
    Breve descripción: La función lista los pokémones por tipo, mostrando el nombre y el poder de ataque de cada pokémon
    que corresponde a ese tipo. 
    Parámetros:
    lista_pokemones: Una lista de diccionarios de pokémones. Cada diccionario representa un pokémon.
    Retorno:
    no retorna anda
    '''
    # Diccionario para almacenar los pokemones por tipo
    pokemones_por_tipo = {}
    
    # Se itera sobre la lista de pokemones para agrupar los pokemones por tipo
    for pokemon in pokemones:
        tipos = pokemon.get('Tipo', '').split('/')
        for tipo in tipos:
            if tipo in pokemones_por_tipo:
                pokemones_por_tipo[tipo].append(pokemon)
            else:
                pokemones_por_tipo[tipo] = [pokemon]
    
    # Se muestran los nombres y poderes de ataque de los pokemones por tipo
    for tipo, pokemones in pokemones_por_tipo.items(): #se usa item para retornar cada tupla contiene su clave y valor
        print(f"Ataque de los pokemones de tipo {tipo}:")
        print('*' * 80)
        for pokemon in pokemones:
            print(f"-{pokemon['Nombre']}({pokemon['Poder de Ataque']})")
        print('*' * 80)

#4
def listar_pokemones_por_habilidad(pokemones):
    '''
    Descripción: listar_pokemones_por_habilidad
    Parámetros:
    pokemones es una lista de diccionarios que contiene los datos de los pokemones
    Retorna: Esta función no retorna nada, simplemente imprime por pantalla los nombres, tipos y promedio
    de poder de los pokemones que tienen la habilidad indicada. Si no se encuentran pokemones con esa habilidad, 
    imprime un mensaje indicándolo.
    '''

    while True:
        # Se pide la habilidad deseada al usuario
        habilidad = input("Ingrese la habilidad que desea buscar: ").capitalize()

        # Lista para almacenar los pokemones con la habilidad buscada
        pokemones_con_habilidad = []

        # Se busca la habilidad en la lista de pokemones
        for pokemon in pokemones:
            habilidades = pokemon.get('Habilidades', [])
            for habilidad_pokemon in habilidades:
                if re.search(habilidad, habilidad_pokemon, flags=re.IGNORECASE):
                    pokemones_con_habilidad.append(pokemon)

        # Si se encontraron pokemones con la habilidad deseada, se muestran y se pregunta si se desea buscar otra habilidad
        if len(pokemones_con_habilidad) != 0:
            # Se muestra el nombre, tipo y promedio de poder entre ataque y defensa de los pokemones con la habilidad deseada
            print(f"Los pokemones con la habilidad '{habilidad}' son:")
            for pokemon in pokemones_con_habilidad:
                promedio_poder = (int(pokemon['Poder de Ataque']) + int(pokemon['Poder de Defensa'])) / 2
                print(f"Nombre: {pokemon['Nombre']}, Tipo: {str(pokemon['Tipo']).strip('[]')}, Promedio de poder: {promedio_poder}")

            # Se pregunta si se desea buscar otra habilidad
            while True:
                opcion = input("¿Desea buscar otra habilidad? (S/N): ").lower()
                if opcion == 'n':
                    return
                elif opcion == 's':
                    break
                else:
                    print("Opción inválida, por favor ingrese 'S' o 'N'.")
        else:
            print(f"No se encontraron pokemones con la habilidad '{habilidad}'.")

#5
def listar_pokemon_ordenados(pokemones):
    '''
    Descripción: listar_pokemon_ordenados
    Parámetros:
    pokemones es una lista de diccionarios que contiene los datos de los pokemones
    Retorna: La función retorna una lista de pokemones ordenados por su poder de ataque.
    En caso de que haya pokemones con el mismo poder de ataque, se ordenan alfabéticamente por nombre.
    '''
    # Ordenar la lista de pokemones
    for i in range(len(pokemones)-1):
        for j in range(i+1, len(pokemones)):
            if int(pokemones[i]['Poder de Ataque']) > int(pokemones[j]['Poder de Ataque']):
                pokemones[i], pokemones[j] = pokemones[j], pokemones[i]
                # Si los poderes de ataque son iguales, ordenar por nombre
            elif int(pokemones[i]['Poder de Ataque']) == int(pokemones[j]['Poder de Ataque']):
                if (pokemones[i]["Nombre"] > pokemones[j]["Nombre"]):
                    pokemones[i], pokemones[j] = pokemones[j], pokemones[i]

    # Retornar la lista de pokemones ordenados
    return pokemones

#5.1
def imprimir_pokemones_ordenados(lista_pokemones):
    '''
    Descripción: imprimir_pokemones_ordenados
    Parámetros:
    lista_pokemones es una lista de diccionarios que contiene los datos de los pokemones previamente ordenados
    Retorna: Esta función no retorna nada, simplemente imprime por pantalla los datos de los pokemones en el siguiente formato:
    "Nombre: {nombre}, Tipo: {tipo}, Poder de Ataque: {poder_ataque], Poder de Defensa: {poder_defensa}"
    '''
    for pokemon in lista_pokemones:
        print(f"Nombre: {pokemon['Nombre']}, Tipo: {str(pokemon['Tipo']).strip('[]')},"            
            f"Poder de Ataque: {pokemon['Poder de Ataque']}, Poder de Defensa: {pokemon['Poder de Defensa']}")

# 6
def crear_json(tipo, lista_pokemones):
    '''
    Descripción: crear_json
    Parámetros:
    tipo: es el tipo de pokemon que se desea filtrar
    lista_pokemones: es una lista de diccionarios que contiene los datos de los pokemones
    Retorna: La función retorna el nombre del archivo JSON generado.
    La función proporciona una forma conveniente de filtrar los pokemones por tipo
    y almacenar sus datos relevantes en un archivo JSON para su posterior procesamiento o análisis.
    '''
    while True:
        # Cargar los pokemones del archivo
        pokemones = lista_pokemones 

        # Crear una lista con los pokemones del tipo especificado
        pokemones_filtrados = []
        for pokemon in pokemones:
            if tipo in pokemon["Tipo"]:
                pokemones_filtrados.append(pokemon)

        if len(pokemones_filtrados) == 0:
            print(f"No se encontraron pokemones del tipo {tipo}. Intente de nuevo.")
            break
        else:
            print('Se creo correctamente el archivo Json')
            break

    # Crear un diccionario para guardar los datos de los pokemones
    datos_pokemones = {}

    # Iterar por los pokemones filtrados y guardar los datos en el diccionario
    for pokemon in pokemones_filtrados:
        nombre = pokemon["Nombre"]
        poder_ataque = int(pokemon["Poder de Ataque"])
        poder_defensa = int(pokemon["Poder de Defensa"])

        if poder_ataque > poder_defensa:
            poder_max = poder_ataque
            tipo_poder = "Ataque"
        elif poder_defensa > poder_ataque:
            poder_max = poder_defensa
            tipo_poder = "Defensa"
        else:
            poder_max = poder_ataque
            tipo_poder = "Ambos"

        datos_pokemones[nombre] = {
            "Tipo del pokemon": nombre,
            "Poder maximo": poder_max,
            "Tipo de poder maximo": tipo_poder
        }
    
    # Generar un archivo JSON
    nombre_archivo = tipo.replace("/", "_")
    with open(f"{nombre_archivo}.json", "w", encoding='utf-8') as archivo:
        json.dump(datos_pokemones, archivo, indent = 4, ensure_ascii = False)
        '''
        Cuando se establece en False, los caracteres no ASCII se escriben sin escapar,
        lo que permite que se muestren correctamente en la salida del archivo JSON.
        '''
    
    return nombre_archivo # Retornar el nombre del archivo generado

#7
def leer_json(nombre_archivo):
    '''
    Descripción: leer_json
    Parámetros:
    nombre_archivo es el nombre del archivo JSON que se desea leer
    Retorna: La función retorna un diccionario que contiene los datos del archivo JSON para asi luego
    printearlo en el menu
    '''
    nombre_archivo = input("Indique el nombre del archivo JSON a leer: ")
    if "." not in nombre_archivo:
        nombre_archivo += ".json"
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        datos_pokemones = json.load(archivo)
    return datos_pokemones