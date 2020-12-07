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
    anterior = 0
    tiempoVentanas = 60
    for a in range(1, len(contenedor)):
        aux = (contenedor[a].replace('"', "")).split(",")
        vector_contador[int(aux[2])] += 1 
        if(a % 2 == 0):
            matriz[int(anterior)][int(aux[2])] += 1 
            
        if( round(float(aux[3])) >= tiempoVentanas and a % 2 != 0):
            #print(f'Tiempo conversacion real:{round(float(aux[3]))} || Tiempo a comparar: {tiempoVentanas}')
            tiempoVentanas += 60
            matriz_contador_time.append(list(np.copy(vector_contador)))

        anterior = int(aux[2])

    if matriz_contador_time[-1] != vector_contador:
        matriz_contador_time.append(np.copy(vector_contador))

def graficarGrafo(matriz):
    global color_nodes

    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
            G.add_edge(x, y, weight = (matriz[x, y])* 0.01, length = 0.1)

    print(f'{matriz} \n')  
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
    
def randomColor(arrayColors, nodeNumbers):
    if(nodeNumbers == len(arrayColors)):
        return arrayColors

    nodeColors = []
    for i in range(0, nodeNumbers):
        nodeColors.append(random.choice(arrayColors))
    return nodeColors

def calcular_prompting(vector): #debes darle un vector con los valores el peso de cada nodo, y devuelve el prompting de cada uno de los nodos en otro vector.
    global labelsPercents
    matriz_prompting = []
    for i in range(len(vector)):
        matriz_prompting.append(vector[i]/sum(vector))
        labelsPercents[i] = "Usuario " + str(i) + " (" + str(round((matriz_prompting[i])*100)) +"%)"
    print(f'\n{matriz_prompting}')
    return matriz_prompting

def main():
    fileName = 'Grupo1-393371.csv'
    try:
        archivo = open(fileName, 'r')
        contenedor = archivo.readlines()
        archivo.close()
    except:
        sys.exit(f'Error file {fileName} not found.')   

    matriz= np.zeros((5, 5))
    matrizAdyacencia_Prompting(matriz, contenedor)
    calcular_prompting(vector_contador)
    graficarGrafo(matriz)
    listaMaestra=[]
    for i in color_nodes:
        listaMaestra.append([])
    for i in matriz_contador_time:
        Number = 0
        for l in (calcular_prompting(i)):
            listaMaestra[Number].append(l)
            Number +=1
    #print(listaMaestra)
    plt.xlabel("Tiempo[Minutos]")
    plt.ylabel("Prompting")
    plt.title("Grafico Prompting")
    Number = 0
    #plt.legend(('Funcion 1', 'Funcion 2', 'Funcion 3'),prop = {'size': 10}, loc='upper right')
    for i in listaMaestra:
        plt.plot(i,color=color_nodes[Number][0],label='Node '+str(Number))
        Number += 1
    plt.legend(loc='upper right')
    plt.show()
        
            
            
        
        
    print(color_nodes)
#CREAMOS LA ESTRUCTURA DEL GRAFO
G = nx.DiGraph()
color_map = ["green", "blue", "red", "magenta", "yellow"]
color_nodes = []
labelsPercents = {}#Diccionarioa que guardara los porcentajes de cada nodo para el grafico
matriz_timestamp = [] #guarda el peso de los vectores a través del tiempo 
vector_contador = [0,0,0,0,0] #lista que contiene el peso de los vectoes al final de toda la comunicación 
matriz_contador_time = [] #lista que contiene vectores con el peso de cada nodo a través del tiempo

#---------------------------------------------
main()
