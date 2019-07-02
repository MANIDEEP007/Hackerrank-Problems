'''
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points 
in a game. Points scored in the first game establish her record for the season, and she begins 
counting from there. The link to the problem is https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

Input Format

The first line contains an integer n, the number of games. 
The second line contains n space-separated integers describing the respective values of .
Output Format
Print two space-seperated integers describing the respective numbers of times her 
best (highest) score increased and her worst (lowest) score decreased.

Sample Input 0

9
10 5 20 20 4 5 2 25 1

Sample Output 0

2 4
'''
import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mins = None
    maxs = None
    mins_count = 0
    maxs_count = 0 
    for i in scores:
        if(mins == None):
            mins = i
        if(maxs == None):
            maxs = i
        else:
            if(mins > i): #Get Max record updated count
                mins = i
                mins_count += 1
            if(maxs < i): #Get Min record updated count
                maxs = i
                maxs_count += 1
    return (maxs_count,mins_count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
