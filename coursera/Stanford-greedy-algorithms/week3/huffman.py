#!/usr/bin/env python3

import sys
import heapq
import collections

Node = collections.namedtuple('node', ['w', 'sym', 'l', 'r'])

def tree_to_codes(node, codes, prefix=''):
    if not node.l and not node.r:
        # Leaf!!!
        assert(len(node.sym) == 1)
        index = node.sym[0]
        codes[index] = prefix
        return

    if node.l:
        tree_to_codes(node.l, codes, prefix + '0')
    if node.r:
        tree_to_codes(node.r, codes, prefix + '1')

    return

def huffman(n, weights):

    # create a heap of (w, [index]) tuples.
    # As the Huffman algo progresses, the heap will contain more and more
    # merged entries: (accumulated weight, [index0,index1,...])
    h = []
    for index,w in enumerate(weights):
        heapq.heappush(h, Node(w, [index], None, None))

    while len(h) > 1:
        min0 = heapq.heappop(h)
        min1 = heapq.heappop(h)

        # merge min0 and min1
        hparent = Node(min0.w + min1.w, min0.sym + min1.sym, min0, min1)
        heapq.heappush(h, hparent)

        #print(h)

    # Build codes by traversing the tree
    codes = n*[""]
    tree_to_codes(h[0], codes)

    # calc a few vitals
    min_bps = max_bps = len(codes[0])
    acc = len(codes[0]) * weights[0]
    sum_of_weights = weights[0]
    for (w,c) in zip(weights[1:], codes[1:]):
        bits = len(c)
        if min_bps > bits:
            min_bps = bits
        if max_bps < bits:
            max_bps = bits
        acc += w * bits
        sum_of_weights += w
    avg_bps = float(acc) / sum_of_weights

    return codes, min_bps, max_bps, avg_bps

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

    codes, min_bps, max_bps, avg_bps = huffman(n, weights)
#    print('codes', codes)
    print('min_bps %f, max_bps %f, avg_bps %f' % (min_bps, max_bps, avg_bps))
    return 0

if __name__ == '__main__':
    sys.exit(main())
