#!/usr/bin/env python3

import sys
import heapq

# "median" definition
# if k is odd, then mk is ((k+1)/2)th smallest number among x1,...,xk;
# if k is even, then mk is the (k/2)th smallest number among x1,...,xk
#
# Invariant for heap-based implementation:
#   maintain invariant that ~ i/2 smallest (largest) elements in HLow (HHigh)
#

# Naive - working !!!
def median_naive(V):
    medians = []

    for i,v in enumerate(V):
        vcopy = V[0:i+1]
        vcopy.sort()

        #print('i', i, ', vcopy', vcopy)
        if i % 100 == 0:
            print(i)

        # 1-based index
        k = i+1
        if k % 2 == 0:
            mk = vcopy[int(k/2) - 1]
        else:
            mk = vcopy[int((k+1)/2) - 1]
        medians.append(mk)
    return medians

# Heap-based - TODO: doesn't work, use test cases 1 & 2 to verify
def median_heap(V):
    heap_lo = [-min(V[0:1])]
    heap_hi = [max(V[0:1])]

    heapq.heapify(heap_lo)
    heapq.heapify(heap_hi)

    medians = len(V) * [0]
    for i,v in enumerate(V):
        if v <= -heap_lo[0]:
            heapq.heappush(heap_lo, -v)
        else:
            heapq.heappush(heap_hi, v)

        # maintain the invariant and extract mk - the k'th median
        if (i+1)%2 == 0:
            if len(heap_lo) > len(heap_hi):
                heapq.heappush(heap_hi, heapq.heappop(heap_lo))
            elif len(heap_lo) < len(heap_hi):
                heapq.heappush(heap_lo, -heapq.heappop(heap_hi))
            else: # equal sizes
                pass
            mk = -heap_lo[0]
        else:
            if len(heap_lo) > len(heap_hi):
                mk = -heap_lo[0]
            else:
                mk = heap_hi[0]

        medians[i] = mk

    print('medians', medians)
    return medians

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<integers file>')
        return -1

    V = []
    with open(sys.argv[1]) as f:
        for line in f:
            V.append(int(line))

    m = median_naive(V)
    print('naive:', sum(m) % 10000)

    m = median_heap(V)
    print('heap:', sum(m) % 10000)

    return 0

if __name__ == '__main__':
    sys.exit(main())
