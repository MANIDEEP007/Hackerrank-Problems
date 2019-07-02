'''
Sam’s house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where s is the start point, and i is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b. 
The link to problem is https://www.hackerrank.com/challenges/apple-and-orange

Input Format

The first line contains two space-separated integers denoting the respective values of  and . 
The second line contains two space-separated integers denoting the respective values of  and . 
The third line contains two space-separated integers denoting the respective values of  and . 
The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point . 
The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .

Sample Input 0

7 11
5 15
3 2
-2 2 1
5 -6
Sample Output 0

1
1
'''
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    res = 0
    for i in apples: #Loop that counts number of apples falling on Sam house
        if(i > 0 and i+a >=s and i+a <=t):
            res += 1
    print(res)
    res = 0
    for i in oranges: #Loop that counts number of oranges falling on Sam house
        if(i< 0 and b + i <= t and b+i>=s):
            res+=1
    print(res)
           
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
