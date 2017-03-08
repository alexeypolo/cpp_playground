#!/usr/bin/env python3

import sys
import numpy

def opt_bst(p):
    A=numpy.zeros([len(p),len(p)])

    for s in range(len(p)):
        for i in range(len(p)-s):
            min_C = 0xffffffff
            sum_probabilities_i_j = sum(p[i:i+s+1])
            for r in range(i,i+s+1):
                C = sum_probabilities_i_j
                if r > i:
                    C += A[i,r-1]
                if r < i+s:
                    C += A[r+1,i+s]
                min_C = min(min_C, C)

            print('i,j=%d,%d: r from %d to %d, min_C=%d' % (i, i+s, i, i+s, min_C))
            A[i,i+s]=min_C
    print(A)
    avg_search_cost = A[0,len(p)-1]
    return avg_search_cost

def main():
    # frequencies (or probabilities) of keys. Key is simply the index
    p = [.05,.4,.08,.04,.1,.1,.23]
    print(p)
    print(opt_bst(p))
    return 0

if __name__ == '__main__':
    sys.exit(main())
