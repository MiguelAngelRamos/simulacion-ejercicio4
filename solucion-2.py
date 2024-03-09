def tiene_longitud_suficiente(id_usuario):
    return len(id_usuario) >=8

def tiene_masyuscula(id_usuario):
    return any(c.isupper() for c in id_usuario)

def tiene_minuscula(id_usuario):
    return any(c.islower() for c in id_usuario)

def tiene_numero(id_usuario):
    return any(c.isdigit() for c in id_usuario)


def evaluar_criterios(id_usuario):
    criterios = {
        "longitud suficiente": tiene_longitud_suficiente,
        "al menos una mayúscula": tiene_masyuscula,
        "al menos una minúscula": tiene_minuscula,
        "al menos un número": tiene_numero,
    }

    faltantes = []

    for descripcion, funcion in criterios.items():
        if not funcion(id_usuario):
            faltantes.append(descripcion)
    return faltantes

def main():
    print("Crea un id de usuario para video juegos, debe contener al menos 8 caracteres, incluir mayúsculas, minúsculas y digitos")
    id_usuario = ""
    while True:
        char = input("Ingrese un caracter: ")
        # id_usuario = id_usuario + char
        id_usuario += char
        criterios_faltantes = evaluar_criterios(id_usuario)
        if not criterios_faltantes:
            print("!Excelente! tu Id de usuario es seguro y ha sido creado con exito!")
            print(id_usuario)
            break
        else:
            print(f"Criterios faltantes para un ID seguro: {', '.join(criterios_faltantes)}")
          
            # Criterios faltantes para un ID seguro: al menos 8 caracteres una letra mayuscula un número

if __name__ == "__main__":
    main()