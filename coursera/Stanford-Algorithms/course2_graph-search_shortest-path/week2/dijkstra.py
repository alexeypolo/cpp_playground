#!/usr/bin/env python3

import sys

class Vertex:
    def __init__(self, i, neighbours, distances):
        self.i = i             # index of a vertex, 1-based, hence value of 0 is a "dummy"
        self.neighbours = []   # neighbour vertices
        self.distances = []    # distances to the neighbour vertices

    def print(self):
        print(self.i, self.neighbours, self.distances)

# calculate shortest distances from vertex #1 to all the other vertices
def dijkstra(vertices):
    # vertices are labeled 1-based, so [0] is a dummy and the distance of vertex [1] from itself is 0
    min_dists = (len(vertices) + 1) * [0]

    X = {}
    V = vertices.copy()
    victim = 1 # pop element with key '1'
    X[victim] = V.pop(victim)

    #print('victim', victim, ', min_dists', min_dists, ', X', X.keys(), ', V', V.keys())

    while len(V):
        # Min Dijkstra Score for edges crossing the cut between X and V
        mds = 1000000
        victim = 0

        # iterate through vertices in X
        for i,x in X.items():
            # look for edges crossing the cut between X and V, calc min dijkstra score
            for (n,d) in zip(x.neighbours,x.distances):
                if n in X:
                    continue
                # we found a crossing edge - an edge with tail in X and head in V
                ds = min_dists[x.i] + d
                if ds < mds:
                    mds = ds
                    victim = n

        if victim == 0:
            # we found a pure "sink" node, no outbound neighbours
            break

        # store min distance for the 'victim' node and move the victim from V to X
        min_dists[victim] = mds
        X[victim] = V.pop(victim)
        #print('victim', victim, ', min_dists', min_dists, ', X', X.keys(), ', V', V.keys())
    return min_dists

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<graph file>')
        return -1

    vertices = {}
    edges = 0
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.split()
            i = int(line.pop(0))
            v = Vertex(i, [], [])
            for edge in line:
                n,d = [int(x) for x in edge.split(',')]
                v.neighbours.append(n)
                v.distances.append(d)
                edges += 1

            vertices[i] = v

    print('vertices', len(vertices), ', edges', edges)

    min_dist = dijkstra(vertices)
    if len(min_dist) < 197:
        print('TEST CASE:', min_dist)
        return 0

    answer = []
    for i in [7,37,59,82,99,115,133,165,188,197]:
        answer.append(min_dist[i])
    print('Quiz answer:', answer)

    return 0

if __name__ == '__main__':
    sys.exit(main())
