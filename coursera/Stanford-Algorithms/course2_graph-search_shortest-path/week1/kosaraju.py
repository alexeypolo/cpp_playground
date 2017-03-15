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

# TODO: use a datastructure to get this list in O(1)
def get_remote_ends_of_outbound_edges(E, v):
    return [edge[1] for edge in E if edge[0] == v]

# TODO: use a datastructure to get this list in O(1)
def get_remote_ends_of_inbound_edges(E, v):
    return [edge[0] for edge in E if edge[1] == v]

# E - list of edges
# n - number of vertices
def DFS(E, n):
    s = E[0][0]

    #queue = [s]           # stack - for DFS
    queue = deque([s])    # fifo - for BFS

    explored = (n+1) * [False]
    explored[s] = True

    print(s)

    while len(queue):
        #v = queue.pop()
        v = queue.popleft()
        ws = get_remote_ends_of_outbound_edges(E, v)
        for w in ws:
            if not explored[w]:
                explored[w] = True
                queue.append(w)
                print(w)

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<input file with adjacency list, vertices are 1 based>')
        return -1

    # Read edges and calculate the number of vertices. Assume - vertices are 1 based
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

    DFS(E, n)

    return 0

if __name__ == '__main__':
    sys.exit(main())
