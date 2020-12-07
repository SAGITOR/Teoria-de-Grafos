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

<<<<<<< HEAD
def matrizAdyacencia_Prompting(matriz, contenedor):
=======
#variables globales.

def rellenarMatrizDeAdyacencia(matriz, contenedor):
>>>>>>> 2ce219e0adbb5012766c4a70a319f0d0af1a90ec
    anterior = 0
    tiempoVentanas = 60
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        vector_contador[int(aux[2])] += 1 
        if(a % 2 == 0):
            matriz[int(anterior)][int(aux[2])] += 1 
            
        if( round(float(aux[3])) >= tiempoVentanas and a % 2 != 0):
<<<<<<< HEAD
            #print(f'Tiempo conversacion real:{round(float(aux[3]))} || Tiempo a comparar: {tiempoVentanas}')
            tiempoVentanas += 60
            matriz_contador_time.append(list(np.copy(vector_contador)))

        anterior = int(aux[2])

    if matriz_contador_time[-1] != vector_contador:
        matriz_contador_time.append(np.copy(vector_contador))

def graficarGrafo(matriz):
    
    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
            G.add_edge(x, y, weight = (matriz[x, y])* 0.01, length = 0.1)
=======
            print(f'Tiempo conversacion real:{round(float(aux[3]))} || Tiempo a comparar: {tiempoVentanas}')
            tiempoVentanas += 60
            matriz_timestamp.append(np.copy(matriz))
            
        anterior = int(aux[2])
    matriz_timestamp.append(np.copy(matriz))
    graficarGrafo(matriz)
    return matriz

def graficarGrafo(matriz):
    labels = {}
    labels[0] = r"$Usuario 1$"
    labels[1] = r"$Usuario 2$"
    labels[2] = r"$Usuario 3$"
    labels[3] = r"$Usuario 4$"
    labels[4] = r"$Usuario 5$"
    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
           G.add_edge(x, y, weight = (matriz[x, y])* 0.01, length = 0.1)
>>>>>>> 2ce219e0adbb5012766c4a70a319f0d0af1a90ec

    print(f'{matriz} \n')       
    weights = nx.get_edge_attributes(G,'weight').values()
    pos = nx.circular_layout(G)
<<<<<<< HEAD
    nx.draw(G, pos, with_labels=False, node_size=3400,
        node_color = randomColor(color_map, G.number_of_nodes()),
        width=list(weights), connectionstyle='arc3, rad = 0.13')
    nx.draw_networkx_labels(G, pos, labelsPercents, font_size=6)
=======
    color_map = ["green", "blue", "red", "orange", "purple"]
    nx.draw(G, pos, with_labels=False, node_size=3400, font_size=20,
    node_color=color_map, width=list(weights), connectionstyle='arc3, rad = 0.13')
    nx.draw_networkx_labels(G, pos, labels, font_size=12)
>>>>>>> 2ce219e0adbb5012766c4a70a319f0d0af1a90ec
    plt.show(block=False)
    plt.pause(5)
    plt.close()

<<<<<<< HEAD
def randomColor(arrayColors, nodeNumbers):
    if(nodeNumbers == len(arrayColors)):
        return arrayColors
        
    nodeColors = []
    for i in range(0, nodeNumbers):
        nodeColors.append(random.choice(arrayColors))
    return nodeColors

def calcular_prompting(vector, labelsPercents): #debes darle un vector con los valores el peso de cada nodo, y devuelve el prompting de cada uno de los nodos en otro vector.
    matriz_prompting = []
    for i in range(len(vector)):
        matriz_prompting.append(vector[i]/sum(vector))
        labelsPercents[i] = "Usuario " + str(i + 1) + " (" + str(round((matriz_prompting[i])*100)) +"%)"
    print(f'\n{matriz_prompting}')
    return matriz_prompting
=======
def prompting(contenedor):
    f = 0
    for i in range(1,len(contenedor)):
        aux = (contenedor[i].replace('"', "")).split(",")
        vector_contador[int(aux[2])] += 1 
        n = aux[3]
        a = n.strip("/n")
        a = int(float(a))
        if a%60 == 0 and f != a/60:
            matriz_contador_time.append(np.copy(vector_contador))
            f = a/60        
    print(vector_contador)
    print(matriz_contador_time)

def calcular_prompting(vector): #debes darle un vector con los valores el peso de cada nodo, y devuelve el prompting de cada uno de los nodos en otro vector.
    matriz_prompting = []
    for i in range(len(vector)):
        matriz_prompting.append(vector[i]/sum(vector))
    print(matriz_prompting)
    return matriz_prompting




>>>>>>> 2ce219e0adbb5012766c4a70a319f0d0af1a90ec

def main():
    fileName = 'Grupo1-393371.csv'
    try:
        archivo = open(fileName, 'r')
        contenedor = archivo.readlines()
        archivo.close()
    except:
        sys.exit(f'Error file {fileName} not found.')   

    matriz= np.zeros((5, 5))
<<<<<<< HEAD
    matrizAdyacencia_Prompting(matriz, contenedor)
    calcular_prompting(vector_contador, labelsPercents)
    graficarGrafo(matriz)
=======
    matriz_total = rellenarMatrizDeAdyacencia(matriz, contenedor)
    prompting(contenedor)
    calcular_prompting(vector_contador)


>>>>>>> 2ce219e0adbb5012766c4a70a319f0d0af1a90ec

#CREAMOS LA ESTRUCTURA DEL GRAFO
G = nx.DiGraph()
<<<<<<< HEAD
color_map = ["green", "blue", "red", "orange", "purple"]
labelsPercents = {}#Diccionarioa que guardara los porcentajes de cada nodo para el grafico
=======
G.add_node(0,pos=(3,4))
G.add_node(1,pos=(4,2))
G.add_node(2,pos=(1,4))
G.add_node(3,pos=(0,2))
G.add_node(4,pos=(2,0))
>>>>>>> 2ce219e0adbb5012766c4a70a319f0d0af1a90ec
matriz_timestamp = [] #guarda el peso de los vectores a través del tiempo 
vector_contador = [0,0,0,0,0] #lista que contiene el peso de los vectoes al final de toda la comunicación 
matriz_contador_time = [] #lista que contiene vectores con el peso de cada nodo a través del tiempo

#---------------------------------------------
main()