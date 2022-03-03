def solution():
    answer = 0
    arr.sort(reverse=True)
    for i in range(N): #i=0 부터 시작하므로 i+1 
        arr[i] = arr[i] * (i + 1)
    return max(arr)
 

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
 # N개 로프  중량 w 로프당 W/k의 부하 최대로 들수 있는 무게 N*w 
print(solution())