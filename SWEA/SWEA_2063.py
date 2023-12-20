# D1 중간값 찾기 
# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

#입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라
# 1. N은 항상 홀수로 주어진다
N = int(input())

arr = list(map(int , input().split()))

sort_arr=sorted(arr)

print(sort_arr[N//2])

# 만약 N =  짝수개 면 
# print (() sort_arr[N//2 -1 ]  + sort)arr[N//2]   ) /2  )