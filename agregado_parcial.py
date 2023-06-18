#8 agregado
import re

#8 agregado
def agregar_pokemon(lista_pokemones):
    pokedex = input("Ingrese el número de la Pokédex del pokémon que quiere agregar: ")

    while not re.match(r'^\d{3}$', pokedex):
        print("Error: el número de Pokédex debe contener exactamente 3 dígitos.")
        pokedex = input("Ingrese el número de la Pokédex del pokémon que quiere agregar: ")

    # Verificar si el Pokémon ya existe en la lista
    pokemon_existente = False
    for pokemon in lista_pokemones:
        if pokemon["N° Pokedex"] == pokedex:
            pokemon_existente = True
            break

    if pokemon_existente:
        print("Error: el Pokémon ya existe en la lista.")
        return None

    nombre = input("Ingrese el nombre del pokemon que quiere agregar: ").capitalize()
    # Sustituir caracteres no deseados en el nombre del pokemon
    nombre = re.sub(r'[^a-zA-Z0-9\s]', '', nombre).capitalize()
    for pokemon in lista_pokemones:
        if pokemon['Nombre'] == nombre:
            print("Error: el Pokémon ya existe en la lista.")
            return None
        
    tipos_existentes = set(map(lambda pokemon: pokemon["Tipo"], lista_pokemones))
    tipo = input("Ingrese el tipo del pokemon que quiere agregar: ").capitalize()
    while tipo not in tipos_existentes:
        print("Error: el tipo ingresado no es válido.")
        tipo = input("Ingrese el tipo del Pokémon que quiere agregar: ").capitalize()

    poder_ataque = input("Ingrese el poder de ataque del pokemon que quiere agregar: ")
    while not poder_ataque.isdigit():
        print("Error: debe ingresar un valor numérico.")
        poder_ataque = input("Ingrese el poder de ataque del pokemon que quiere agregar: ")

    poder_defensa = input("Ingrese el poder de defensa que quiere agregar: ")
    while not poder_defensa.isdigit():
        print("Error: debe ingresar un valor numérico.")
        poder_defensa = input("Ingrese el poder de defensa que quiere agregar: ")

    habilidades = input("Ingrese las habilidades del pokemon que quiere agregar: ").split(',')

    nuevo_pokemon = {
        "N° Pokedex": pokedex,
        "Nombre": nombre,
        "Tipo": tipo,
        "Poder de Ataque": poder_ataque,
        "Poder de Defensa": poder_defensa,
        "Habilidades": habilidades
    }

    lista_pokemones.append(nuevo_pokemon)

    print("Nuevo pokemon agregado exitosamente.")
    return nuevo_pokemon

#8.1 agregado
def guardar_pokemon_en_csv(pokemon, path):
    with open(path, mode="a", newline="", encoding="UTF-8") as archivo_csv:
        habilidades_str = ', '.join(pokemon["Habilidades"])
        fila = f'{pokemon["N° Pokedex"]},{pokemon["Nombre"]},{pokemon["Tipo"]},{pokemon["Poder de Ataque"]},{pokemon["Poder de Defensa"]},{habilidades_str}\n'
        archivo_csv.write(fila)

    print("Los datos del pokemon se han guardado en el archivo CSV.")