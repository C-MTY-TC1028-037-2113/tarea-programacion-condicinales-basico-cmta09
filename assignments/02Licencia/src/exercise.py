
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if edad >=18:
        id = input("¿Tienes identificación oficial? (s/n): ").upper()
        if id == "S":
            print("Trámite de licencia concedido")
        elif id == "N":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif edad<18 and edad>0:
        print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

if __name__ == '__main__':
    main()
