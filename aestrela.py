import networkx as nx
from queue import PriorityQueue

def criaGrafo(file):
    """Builds a weighted, undirected grafo"""
    grafo = nx.MultiGraph()
    for line in file:
        # insere em 'v1' e 'v2' as cidades e em 'w' as distancias
        v1, v2, w = line.split(',')
        # retira os espacos em branco da string
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())

        # nao é necessaria esta verificacao
        # if v1 not in grafo:
            # grafo.add_node(v1)
        # if v2 not in grafo:
            # grafo.add_node(v2)

        # cria as arestas entre as cidades e define o peso entre elas
        # v1 e v2 ja serao adicionados como 'nodes'
        grafo.add_edge(v1,v2,weight = w)
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

def aestrela(graph, start, goal):
    # cria uma fila de prioridades
    frontier = PriorityQueue()
    # inicia a fila com a cidade de origem e custo 0
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        #  recebe cidade atual
        current = frontier.get()

        # destino alcancado
        if current == goal:
            break


        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def main():
    start = input('Cidade de inicio: ')
    dest = input('Cidade de destino: ')
    # abre arquivo de distancias reais somente como leitura
    with open('dist_real.csv', 'r') as file:
        lines = file.readlines()
    grafo = criaGrafo(lines)
    # print(criaHeuristica())

    # imprimir 'nós'
    print(grafo.nodes())
    # imprimir 'arestas'
    print(grafo.edges())

    # chama busca A*
    # aestrela(grafo, start, dest)

if __name__ == '__main__':
    main()
