# a b 학생 x y 만큼 멀리뛰기 시작위치  p q 뛰는거리 x y  최소공배수 
import sys


x,y,p,q =map(int,sys.stdin.readline().split())

for i in range(100):
    for j in range(100):
        if(p + x*i == q + y*j):
            print(p + x*i)
            exit()

print(-1)