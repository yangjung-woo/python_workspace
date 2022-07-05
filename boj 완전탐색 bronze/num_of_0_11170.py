import sys


T = int(input())
for i in range(T):
    cnt =0
    start , finish =map(int,sys.stdin.readline().split())
    for j in range(start, finish+1):
        temp_str =str(j)
        for k in temp_str:
            if k =='0':
                cnt+=1
    print(cnt)

