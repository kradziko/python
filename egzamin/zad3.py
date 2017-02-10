'''dany jest graf opisany slownikiem w nastepujacy sposob g ,(wierzcholek nr 1 jest polaczony z wierzcholkami 2 ,4 ,5)
Napisz procedure  znajdywania wszystkich wierzcholkow osiagalnych z zadanego wierzcholka p, napisz procedure sprawdzajaca czy
dany graf jest spojny oraz program znajdujacy droge hamiltona w grafie'''

g = {1:[2,4,5], 2:[1,3], 3:[2], 4:[1], 5:[1], 6:[]}

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        print stack
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(filter(lambda x: x not in visited, graph[vertex]))
    return visited

def czySpojny(graph):
    licznik = len(graph)
    visited, stack = [], [1]
    while stack:
        vertex = stack.pop()
        licznik -=1
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(filter(lambda x: x not in visited, graph[vertex]))
    if licznik != 0:
        return False
    return True


def drogaHamiltona(graph,v):
    pass


print dfs(g,5)
print czySpojny(g)
