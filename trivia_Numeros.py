datosTrivia = {
    1: {
        "pregunta": "2*2*2",
        "respuesta": 8
    },
    2: {
        "pregunta": "5+6+7",
        "respuesta": 18
    },
    3: {
        "pregunta": "(2+2)+5*2",
        "respuesta": 14
    },
    4: {
        "pregunta": "95-15*2-30",
        "respuesta": 35
    },
    5: {
        "pregunta": "50/2+6/2-5",
        "respuesta": 23
    }
}

def trivia_fetch(num):
    if num in datosTrivia:
        return datosTrivia[num]
    else:
        print("Error: Información no encontrada.")

def main():
    print("""¡Bienvenidos a la Trivia!
          Tienes la posibilidad de contestar cualquiera de las 5 opciones siguientes:
          1. 2*2*2 =
          2. 5+6+7 = 
          3. (2+2)+5*2 = 
          4. 95-15*2-30 = 
          5. 50/2+6/2-5 = 
          """)
    while True:
        try:
            num = int(input("Escriba el número de la pregunta que le gustaría responder. Digite '0' para salir: "))
            if num == 0:
                break
            pregunta = trivia_fetch(num)["pregunta"]
            print(f"Pregunta: {pregunta}")
            respuesta_usuario = int(input("La respuesta es: "))
            respuesta_correcta = trivia_fetch(num)["respuesta"]
            if respuesta_usuario == respuesta_correcta:
                print("¡Le has acertado!")
            else:
                print("Te has equivocado. La respuesta correcta es:", respuesta_correcta)
        except ValueError:
            print("Error. Digite un número del 1 al 5. Para salir escriba '0'.")

if __name__ == "__main__":
    main()
