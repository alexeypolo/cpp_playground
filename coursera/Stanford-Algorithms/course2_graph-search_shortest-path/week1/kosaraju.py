#!/usr/bin/env python3

# Kosaraju algorithm
#
# Takes adjacency list as an input.
# Each row of a file is two numbers - first number is the "tail" vertex and the
# second number is the "head" vertex.
#
# Vertices are 1 based

import sys
from collections import deque

# G - list of lists, i'th element is a list of endpoints of outbound edges starting at i'th vertex
# n - number of vertices
def DFS(G, n):
    s = 1 # vertices are indexed 1-based. We start at vertex '1'

    #queue = [s]           # stack - for DFS
    queue = deque([s])    # fifo - for BFS

    explored = (n+1) * [False]
    explored[s] = True

    print(s)

    while len(queue):
        #v = queue.pop()
        v = queue.popleft()
        ws = G[v] # list of remote endpoints of outbound edges
        for w in ws:
            if not explored[w]:
                explored[w] = True
                queue.append(w)
                print(w)

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<input file with adjacency list, vertices are 1 based>')
        return -1

    # Read edges and calculate the number of vertices 'n'. Assume - vertices are 1 based
    n = -1
    E = []
    with open(sys.argv[1]) as f:
        for line in f:
            if not line:
                continue
            v0,v1 = [int(x) for x in line.split()]
            E.append([v0, v1])
            if n < v0: n = v0
            if n < v1: n = v1

    print('edges', len(E), ', vertices', n)

    # G[0] is a dummy, vertices are 1 based, so we allocate one extra so that
    # vertices ID can be used as an index into G. G[0] will never be referenced

    # Graph - an i'th element is a list of vertices at the remote end of an
    # oubound edge starting in i'th vertex
    G = [[] for x in range(n + 1)]

    # Transposed Graph - an i'th element is a list of vertices at the remote end of an
    # inbound edge ending at i'th vertex
    Gt = [[] for x in range(n + 1)]

    for e in E:
        v0,v1=e[0],e[1]
        G[v0].append(v1)
        Gt[v1].append(v0)

    print('done preparing the dataset')

    DFS(G, n)

    return 0

if __name__ == '__main__':
    sys.exit(main())
