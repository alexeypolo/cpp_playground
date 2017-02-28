#!/usr/local/bin/python3

import sys
import time

def prim(graph):
    # sort by edge cost in increasing order
    graph.sort(key = lambda edge: edge[2])

    v = graph[0][0] # arbitrary choice of a vertex to start with
    X = [v] # vertices spanned so far
    T = [] # edges of the spanning tree

    #print('G', graph, '\nT', T)

    while graph:
        # find a min-cost edge that is not already in T and has a vertex in X
        min_cost = sys.maxsize
        min_i = -1
        min_v = -1
        min_edge = []
        v0_in_tree = v1_in_tree = False

        for i,edge in enumerate(graph):
            if edge[2] < min_cost:
                v0_in_tree = (edge[0] in X)
                v1_in_tree = (edge[1] in X)
                if v0_in_tree == v1_in_tree:
                    continue

                if v0_in_tree:
                    min_v = edge[1]
                else:
                    min_v = edge[0]

                #print(edge, v0_in_tree, v1_in_tree)
                min_edge = edge
                min_cost = edge[2]
                min_i = i

        #print('min_edge', min_edge)

        # If we don't find an edge, it means that T spans all vertices and we are done
        if min_i < 0:
            #print('done')
            break

        g = graph.pop(min_i)
        assert(g == min_edge)

        X.append(min_v)
        T.append(g)
        #print('G', graph, '\nT', T, '\nX', X, 'v0_in_tree', v0_in_tree)

    #print('vertices', X)
    assert(len(X) == len(set(X)))
    #print('mst', T)
    T_weight = sum([t[2] for t in T])
    return T_weight

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<edges file>')

    graph=[]
    with open(sys.argv[1]) as f:
        pair_str = f.readline().split()
        number_of_nodes, number_of_edges = int(pair_str[0]), int(pair_str[1])
        for line in f:
            trival = line.split()
            graph.append([int(v) for v in trival])

    t0 = time.perf_counter()
    res = prim(graph)
    t1 = time.perf_counter()
    print(res, t1-t0)

if __name__ == '__main__':
    sys.exit(main())
