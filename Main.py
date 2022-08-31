# Para hacer graficos
import matplotlib.pyplot as plt
import numpy as np
# Para alelatoriedad
from random import sample

def plot(correctas, titulo, promedio):
    legends =['correctas', 'promedio']
    fig, ax = plt.subplots()
    ax.plot(correctas.keys(),correctas.values(), color='green')
    ax.set(xlabel='Intentos', ylabel='Nota',
           title='Prueba de Pruebas ' + titulo)
    plt.axhline(y=promedio)
    ax.legend(legends)
    ax.grid()
    plt.show()

def prueba(preguntas, opciones):
    respuestas = []
    for i in range(0, preguntas):
            respuestas.append(sample(opciones, 1))
    return respuestas

def intento(preguntas, opciones, repetir):
    correctas = {}
    promedioFinal = 0
    for i in range(0, int(repetir)):
        intentos = []
        correctas[i] = 0
        respuestas = prueba(preguntas, opciones)
        for k in range(0, preguntas):
            intentos.append(sample(opciones, 1))
            if intentos[k] == respuestas[k]:
                correctas[i] += 1
        promedioFinal += correctas[i]
    promedioFinal = promedioFinal/ int(repetir)
    print(promedioFinal)
    return plot(correctas, "Alelatorio", promedioFinal)

def intentoA(preguntas, opciones, repetir):
    correctas = {}
    promedioFinal = 0
    for i in range(0, int(repetir)):
        intentos = []
        correctas[i] = 0
        respuestas = prueba(preguntas, opciones)
        for k in range(0, preguntas):
            intentos.append([1])
            if intentos[k] == respuestas[k]:
                correctas[i] += 1
        promedioFinal += correctas[i]
    promedioFinal = promedioFinal/ int(repetir)
    print(promedioFinal)
    return plot(correctas, "todas A", promedioFinal)

(intentoA(10, [1,2,3,4], input("cantidad de veces que hacerlo tirando siempre A: ")))
(intento(10, [1,2,3,4], input("cantidad de veces que hacerlo tirando alelatorio: ")))