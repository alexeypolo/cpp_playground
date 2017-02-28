#!/usr/bin/env python3

import sys

def UF_find_cluster(UF_nodes, vertice):
    # vertices are indexed 1-based
    return UF_nodes[vertice - 1][1]

def UF_merge_clusters(UF_nodes, UF_sizes, c1, c2):
    # !!! clusters are indexed 1-based because, initially,
    # cluster==lead_vertex and vertices are 1-based
    if (UF_sizes[c1-1] > UF_sizes[c2-1]):
        mergeto, mergefrom = c1, c2
    else:
        mergeto, mergefrom = c2, c1

    # could just as well delete this entry, not sure what is less expensive - assign a 0 or delete

    UF_sizes[mergeto - 1] += UF_sizes[mergefrom - 1]
    UF_sizes[mergefrom - 1] = 0
    for i,node in enumerate(UF_nodes):
        if node[1] == mergefrom:
            node[1] = mergeto

# n: number of vertices
# graph: list of [v0, v1, edge cost]
# k: target number of clusters
def cluster(UF_nodes, UF_sizes, graph, k):
    # sort the graph by increasing edge cost
    graph.sort(key = lambda e: e[2])

    # Kruskal's algo with naive data structure (i.e. without Union Find)
    clusters_n = len(UF_nodes) # initially each vertice is a cluster
    #print('DEBUG: clusters_n',clusters_n,'\nUF_sizes',UF_sizes,'\nUF_nodes',UF_nodes)
    if clusters_n <= k:
        print('done prematurely')
        return 0

    # split the graph to 'k' clusters
    for idx,e in enumerate(graph):
        c0 = UF_find_cluster(UF_nodes, e[0])
        c1 = UF_find_cluster(UF_nodes, e[1])
        if c0 == c1:
            continue

        UF_merge_clusters(UF_nodes, UF_sizes, c0, c1)
        clusters_n -= 1

        if clusters_n == k:
            print('done clustering, last merged edge', e)
            break

    # continue scanning till the first edge that would result in one extra merge.
    # This cost if this edge is the 'min spacing' of clustering
    for idx,e in enumerate(graph[idx+1:]):
        c0 = UF_find_cluster(UF_nodes, e[0])
        c1 = UF_find_cluster(UF_nodes, e[1])
        if c0 != c1:
            print('first min-cost edge crossing the cut between clusters', e)
            break

    if idx + 1 < len(graph):
        max_spacing = e[2]
    else:
        max_spacing = 0

    print('done, idx', idx, ', edge', e, ', next edge', graph[idx+1])
    return max_spacing

def main():
    if len(sys.argv) != 3:
        print('USAGE:', sys.argv[0], '<graph file> <number of clusters>')
        return -1

    k = int(sys.argv[2])
    graph = []
    vertices = [] # vertices + the extra field for "lead vertice" for the Union-Find data structure
                     # initially, "lead vertice" is the vertice itself
    with open(sys.argv[1]) as f:
        n = int(f.readline())
        for line in f:
            edge=[int(x) for x in line.split()]
            graph.append(edge)
            vertices.append(edge[0])
            vertices.append(edge[1])

    U = list(set(vertices))

    # validate that vertices are a 1:n arithmetic progression: 1,2,...,n
    assert(n == len(U))
    assert(min(vertices) == 1)
    assert(max(vertices) == n)

    # vertices + the extra field for "lead vertice" for the Union-Find data structure
    # Initially, "lead vertice" is the vertice itself and each cluster is of size 1
    list_of_tuples = list(zip(U,U))
    UF_nodes = [list(elem) for elem in list_of_tuples]
    UF_sizes = len(U)*[1]
    print('Input preparation done! k =', k, 'n =', n)

    print(cluster(UF_nodes, UF_sizes, graph, k))
    return 0

if __name__ == '__main__':
    sys.exit(main())
