# 백만장자 프로젝트 
# 중요 point  사재기는 마지막 날에 비싸게 팔면 이득 
# => list를 뒤에서부터 순환하는게 키 포인트 
#import sys
n= int(input())

for i in range(1,n+1):
    m = int(input())
    total= 0
    arr = list(map(int,input().split()))
    #arr = list(map(int,sys.stdin.readline().split()))

    current_price =0
    for k in arr[::-1]: # last부터 순회
        if k >=current_price:  # 비교일 k 가 현재 금액보다 비싸다면 그날 파는게 가장 이득 
            current_price = k
        else:
            total = total + current_price-k

    print("#",i," ",total,sep="")

