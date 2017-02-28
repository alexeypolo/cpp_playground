#!/usr/bin/env python3

# Input:
#   24 bit vectors, number of vectors is 200000 (not too big!!!)
#
# The general idea:
#  We need to put vectors with Hamming distance <=2 (i.e. <=2 bits are different) in same cluster
#  To do that, we first find all duplicates for [x x 1 1 1 1 1 1 ... 1 1] mask, meaning first 2 bits
#  can be any value, but the rest of the bits must match.
#  All matching vectors are our first cluster.
#  Then we check all [x 1 x 1 1 1 ... 1 1 1]. All matches are the seconf cluster.
#  And so on.
#  There is a total of 24*23 combinations of 24 bit mask with 2 dont-cares
#  Also, we re-arrange the dataset by ciolumns (column==bit), so applying a mask of [x x 1 1 ... 1 1]
#  means that we take columnd 2,3,...,23 and find duplicates across rows.
#
#  There is a total of 24*23 choices of 22 columns out of 24.
#  Each choice of columns creates a set of N vectors, each 22bit.
#  We just sort the set, O(N*log(N)), then linearly scan and drop dupicates O(N)
#  We repeat this process for all possible selection of 22 out of 24 columns ==> 400*O(N*log(N))
#
#
# Example:
# input [0 1 0 1 0 1 0 1 0 1]
#       [0 1 0 1 0 1 0 1 1 0]
#       [0 1 0 1 0 1 0 1 1 1]
#

import sys
import time
import numpy

# select all columns except for i and j
def matrix_subset(M, i, j, columns_n):
    # assert that 0 <= i < j < num_of_columns(M)
    assert((i >= 0) and (i < j) and (j < columns_n))

    # columns between 0 and i, i+1 to j, j+1 to end, excluding i and j
    # any of the three regions can be empty
    columns = list(range(0,i)) + list(range(i+1,j)) + list(range(j+1,columns_n))

    return M[:,columns]

def merge_clusters(cluster_sizes, cluster_ids, mergeto, mergefrom):
    cluster_sizes[mergeto] += cluster_sizes[mergefrom]
    cluster_sizes[mergefrom] = 0
    cluster_ids[mergefrom] = mergeto

def get_cluster_id(cluster_ids, i):
    while cluster_ids[i] != i:
        i = cluster_ids[i]
    return i

t0 = time.time()
def print_with_timestamp(message):
    global t0
    t1 = time.time()
    print(t1 - t0, 'sec', message)
    t0 = t1

def calc_clusters(nodes_n, bits_n, nodes, debug_on):
    # transpose the matrix, columns of nodes are rows of M
    M = numpy.mat(nodes)

    # initially all clusters are of size 1 and the id is the index
    # as the algorithm progresses, linked lists are formed, similar to PCI caps list
    # For example, if nodes 0, 5, 7 belong to same cluster the arrays *might* look as follows:
    #   cluster_sizes = [ 3, 1, 1, 1, 1, 1, 1, 1, 1 ]
    #   cluster_ids   = [ 0, 1, 2, 3, 4, 0, 6, 5, 8 ]
    #       where cluster_ids[7] == 5, cluster_ids[5] == 0 and cluster_ids[0] == 0. '0' is cluster leader
    cluster_ids = [x for x in range(len(nodes))]
    cluster_sizes = len(nodes)*[1]

    print_with_timestamp('dataset ready')

    for i in range(0,bits_n-1):
        for j in range(i+1,bits_n):
            print_with_timestamp('i ' + str(i) + ', j ' + str(j))

            # select all bit columns except for i and j, and always select the last column of indices
            # sort by rows (0 == x axis)
            M_subset = matrix_subset(M, i, j, bits_n+1).tolist()
            #print(M_subset)
            M_subset.sort()

            if debug_on:
                print('pre ids', cluster_ids, ', sizes', cluster_sizes)

            # find duplicates in nodes_subset, they correspond to hamming<=2 clusters in 'nodes'
            # mark all clusters in the original 'nodes'
            node0 = M_subset[0]
            idx0 = get_cluster_id(cluster_ids, node0[-1])
            for node in M_subset[1:]:
                # compare row to row, ignore the last element - the index
                idx = get_cluster_id(cluster_ids, node[-1])
                if node0[0:-1] == node[0:-1]:
                    # TODO: cluster of size 1 is a frequent case, may deserve a special treatment
                    if idx == idx0:
                        pass # this node is already in 'idx0' cluster, nothing to do
                    else:
                        if cluster_sizes[idx0] > cluster_sizes[idx]:
                            mergeto, mergefrom = idx0, idx   # merge two clusters
                        else:
                            mergeto, mergefrom = idx, idx0   # merge two clusters
                            node0 = node
                            idx0 = idx
                        #print('merging', mergeto, '<<', mergefrom)
                        merge_clusters(cluster_sizes, cluster_ids, mergeto, mergefrom)
                else:
                    node0 = node
                    idx0 = idx

            if debug_on:
                print('post ids', cluster_ids, ', sizes', cluster_sizes)

    return len(cluster_sizes) - cluster_sizes.count(0)

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<input file>')
        return -1

    # step 1: read the input
    with open(sys.argv[1]) as f:
        line = f.readline().split()
        nodes_n, bits_n = int(line[0]), int(line[1])
        nodes = []
        index = 0
        for line in f:
            nodes.append([int(x) for x in line.split()] + [index])
            index += 1

    print_with_timestamp('done reading input, nodes_n ' + str(nodes_n))
    assert(nodes_n == len(nodes))
    assert(bits_n + 1 == len(nodes[0])) # the last element is not a bit, but the index of the array

    n = calc_clusters(nodes_n, bits_n, nodes, False)
    print('clusters', n)
    return 0

if __name__ == '__main__':
    sys.exit(main())


