#!/usr/bin/env python3

import sys

# Large prime number
hash_n = 2000003

# hash function is 'x mod n'
def hashify(keys):
    H=hash_n*[None]
    hash_collisions = 0
    key_collisions = 0
    for key in keys:
        i = key % hash_n
        if H[i] == None:
            H[i] = [key]
        else:
            hash_collisions += 1
            if key in H[i]:
                key_collisions += 1
            else:
                H[i].append(key)

    print('hash collision', hash_collisions, ', key collisions', key_collisions)
    return H

def lookup(H, key):
    i = key % hash_n
    return True if (H[i] != None) and (key in H[i]) else False

# count how many distinct (x,y) pairs satisfy lo <= (t=x+y) <= hi
def count_2sum_in_range(A, lo, hi):
    assert(hi > lo)

    H = hashify(A)

    hits={}

    for t in range(lo, hi+1):
        print((t - lo) / (hi - lo))
        for x in A:
            y = t-x
            if x!=y and lookup(H, y):
                print('hit:', x, y)
                hits[t] = 1

    return len(hits)

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.atgv[0], '<input file>')
        return -1

    A = []
    with open(sys.argv[1]) as f:
        A = [int(x) for x in f.readlines()]

    m = min(A)
    M = max(A)
    print('length:', len(A), ', min:', m, ', max:', M, ', 10K buckets:', (M-m)/10000 + 1)
    print('2-sum:', count_2sum_in_range(A, -10000, 10000))
    return 0

if __name__ == '__main__':
    sys.exit(main())
