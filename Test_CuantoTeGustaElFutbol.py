titulo = "Bienvenido al test sobre tu fanatismo sobre el fútbol..."
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
separador = "\n" + "-" * len(titulo) + "\n"

nombre = input("Antes de empezar, ¿cómo te llamas?:\n"
               "Respuesta: ")
print(separador)
club = input("¡Excelente, hola " + nombre + "! ¿De qué club sos hincha?\n"
             "Respuesta: ")
print(separador)

print("Asi que de " + club + ", ¿eh?. ¡Bien, empecemos!\n"
                             + separador)

puntuacion = 0

print("Pregunta 1: ¿Qué tan seguido ves los partidos de tu equipo?")
pregunta1 = input("A - Siempre, no me pierdo ninguno.\n"
                  "B - Intento verlos, pero tengo mejores cosas que hacer.\n"
                  "C - La verdad es que no le doy mayor importancia.\n"
                  "Respuesta: ")

if pregunta1 == "A":
    puntuacion = 10
elif pregunta1 == "B":
    puntuacion = 5
elif pregunta1 == "C":
    puntuacion = 0
else:
    print("Las respuestas posibles son A, B o C")
    exit()

print(separador)
print("¡Bien, pasemos a la siguiente...")
print(separador)

print("Pregunta 2: ¿Qué tan seguido vas a la cancha?")
pregunta2 = input("A - Siempre, sigo a mi equipo a todas partes.\n"
                  "B - A veces, sobre todo si son partidos importantes.\n"
                  "C - Nada como casa o disfrutar otras cosas.\n"
                  "Respuesta: ")

if pregunta2 == "A":
    puntuacion += 10
elif pregunta2 == "B":
    puntuacion += 5
elif pregunta2 == "C":
    puntuacion += 0
else:
    print('Las respuestas posibles son A, B o C')
    exit()

print(separador)
print("¡Última pregunta! Aquí va:")
print(separador)

print("Pregunta 3: Qué tan seguido compras indumentaria o merchandising de " + club + " ?")
pregunta3 = input("A - Siempre intento comprar algo... la última camiseta.\n"
                  "B - Tengo alguna que otra cosa, pero tampoco me vuelvo loco.\n"
                  "C - ¿Gastarme el sueldo en eso? Ni de broma.\n"
                  "Respuesta: ")

if pregunta3 == "A":
    puntuacion += 10
elif pregunta3 == "B":
    puntuacion += 5
elif pregunta3 == "C":
    puntuacion += 0
else:
    print("Las respuestas posibles son A, B o C")
    exit()

print(separador)
print("¡Hora del resultado...!\n"
      "Tu puntuación fue de {} puntos.".format(puntuacion))

if puntuacion >= 25:
    print(nombre + ", ¡sos un verdadero hincha que sigue a " + club + " como solo algunos entenderían!")
elif puntuacion >= 15:
    print(nombre + ", entendemos que tengas mejores aficiones, no todo puede ser " + club + ", ¡pero la verdad es que eres más fan de lo que crees!")
else:
    print(nombre + ", en el mundo hay más que fútbol y pasión por la pelotita... Estamos seguros que no te sentirás mal por " + club + ".")

print(separador)
print("Esperamos que te haya gustado el test. ¡Hasta la próxima!")