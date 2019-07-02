'''
You are choreograhing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location as part of the show.
Complete the function kangaroo which takes starting location and speed of both kangaroos as input, and return  or  appropriately. Can you determine if the kangaroos will ever land at the same location at the same time? The two kangaroos must land at the same location after making the same number of jumps.
The link to the problem is https://www.hackerrank.com/challenges/kangaroo/problem
'''
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if(x1 == x2): #Already Meet
        return "YES"
    elif(v1 > 0 and v2 < 0): #Never Meet
        return "NO"
    elif(v1 < 0 and v2 > 0): #Never Meet
        return "NO"
    else:
        for i in range(10000): #Check Whether can meet
            if((x1+i*v1)==(x2+i*v2)): #Will Meet 
                return "YES"
                break 
        else:
            return "NO" #Never Meet
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
