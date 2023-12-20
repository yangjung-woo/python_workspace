# 준환이의 운동관리 D3??

print("program is start")

# 하루에 L분 이상 U 분 이하 운동
# 준환이는 X 분만큼 운동을 ㅏㅁ 
# 제한되어있는 시간을 넘은 운동을 했는지 , 몇분 더 해ㅑ 제한을 푸는지 출력 
tc = int(input())

for i in range(1,1+tc):
    L , U , X = map(int, input().split())
    if X < L:
        result = L-X
    else:
        if X>U:
            result = -1
        else:
            result = 0

    print('#{} {}'.format(i , result))