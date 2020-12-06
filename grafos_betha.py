#Librerias estandar
import sys

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

def rellenarMatrizDeAdyacencia(matriz, contenedor):
    anterior = 0
    tiempoVentanas = 60
    for a in range(1, len(contenedor) - 1):
        aux = (contenedor[a].replace('"', "")).split(",")
       
        if(a % 2 == 0):
            matriz[int(anterior)][int(aux[2])] += 1 
            
        #if( round(float(aux[3])) >= tiempoVentanas and a % 2 != 0):
         #   print(f'Tiempo conversacion real:{round(float(aux[3]))} || Tiempo a comparar: {tiempoVentanas}')
          #  tiempoVentanas += 60
           # graficarGrafo(matriz)
            
        anterior = int(aux[2])

    graficarGrafo(matriz)
    return matriz

def graficarGrafo(matriz):
    for x in range(0 , len(matriz[0])):
        for y in range(0, len(matriz[0])):
           G.add_edge(x, y, weight = (matriz[x, y])* 0.03, length = 0.1)

    print(f'{matriz} \n')       
    weights = nx.get_edge_attributes(G,'weight').values()
    pos = nx.circular_layout(G)
    nx.draw(G, pos,with_labels=True,node_size=3400,font_size = 20, node_color = 'orange',width=list(weights), connectionstyle='arc3, rad = 0.1')
    plt.show(block=False)
    plt.pause(5)
    plt.close()

def prompting(matriz):
    suma_w_nodos = []
    aux = 0
    w_total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            aux += matriz[i][j]
        suma_w_nodos.append(aux)
        w_total += aux
        aux = 0
    return suma_w_nodos, w_total   

def main():
    fileName = 'Grupo1-393371.csv'
    try:
        archivo = open(fileName, 'r')
        contenedor = archivo.readlines()
        archivo.close()
    except:
        sys.exit(f'Error file {fileName} not found.')   

    matriz= np.zeros((5, 5))
    matriz_total = rellenarMatrizDeAdyacencia(matriz, contenedor)
    print(matriz_total)
    print(prompting(matriz_total))

#CREAMOS LA ESTRUCTURA DEL GRAFO CON SUS NODOS
G = nx.DiGraph()
G.add_node(0,pos=(3,4))
G.add_node(1,pos=(4,2))
G.add_node(2,pos=(1,4))
G.add_node(3,pos=(0,2))
G.add_node(4,pos=(2,0))
#---------------------------------------------
main()