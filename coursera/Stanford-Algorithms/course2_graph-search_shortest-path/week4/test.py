#!/usr/bin/env python3

import sys
import two_sum

if __name__ == '__main__':
    test_A = [ -3, -1, 1, 2, 9, 11, 7, 6, 2 ]
    count = two_sum.count_2sum_in_range(test_A, 3, 10)
    print(test_A, count)
