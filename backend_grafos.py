#Librerias estandar
import sys
import random
#Se intenta importar las librerias que no son estandar del lenguaje de programacion de Python 3
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
    
    plt.close()
    #CREAMOS LA ESTRUCTURA DEL GRAFO
    G = nx.DiGraph()
    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
            if(matriz[x, y] == 0):#Si el peso entre nodos es cero, se procede a no graficar la arista
                pass
            elif(matriz[x, y] <= 20):#Si el peso entre los nodos es muy pequeños, para visualizarlo de mejor manera se le cambia el color a azul y se aumenta el grosor de su arista
                G.add_edge(x, y, weight = (matriz[x, y])* 0.08, color = "blue")
            elif(matriz[x, y] >= 500):#Si el peso entre los nodos es mayor a 500, se resaltara este visualmente su arista con el color rojo
                G.add_edge(x, y, weight = (matriz[x, y])* edgeSize, color = "red")
            else:
                G.add_edge(x, y, weight = (matriz[x, y])* edgeSize, color = "black")

    plt.figure(figsize = (10, 10))        
    plt.title("Grafo")    
    colorEdges = nx.get_edge_attributes(G,'color').values()
    weights = nx.get_edge_attributes(G,'weight').values()
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=False, node_size = nodeSize,
        node_color = colorNodes, edge_color = colorEdges,
        width=list(weights), connectionstyle ='arc3, rad = 0.70')
    nx.draw_networkx_labels(G, pos, labelsPercents, font_size = 6)
    plt.show(block=False)

def graficarPrompting():
    plt.close()
    plt.figure(figsize = (10, 10))       
    plt.xlabel("Tiempo[Minutos]")
    plt.ylabel("Prompting")
    plt.title("Grafico Prompting")
    number = 0
    for i in listaPromptingFinal:
        plt.plot(i,color=colorNodes[number][0],label ='Node '+str(number))
        number += 1
    plt.legend(loc='upper right',fontsize = fontSize)
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
            labelsPercents[i] = labelsPercentsNamesNodes + str(i) + "\n(" + str(round((listaPesos[i]/sum(listaPesos))*100)) +"%)"    

def numberOfNodes(contenedor):
    global nodeSize
    global edgeSize
    global labelsPercentsNamesNodes
    global connectionstyleRad
    global fontSize

    nodes = []
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        if int(aux[2]) not in nodes:
            nodes.append(int(aux[2]))   
        
    for i in range(len(nodes)):
        listaPromptingFinal.append([])   
    
    if(len(nodes) > 25):
        nodeSize = 400
        fontSize = 6.7
        edgeSize = 0.0005
        labelsPercentsNamesNodes = ""
    else:
        nodeSize = 1000
        edgeSize = 0.003
        fontSize = 10
        labelsPercentsNamesNodes = "Usuario " 
  
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
    
def click():
    graficarPrompting()

def click2():
    graficarGrafo(matrizPesos)

#Variables Globales
colorNodes = []
labelsPercents = {}#Diccionarioa que guardara los porcentajes finales de cada nodo para el grafo
listaContador = [] #lista que contiene el peso de los nodos al final de toda la comunicación 
matrizPesos = [] #matriz que contiene el peso de los vectores
listaPromptingFinal = []
labelsPercentsNamesNodes = ""
nodeNumbers = 0
nodeSize = 0
edgeSize = 0
fontSize = 0
#---------------------------------------------AGREGAR DINAMISMO EN LAS GRAFICAS
