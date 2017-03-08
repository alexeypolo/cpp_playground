#!/usr/bin/env python3

import sys

# maximum-weight independent set
def mwis(n, weights):
    assert((len(weights) == n) and (n > 2))

    print('weights', weights)

    # list of lists
    wis = n*[0]

    # a path of single vertex is an MWIS
    wis[0] = weights[0]

    # a path of two vertices - choose the one with a greater weight
    wis[1] = max(weights[0], weights[1])

    # build sequence of 1:n optimal solutions
    for i in range(2,n):
        # compare two cases - the optimal solution includes or does not include the current vertex
        wis[i] = max(wis[i-1], wis[i-2] + weights[i])

    print('wis', wis)

    # reconstruct the mwis subset of vertices of n'th solution
    vertices = []
    i = n - 1
    while i >= 2:
        if wis[i] - weights[i] == wis[i-2]:
            # vertex i is part of mwis(n)
            vertices.append(i)
            i -= 2
        else:
            # vertex i is not in mwis(n)
            i -= 1

    if i == 1 and wis[i] == weights[i]:
        vertices.append(1)
    else:
        vertices.append(0)

    vertices.sort()
    return vertices

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<weight file>')
        sys.exit(-1)

    # read input
    weights = []
    with open(sys.argv[1]) as f:
        n = int(f.readline())
        for line in f:
            weights.append(int(line))

    vertices = mwis(n, weights)
    print('vertices', vertices)

    # we do everything 0-based. But the assignments wants the answer 1-based.
    # We convert here by looking up (i-1)
    res = ''
    for i in [1,2,3,4,17,117,517,997]:
        res += '1' if i-1 in vertices else '0'

    print(res)

    return 0

if __name__ == '__main__':
    sys.exit(main())
