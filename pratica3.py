#Pratica03 Igor Miranda e Renan Siman
# networkx - library to create graphs
#from collection import OrderedDict
import csv
import numpy

# Reading a file.csv
with open('dist_real.csv', newline = '') as csvfile:
    lines_real = list(csv.reader(csvfile))

dist_heur = open('dist_heuristica.csv')
lines_heur = csv.reader(dist_heur)

arestas_reais = []
i = 0
print("Real distances between the cities\n")
for lineR in lines_real:
    print(lineR)
    i+=1

print("O valor de i:", i)
print("\nHeuristic distances between Bucharest and the other cities\n")
for lineH in lines_heur:
   print(lineH)
print("\n")

# Construction of A* algorithm
# Step 0: choose the start point
start_city = [3]
start_city[0] = input('Write the city who is gonna start the algorithm: ')
print("The algorithm begins in", start_city[0])

# Step 1: create the function f(n) = g(n) + h(n) for the start_city
# g(n) for start_city - store the real distances in array
for lineR in lines_real:
    numpy.split(lineR,3)
    print(lineR[2])
    # if (start_city[0] is aux[0])
    #     start_city[1] is aux[1]
    #     print("Cidade destino:", start_city[1])

# # h(n) for start_city - store the heuristic distance in array
# for lineH in lines_heur:
#     if (start_city[0] is lineH)
#         start_city[2] is
