from funciones_parcial import *
from agregado_parcial import *

#9
def imprimir_menu():
    print('''1 - Mostrar los datos traidos desde el archivo
2 - Mostrar cantidad de pokemons por tipo
3 - Listar pokemons por tipo
4 - Listar pokemons por habilidad
5 - Listar todos los pokemon por orden de 'poder de ataque'
6 - Crear archivo JSON segun el tipo que quiera con sus respectivos pokemons
7 - Mostrar el archivo JSON por pantalla
8 - Agregar pokemon nuevo
9 - salir''')

#9.1
def pokemon_menu_principal():
    imprimir_menu()
    respuesta = input("Ingrese una opción: ")
    return respuesta

#9.2
def pokemon_app():
    lista_pokemones_aprobada = False
    while True:
        respuesta = pokemon_menu_principal()
        match respuesta:
            case '1':
                lista_pokemones = cargar_pokemones('pokemones.csv')
                print("Se han cargado todos los pokemones.")
                lista_pokemones_aprobada= True
            case '2':
                if lista_pokemones_aprobada:
                    listar_cantidad_pokemon_por_tipo(lista_pokemones)
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")   
            case '3':
                if lista_pokemones_aprobada:
                    listar_pokemones_por_tipo(lista_pokemones)
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")
            case '4':
                if lista_pokemones_aprobada:
                    listar_pokemones_por_habilidad(lista_pokemones)
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")
            case '5':
                if lista_pokemones_aprobada:
                    pokemones_ordenados = listar_pokemon_ordenados(lista_pokemones)
                    imprimir_pokemones_ordenados(pokemones_ordenados)
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")
            case '6':
                if lista_pokemones_aprobada:
                    tipo_pokemon = input('Indique el tipo de pokemon que desea crear en el archivo JSON: ').capitalize()
                    crear_json(tipo_pokemon, lista_pokemones)                  
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")
            case '7':
                if lista_pokemones_aprobada:
                    nombre_archivo = crear_json(tipo_pokemon, lista_pokemones)   
                    datos_pokemones = leer_json(nombre_archivo)
                    print(json.dumps(datos_pokemones, indent=4, ensure_ascii = False))
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")
            case '8':
                if lista_pokemones_aprobada:
                    nuevo_pokemon = agregar_pokemon(lista_pokemones)
                    if nuevo_pokemon != None:
                        guardar_pokemon_en_csv(nuevo_pokemon, 'pokemones.csv')
                    else:
                        print("Error al querer crear un pokemon nuevo")
                else:
                    print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 primero")
            case '9':
                break