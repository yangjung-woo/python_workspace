import sys
from collections import deque
def suger_calculator(now_suger,now_l):
    if now_suger>=now_l:
        # return now suger
    else: 
        #재귀호출
n,m = map(int ,input().split())
s_list =deque()

parent =0
son =0
for i in range(n):
    a,b  =map(int,sys.stdin.readline().split()) #   a =L , b =suger   1L 당 suger: b/a
    s_list.append([b/a,a,b])

s_list.sort(reverse=True) # L 당 설탕수  내림차순 정렬

suger_calculator(0,m)

