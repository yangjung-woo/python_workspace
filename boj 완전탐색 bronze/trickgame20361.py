import sys
n,x,k = map(int ,input().split()) # n개컵 x 정답위치 k 교체횟수 
gold = x

for i in range(k):
    a , b =map(int, sys.stdin.readline().split())
    if a ==gold:
        gold =b
    elif b==gold:
        gold=a
    else: pass
print(gold)



