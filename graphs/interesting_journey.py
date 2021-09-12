from collections import deque
from random import randint


def list_generator(n, dist):

    s = [str(n)]

    for _ in range(n):
        s.append(str(randint(-dist, dist)) + ' ' + str(randint(-dist, dist)))
    
    s.append(str(randint(0, 2*dist)))
    s.append(str(randint(0, n-1)) + ' ' + str(randint(0, n-1)))

    return '\n'.join(s)


def graph_matrix(text):

    text = text.split('\n')
    n = text.pop(0)
    n = int(n)
    cord = text.pop()
    start, finish = map(int, cord.split())
    k = text.pop()
    k = int(k)
    graph = []
    cities = []

    for item in text:
        s1, s2 = map(int, item.split())
        cities.append((s1, s2))
    
    metrics = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])
    for city in cities:
        graph.append( [metrics(city, c) <= k for c in cities] )

    return graph, start, finish


def bfs(graph, start, finish):

    start -= 1
    finish -= 1
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    is_visited[start] = True
    deq = deque([start])

    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            break
        for i, vertex in enumerate(graph[current]):
            if vertex and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)
    else:
        return -1
    
    cost = 1
    i = finish
    while parent[i] != start:
        cost += 1
        i = parent[i]
    
    return cost


text = list_generator(7, 10)
graph, start, finish = graph_matrix(text)
way_len = bfs(graph, start, finish)

print(way_len)
