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
import resource

t = 0       # track the finishing times on the 1st pass of Kosaraju's algo

s = 0       # leader vertex for the current SCC, i.e. most recent vertex from
            # which DFS was # initiated at the 2nd pass of Kosaraju's algo

explored = None
f = None
finv = None

# G - list of lists, i'th element is a list of endpoints of outbound edges starting at i'th vertex
# n - number of vertices
def kosaraju(G, Gt, n):
    global s, t, explored, f, finv

    explored = (n+1) * [False]
    f = (n+1) * [0]             # finishing time - index, vertex id - element
    finv = (n+1) * [0]          # finishing time - index, vertex id - element
    t = 0
    # pass 1: explore the transposed Graph - all edges are reversed
    for i in range(n, 0, -1):
        if not explored[i]:
            DFS_iterative(Gt, i)

    # pass 2: explore the original Graph in the order of decreasing finishing times
    explored = (n+1) * [False]
    SCC_sizes = []
    # finv is sorted by 't' in ascending order (it is sorted by "construction").
    # skip dummy finv[0]
    for i in reversed(finv[1:]):
        if not explored[i]:
            count = DFS_iterative(G, i)
            SCC_sizes.append(count)

    SCC_sizes.sort(reverse=True)
    print('Number of SSCs', len(SCC_sizes))
    print('Sizes of 5 largest SCCs', SCC_sizes[0:5])

# G - graph
# i - at which vertex to start
# finish-time trick from here: http://stackoverflow.com/questions/24051386/kosaraju-finding-finishing-time-using-iterative-dfs

def DFS_iterative(G, i):
    global t, explored, f, finv

    print(i, 'invoked')

    queue = [i]
    explored_count = 0
    while len(queue):
        v = queue.pop() # For BFS, use pop(0)
        if not explored[v]:
            explored[v] = True
            explored_count += 1
            queue.append(v)
            for w in G[v]:
                if not explored[w]:
                    queue.append(w)
        else:
            if f[v] == 0:
                t += 1
                f[v] = t
                finv[t] = v

    return explored_count

# G - graph
# i - at which vertex to start
def DFS_recursive(G, i):
    global t, explored, finv

    explored[i] = True

    ws = G[i] # list of remote endpoints of outbound edges
    for w in ws:
        if not explored[w]:
            DFS_recursive(G, w)

    t+=1
    finv[t] = i

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

    kosaraju(G, Gt, n)

    return 0

if __name__ == '__main__':
    sys.exit(main())
