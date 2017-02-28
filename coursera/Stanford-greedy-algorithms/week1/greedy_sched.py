#!/usr/local/bin/python3

import sys

def schedule_jobs_by_delta(weight, length):
    jobs = list(zip(weight,length))
    # sort in decreasing order by (weight - length)
    jobs.sort(key = lambda jb: jb[0] - jb[1], reverse=True)


    C=0 # current completion time
    WS=0 # weighted sum of completion times

    while jobs:

        # get all jobs with same 'delta'
        delta = jobs[0][0] - jobs[0][1]
        jobs_same_delta = [jobs.pop(0)]

        while jobs:
            if delta == jobs[0][0] - jobs[0][1]:
                jobs_same_delta.append(jobs.pop(0))
            else:
                break

        print(len(jobs_same_delta))
        if len(jobs_same_delta) == 9:
            print(jobs_same_delta)

        # sort by weight in decreasing order
        jobs_same_delta.sort(key = lambda jb: jb[0], reverse=True)

        if len(jobs_same_delta) == 9:
            print(jobs_same_delta)

        # accumulate completion time and weight sum of completion times
        for j in jobs_same_delta:
            C += j[1]
            WS += C * j[0]

    print('total_completion_time', WS)

def schedule_jobs_by_ratio(weight, length):
    jobs = list(zip(weight,length))
    # sort in decreasing order by weight/length
    jobs.sort(key = lambda jb: jb[0] / jb[1], reverse=True)

    C=0 # current completion time
    WS=0 # weighted sum of completion times

    for j in jobs:
        C += j[1]
        WS += C * j[0]

    print('total_completion_time', WS)

def main():
    if len(sys.argv) != 2:
        print('USAGE:', sys.argv[0], '<jobs file>')

    weight=[]
    length=[]
    with open(sys.argv[1]) as f:
        n = int(f.readline())
        for line in f:
            pair = line.split()
            weight.append(int(pair[0]))
            length.append(int(pair[1]))

    schedule_jobs_by_delta(weight, length)
    schedule_jobs_by_ratio(weight, length)

if __name__ == '__main__':
    sys.exit(main())
