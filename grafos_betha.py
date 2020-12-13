#Librerias estandar
import sys
import random
#Se intenta importar las librerias que no son estandar del lenguaje de programaciond e Python 3
try:
    # importing numpy
    import numpy as np
    # importing networkx  
    import networkx as nx 
    # importing matplotlib.pyplot 
    import matplotlib.pyplot as plt
    # importing tkinter for the GUI
    import tkinter
    
except:#Si no se logran importar, se procede a instalarlas en el sistema del usuario
    print("Error when importing necessary libraries  to make the program work, it will proceed to start the intallation of these\n")
    import subprocess
    subprocess.call(['pip', 'install', "-r","requeriments.txt"])
    print("Libraries were installed to execute the program\n")
    sys.exit("Please restart the program") 

def matrizAdyacencia_Prompting(matriz, contenedor):
    anterior = -1
    tiempoVentanas = 60
    tiempoReal = 0
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        listaContador[int(aux[2])] += 1 
        if(anterior == -1):
            anterior = int(aux[2])
        else:
            matriz[int(aux[2])][int(anterior)] += 1 
            anterior = int(aux[2])

        if( round(float(aux[3])) >= tiempoVentanas):
            tiempoVentanas += 60
            calcularPrompting(listaContador, 1, listaPromptingFinal)

        anterior = int(aux[2])
        tiempoReal = float(aux[3])

    if tiempoReal != tiempoVentanas:
        calcularPrompting(listaContador, 1, listaPromptingFinal)

def graficarGrafo(matriz):

    #CREAMOS LA ESTRUCTURA DEL GRAFO
    plt.close()
    G = nx.DiGraph()
    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
            G.add_edge(x, y, weight = (matriz[x, y])* 0.005, length = 0.1)

    plt.title("Grafo")    
    weights = nx.get_edge_attributes(G,'weight').values()
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=False, node_size=3400,
        node_color = colorNodes,
        width=list(weights), connectionstyle='arc3, rad = 0.13')
    nx.draw_networkx_labels(G, pos, labelsPercents, font_size=6)
    plt.show(block=False)

def graficarPrompting():
    plt.close()
    plt.xlabel("Tiempo[Minutos]")
    plt.ylabel("Prompting")
    plt.title("Grafico Prompting")
    number = 0
    for i in listaPromptingFinal:
        plt.plot(i,color=colorNodes[number][0],label='Node '+str(number))
        number += 1
    plt.legend(loc='upper right')
    plt.show(block=False)


def randomColor(nodeNumbers):
    arrayColors = ["green", "blue", "red", "magenta", "yellow"]
    if(nodeNumbers == len(arrayColors)):
        return arrayColors

    nodeColors = []
    for i in range(0, nodeNumbers):
        nodeColors.append(random.choice(arrayColors))
    return nodeColors

def calcularPrompting(listaPesos, option, listaPrompting): #debes darle una lista con los valores el peso de cada nodo, y devuelve el prompting de cada uno de los nodos en otro vector.
    
    for i in range(len(listaPesos)):
        if(option == 1 and listaPrompting != None):
            listaPrompting[i].append(listaPesos[i]/sum(listaPesos))
        elif(option == 2):
            labelsPercents[i] = "Usuario " + str(i) + " (" + str(round((listaPesos[i]/sum(listaPesos))*100)) +"%)"    

def numberOfNodes(contenedor):

    nodes = []
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        if int(aux[2]) not in nodes:
            nodes.append(int(aux[2]))   
        
    for i in range(len(nodes)):
        listaPromptingFinal.append([])   
  
    return len(nodes)

def main():
    global listaContador
    global colorNodes
    global matrizPesos 

    fileName = 'Grupo1-393371.csv'
    try:
        archivo = open(fileName, 'r')
        contenedor = archivo.readlines()
        archivo.close()
    except:
        sys.exit(f'Error file {fileName} not found.') 

    nodeNumbers = numberOfNodes(contenedor)
    colorNodes = randomColor(nodeNumbers)
    matrizPesos = np.zeros((nodeNumbers, nodeNumbers))
    listaContador = [0]*nodeNumbers
    matrizAdyacencia_Prompting(matrizPesos, contenedor)
    calcularPrompting(listaContador, 2, None)
    #print(labelsPercents, vector_contador, nodeNumbers)

def click():
    graficarPrompting()

def click2():
    graficarGrafo(matrizPesos)

#Variables Globales
colorNodes = []
labelsPercents = {}#Diccionarioa que guardara los porcentajes finales de cada nodo para el grafo
listaContador = [] #lista que contiene el peso de los nodos al final de toda la comunicación 
matrizPesos = [] #lista que contiene el peso de los vectores
#matriz_contador_time = [] #lista que contiene vectores con el peso de cada nodo a través del tiempo
listaPromptingFinal = []
nodeNumbers = 0
#---------------------------------------------AGREGAR DINAMISMO EN LAS GRAFICAS
