

import sys
n= int(input())

for i in range(1,n+1):
    #arr = list(map(int,input().split()))
    arr = list(map(int,sys.stdin.readline().split()))
    answer = round(sum(arr)/10)
    print("#%d" %i,answer)