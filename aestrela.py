import networkx as nx
from queue import PriorityQueue

def criaGrafo(file):
    """Builds a weighted, undirected grafo"""
    grafo = nx.Graph()
    for line in file:
        # insere em 'v1' e 'v2' as cidades e em 'w' as distancias
        v1, v2, w = line.split(',')
        # retira os espacos em branco da string
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())

        # cria as arestas entre as cidades e define o peso entre elas
        # v1 e v2 ja serao adicionados como 'nodes'
        grafo.add_edge(v1,v2,weight = w)

        # imprimir peso da aresta
        # print(grafo[v1][v2]['weight'])
    # print("Numero de nós no grafo: ", len(grafo))
    return grafo

def criaHeuristica():
    h = {}
    # abre arquivo de distancias heuristicas somente como leitura
    # le o arquivo e passa ele para o vetor 'h'
    with open("dist_heuristica.csv", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            # insere o nome da cidade no 'node'
            node = line[0].strip()
            sld = int(line[1].strip())
            # cria vetor que para cada posicao (nome da cidade) ira armazenar a distancia 'sld'
            h[node] = sld
    return h

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

def aestrela(graphR, start, goal, graphH):
    # cria uma fila de prioridades
    frontier = PriorityQueue()
    # inicia a fila com a nó de origem e o custo = 0
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        #  recebe o nó atual
        current = frontier.get()
        # imprime os nós adjacentes do nó atuais e o peso entre as arestas
        print(graphR.adj[current])

        # se o objetivo for alcançado
        if current == goal:
            break

        # verifica o peso das adjacências do nó atual
        for next_node in graphR.adj[current]:
            # atribui um novo custo para as adjacencias atuais f(n) = g(n) + h(n)
            new_cost = graphR[current][next_node]['weight'] + graphH[next_node]

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + graphH[next_node]
                frontier.put(next_node, priority)
                came_from[next_node] = current

    return  cost_so_far #,came_from


def main():
    # start = input('Cidade de inicio: ')
    # dest = input('Cidade de destino: ')
    start = "lugoj"
    dest = "bucharest"
    # abre arquivo de distancias reais somente como leitura
    with open('dist_real.csv', 'r') as file:
        lines = file.readlines()

    grafo = criaGrafo(lines)

    # imprimir 'nós'
    # print("Nós do grafo: \n",grafo.nodes(),"\n")
    # imprimir 'arestas'
    # print("Arestas do grafo: \n",grafo.edges(),"\n")

    # chama busca A*
    print("\n", aestrela(grafo, start, dest, criaHeuristica()))

if __name__ == '__main__':
    main()
