def solution(arr1):
    answer = 0
    arr1.sort(reverse=True)
    for i in range(N): #i=0 부터 시작 i+1 
        arr1[i] = arr1[i] * (i + 1)
    return max(arr1)
 

N = int(input())
arr = []
for _ in range(N): # _ 는 dummy variable 값을 무시하고 싶을때 사용 (_)는 변수다 
    # N의 크기만큼 반복해라
    arr.append(int(input())) #
 # N개 로프  중량 w 로프당 W/k의 부하 최대로 들수 있는 무게 N*w 
print(solution(arr))
