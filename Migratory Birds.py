'''
You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number. The link to problem is https://www.hackerrank.com/challenges/migratory-birds/problem

Input Format:

The first line contains an integer denoting n, the number of birds sighted and reported in the array ar. 
The second line describes 
ar as n space-separated integers representing the type numbers of each bird sighted.

Output Format:

Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.
'''
import math
import os
import random
import re
import sys
def migratoryBirds(arr):
    sl = list(set(arr))
    sl.sort()
    L = []
    for i in sl:
        L.append(arr.count(i))
    max_index = sl[L.index(max(L))]
    return max_index 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
