#!/usr/bin/env python3
import sys
import numpy
import time

def knapsack_huge(W, vw):
    prev_i=numpy.zeros([W+1],dtype=numpy.int)
    cur_i=numpy.zeros([W+1],dtype=numpy.int)

    for i in range(1,len(vw)+1):
        sys.stdout.write('%3.2f%%\r' % ((100.0 * i) / len(vw)))
        #print(i)
        for w in range(1,W+1):
            # without adding i'th item
            without_vi = prev_i[w]

            # with adding i'th item (if the item can fit)
            vi,wi=vw[i-1] # 0-based
            if wi <= w:
                with_vi = prev_i[w-wi] + vi
                cur_i[w]=max([with_vi,without_vi])
            else:
                # i'th item is too big - doesn't fit in
                cur_i[w]=without_vi
        prev_i, cur_i = cur_i, prev_i
    sys.stdout.write('\n')
    return prev_i[-1]

def knapsack(W, vw):
    # lookup array
    A=numpy.zeros([len(vw)+1,W+1])
    # loop over capacities, including the largest, hence W+1
    #   w==0, knapsack of size 0, corresponds w==0, all-i. All set to 0

    # loop over items count,
    #   0 - no items - corresponds to i==0, all-w. All set to 0
    #   1 - only item 1
    #   2 - items 1,2
    #   3 - items 1,2,3
    #     ... and so on

    # the order of nesting does not matter!!!
    for i in range(1,len(vw)+1):
        for w in range(1,W+1):
            # compare optimum solution with and without ith item

            # without adding i'th item
            without_vi = A[i-1,w]

            # with adding i'th item (if the item can fit)
            vi,wi=vw[i-1] # 0-based
            if wi <= w:
                with_vi = A[i-1,w-wi] + vi
                A[i,w]=max([with_vi,without_vi])
            else:
                # i'th item is too big - doesn't fit in
                A[i,w]=without_vi
    print(A)
    return A[-1,-1]

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<knapsack file>')
        return -1

    with open(sys.argv[1]) as f:
        for l in f:
            if l[0] != '#':
                break
        W,N = [int(x) for x in l.split()]
        vw=[]
        for l in f:
            if l[0]=='#':
                continue
            vw.append([int(x) for x in l.split()])

    assert(len(vw) == N)
    print(W,N)
    #print(knapsack(W,vw))
    print(knapsack_huge(W,vw))

    return 0

if __name__ == '__main__':
    sys.exit(main())

