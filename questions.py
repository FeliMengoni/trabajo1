import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Lista de indices
ind = [int(0), int(1), int(2), int(3), int(4)]
puntos = 0
num = random.sample(ind, k=3)  
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    print(_)
    # Guardamos todas las listas en una sola, ordenada por indices
    conjunto = list(zip(questions, answers, correct_answers_index))
    # Guardamos los elementos de manera aleatoria en una variable
    test = conjunto[num[_]]
    que = test[0]
    ans = test[1]
    cor = test[2]
    # Se muestra la pregunta y las respuestas posibles
    print(que)
    for i, ans in enumerate(ans):
        print(f"{i + 1}. {ans}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Verificamos si ingreso un numero o caracteres 
        if user_answer.isdigit():
            user_answer = int(user_answer) - 1
            # Se verifica si la respuesta es correcta
            if user_answer == cor:
                print("¡Correcto!")
                puntos = puntos + 1
                break
            # Si no es valido el numero se sale del programa
            if user_answer < 0 or user_answer > 3:
                print("Respuesta no valida")
                sys.exit(1)
            puntos = puntos - 0.5
        else:
            print("Respuesta no valida")
            sys.exit(1)
    else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(ans, cor)
    # Se imprime un blanco al final de la pregunta
print()
print("---------------")
print("Puntuacion final: ", puntos, "!!!")
