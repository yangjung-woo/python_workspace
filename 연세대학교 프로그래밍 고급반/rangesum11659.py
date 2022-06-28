n,m=map(int,input().split())
arr = list(map(int,input().split()))
sum_list =[0]
temp =0
for i in arr:
    temp +=i
    sum_list.append(temp)

for _ in range(m):
    start ,end = map(int,input().split())
    print (sum_list[end]-sum_list[start-1])

# 오답이유 sum 을 반복마다 호출시 시간복잡도 O(n*m)이 된다 따라서 미리 arr 구간 합을 구해놓으면  O(N+M)으로 단축할수 있다
#for _ in range(m):
#    start ,end = map(int,input().split())
#    print(sum(arr[(start-1):(end)]))
# pypy 3 okay     // python3  runtime error
