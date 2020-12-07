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
except:#Si no se logran importar, se procede a instalarlas en el sistema del usuario
    print("Error when importing necessary libraries  to make the program work, it will proceed to start the intallation of these\n")
    import subprocess
    subprocess.call(['pip', 'install', "-r","requeriments.txt"])
    print("Libraries were installed to execute the program\n")
    sys.exit("Please restart the program") 

def matrizAdyacencia_Prompting(matriz, contenedor):
    anterior = -1
    tiempoVentanas = 60
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        vector_contador[int(aux[2])] += 1 
        if(anterior == -1):
            anterior = int(aux[2])
        else:
            matriz[int(aux[2])][int(anterior)] += 1 
            anterior = int(aux[2])

        if( round(float(aux[3])) >= tiempoVentanas):
            tiempoVentanas += 60
            matriz_contador_time.append(list(np.copy(vector_contador)))

        anterior = int(aux[2])

    if matriz_contador_time[-1] != vector_contador:
        matriz_contador_time.append(list(np.copy(vector_contador)))

def graficarGrafo(matriz):
    global color_nodes

    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
            G.add_edge(x, y, weight = (matriz[x, y])* 0.005, length = 0.1)

    print(f'{matriz} \n') 
    plt.title("Grafo") 
    color_nodes = randomColor(color_map, G.number_of_nodes())     
    weights = nx.get_edge_attributes(G,'weight').values()
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=False, node_size=3400,
        node_color = color_nodes,
        width=list(weights), connectionstyle='arc3, rad = 0.13')
    nx.draw_networkx_labels(G, pos, labelsPercents, font_size=6)
    plt.show(block=False)
    plt.pause(5)
    plt.close()

def graficarPrompting():
    listaMaestra = []
    for i in range(nodeNumbers):
        listaMaestra.append([])

    for i in matriz_contador_time:
        calcular_prompting(i, 1, listaMaestra)

    plt.xlabel("Tiempo[Minutos]")
    plt.ylabel("Prompting")
    plt.title("Grafico Prompting")
    number = 0

    for i in listaMaestra:
        plt.plot(i,color=color_nodes[number][0],label='Node '+str(number))
        number += 1
    plt.legend(loc='upper right')
    plt.show(block=False)
    plt.pause(5)
    plt.close()

def randomColor(arrayColors, nodeNumbers):
    if(nodeNumbers == len(arrayColors)):
        return arrayColors

    nodeColors = []
    for i in range(0, nodeNumbers):
        nodeColors.append(random.choice(arrayColors))
    return nodeColors

def calcular_prompting(vector, option, listaPrompting): #debes darle un vector con los valores el peso de cada nodo, y devuelve el prompting de cada uno de los nodos en otro vector.
    global labelsPercents
    matriz_prompting = []
    for i in range(len(vector)):
        if(option == 1 and listaPrompting != None):
            listaPrompting[i].append(vector[i]/sum(vector))
        elif(option == 2):
            matriz_prompting.append(vector[i]/sum(vector))
            labelsPercents[i] = "Usuario " + str(i) + " (" + str(round((matriz_prompting[i])*100)) +"%)"    

def numberOfNodes(contenedor):
    nodes = []
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        if int(aux[2]) not in nodes:
            nodes.append(int(aux[2]))      
    return len(nodes)

def main():
    global vector_contador
    global nodeNumbers
    fileName = 'Grupo1-393371.csv'
    try:
        archivo = open(fileName, 'r')
        contenedor = archivo.readlines()
        archivo.close()
        nodeNumbers = numberOfNodes(contenedor)
    except:
        sys.exit(f'Error file {fileName} not found.')  
     
    matriz= np.zeros((nodeNumbers, nodeNumbers))
    vector_contador = [0]*nodeNumbers
    matrizAdyacencia_Prompting(matriz, contenedor)
    calcular_prompting(vector_contador, 2, None)
    graficarGrafo(matriz)
    graficarPrompting()
    print(labelsPercents)

#Variables Globales
#CREAMOS LA ESTRUCTURA DEL GRAFO
G = nx.DiGraph()
#---------------
color_map = ["green", "blue", "red", "magenta", "yellow"]
color_nodes = []
labelsPercents = {}#Diccionarioa que guardara los porcentajes finales de cada nodo para el grafo
matriz_timestamp = [] #guarda el peso de los vectores a través del tiempo 
vector_contador = [] #lista que contiene el peso de los vectoes al final de toda la comunicación 
matriz_contador_time = [] #lista que contiene vectores con el peso de cada nodo a través del tiempo
nodeNumbers = 0
#---------------------------------------------AGREGAR DINAMISMO EN LAS GRAFICAS
main()