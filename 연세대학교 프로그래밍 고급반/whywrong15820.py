s1, s2 = map(int, input().split())
li1 = [list(map(int, input().split())) for _ in range(s1)] #샘플 케이스 
li2 = [list(map(int, input().split())) for _ in range(s2)] # 테스트 케이스 
for i in range(s1):
    if li1[i][0] != li1[i][1]:  # 샘플중 하나라도 틀리면 wrong
        print("Wrong Answer")
        exit()
for i in range(s2):
    if li2[i][0] != li2[i][1]: # 샘플은 맞았으나 테스트 wrong
        print("Why Wrong!!!")
        exit()
print("Accepted") #sample & test right
