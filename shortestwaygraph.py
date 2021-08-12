import sys
from math import inf
from itertools import product
import networkx as nx
import matplotlib.pyplot as plt
import numpy


def visualize_graph(graph):
    visual = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                x = j
                y = graph[:i + 1].index(graph[i])
                visual.append([x, y, {'weight': graph[x][y]}])
    numpy.random.seed(2040021520)
    # 111, 666,666666, 22222, 2040021520
    # few seeds that also work
    G = nx.Graph()
    G.add_edges_from(visual)
    nx.draw_networkx(G)
    plt.show()

class DijkstraSearch():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def minDistance(self, dist, sptSet):
        min = sys.maxsize # Initialize minimum distance for next node
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v
        return min_index

    def printSolution(self, dist, src, *args):
        if not args:
            for node in range(self.V):
                print(f"Distance from {src} to {node} = {dist[node]}")
        if args:
            for node in range(args[0] + 1):
                print(f"Distance from {src} to {node} = {dist[node]}")
            # print(f"Дистанція від {src} до {args[0]} = {dist[args[0]]}")
        visualize_graph(self.graph)

    def dijkstra(self, start, *args):
        if not args:
            dist = [sys.maxsize] * self.V
            dist[start] = 0
            sptSet = [False] * self.V
            for cout in range(self.V):
                u = self.minDistance(dist, sptSet)
                sptSet[u] = True
                for v in range(self.V):
                    if self.graph[u][v] > 0 and not sptSet[v] and\
                        dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
            self.printSolution(dist, start)

        if args:
            dist = [sys.maxsize] * self.V
            dist[start] = 0
            sptSet = [False] * self.V
            for cout in range(self.V):
                u = self.minDistance(dist, sptSet)
                sptSet[u] = True
                for v in range(self.V):
                    if self.graph[u][v] > 0 and sptSet[v] == False and\
                        dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
            self.printSolution(dist, start, args[0])


class Floyd_WarshallSearch():
    def __init__(self, n):
        self.INF = 999
        self.V = n
        self.graph =  [[0 for col in range(n)]
                      for row in range(n)]
        self.matrix = [[0 for col in range(n)] for row in range(n)]


    def floyd_warshall(self, graph):
        distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        self.print_solution(distance)
        visualize_graph(self.matrix)

    def print_solution(self, distance):
        for i in range(self.V):
            for j in range(self.V):
                if (distance[i][j] == self.INF):
                    print("INF", end=" ")
                    self.matrix[i][j] = self.INF
                else:
                    print(distance[i][j], end="  ")
                    self.matrix[i][j] = distance[i][j]
            print(" ")
