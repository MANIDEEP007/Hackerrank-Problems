'''
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

For example, given the arrays a= [2,6]  and b= [24,36] , there are two numbers between them: 6 and 12. 6%2==0 ,6%6==0 ,24%6==0  and 36%6==0  for the first value. Similarly,12%2==0 ,12%6==0, 24%12==0  and ,36%12==0. The link to problem is https://www.hackerrank.com/challenges/between-two-sets/problem

Input Format

The first line contains two space-separated integers, n and m, the number of elements in array a and the number of elements in array b. 
The second line contains n distinct space-separated integers describing a[i] where 0<= i <n. 
The third line contains m distinct space-separated integers describing b[j] where 0<= j < m.

Sample Input

2 3
2 4
16 32 96

Sample Output

3
'''
import math
import os
import random
import re
import sys
def getTotalX(a, b):
    mins = a[len(a)-1] 
    maxs = b[0]
    res = 0 
    flag = 0
    for i in range(mins,maxs+1):
        flag = 0
        for j in a:
            if(i % j != 0):
                flag = 1
                break
        for j in b:
            if(j % i != 0):
                flag = 1
                break
        if(flag == 0):
            res += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()
