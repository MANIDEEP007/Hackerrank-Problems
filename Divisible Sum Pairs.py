'''
You are given an array of n integers, a0,a1,..,an-1, and a positive integer,k. Find and print the number of (i,j)pairs where ai+aj is evenly divisible by K. The link to the problem is https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

Sample Input

6 3
1 3 2 6 1 2

Sample Output

5
'''
import os
import random
import re
import sys
def divisibleSumPairs(n, k, ar):
    L = []
    for i in range(0,len(ar)):
        for j in ar[i+1:]:
            L.append([ar[i],j])
    res = 0
    for i in L:
        if(sum(i)%k==0):
            res+=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
