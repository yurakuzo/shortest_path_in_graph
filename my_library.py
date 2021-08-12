import shortestwaygraph as swg

ds = swg.DijkstraSearch(9)
fws = swg.Floyd_WarshallSearch(6)

ds.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]]

fws.graph = [[0, 1, 6, fws.INF, fws.INF, fws.INF],
            [fws.INF, 0, 4, fws.INF, -2, fws.INF],
            [fws.INF, fws.INF, 0, fws.INF, 5, 3],
            [2, fws.INF, fws.INF, 0, -5, fws.INF],
            [fws.INF, fws.INF, fws.INF, 8, 0, 4],
            [fws.INF, fws.INF, fws.INF, fws.INF, fws.INF, 0]]

ds.dijkstra(0, 8)
print("-"*26)
fws.floyd_warshall(fws.graph)

# question:
# def foo(a, *args):
#       if not args:
#             pass
#       elif args:
#             pass