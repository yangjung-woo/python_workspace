import sys


N =int(input())
attack_list=[]
slice_list =[] # 기울기 저장
total =0
for i in range(N):
    x1 ,y1 ,x2 ,y2,w =map(int,sys.stdin.readline().split())
    attack_list.append([w,x1 ,y1 ,x2 ,y2])
     # 0 1 2 3 4
attack_list.sort(reverse=True)

for k in attack_list:
    if len(slice_list)==0:
        total =k[0]
        slice_list.append(abs(k[4]-k[2])/abs(k[3]-k[1])) 
    else 
