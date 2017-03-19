#!/usr/bin/env python3

import sys

class Vertex:
    def __init__(self, i, neighbours, distances):
        self.i = 0             # index of a vertex, 1-based, hence value of 0 is a "dummy"
        self.neighbours = []   # neighbour vertices
        self.distances = []    # distances to the neighbour vertices

    def print(self):
        print(self.i, self.neighbours, self.distances)

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<graph file>')
        return -1

    vertices = []
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

            vertices.append(v)

    print('vertices', len(vertices), ', edges', edges)

    return 0

if __name__ == '__main__':
    sys.exit(main())
