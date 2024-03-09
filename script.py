#Aquí se debe definir la función
def validar_identificador(id_usuario):
    criterios = {
        "longitud": len(id_usuario) >=8,
        "mayuscula": any(c.isupper() for c in id_usuario),
        "minuscula": any(c.islower() for c in id_usuario),
        "numero": any(c.isdigit() for c in id_usuario)
    }
    return criterios

def criterios_faltantes(criterios):
    mensajes = []
    if not criterios["longitud"]:
        mensajes.append("al menos 8 caracteres")
    if not criterios["mayuscula"]:
        mensajes.append("una letra mayuscula")
    if not criterios["minuscula"]:
        mensajes.append("una letra minúscula")
    if not criterios["numero"]:
        mensajes.append("un número")

    return ", ".join(mensajes) # "al menos 8 caracteres una letra mayuscula un número"



def main():
    print("Crea un id de usuario para video juegos, debe contener al menos 8 caracteres, incluir mayúsculas, minúsculas y digitos")
    id_usuario = ""
    while True:
        char = input("Ingrese un caracter: ")
        # id_usuario = id_usuario + char
        id_usuario += char
        criterios = validar_identificador(id_usuario)
        if all(criterios.values()):
            print("!Excelente el Id usuario es seguro!")
            print(f"El ID es: {id_usuario}")
            break
        else:
            faltantes = criterios_faltantes(criterios)
            print(f"Criterios faltantes para un ID seguro: {faltantes}")
          
            # Criterios faltantes para un ID seguro: al menos 8 caracteres una letra mayuscula un número

if __name__ == "__main__":
    main()