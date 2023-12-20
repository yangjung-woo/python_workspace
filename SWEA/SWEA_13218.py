# 조별과제 문제
print("program is start \n")
T = int(input())

for i in range(1,1+T):
    n = int(input())
    print('#{} {}'.format(i, n//3))
    # 메모리 할당이나 시간 초과문제가 있을수 있기때문에
    #  최대한 새로운 변수는 지양