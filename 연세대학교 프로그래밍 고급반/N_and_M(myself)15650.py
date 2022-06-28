from itertools import combinations


n,m=map(int,input().split()) # 1~N 중  오름차순 수열을 만족하는 조합 m개 출력
#permutation(list,n) 순열  n개 
#combination(list,n) 조합 n 개 
#product (list_a, list_b,list_c..) list a, b,c 에서 1개씩 포함하는 조합 생성
arr = []
for i in range(1,n+1):
    arr.append(i)

combi_arr=list(combinations(arr,m))
for j in combi_arr:
    print(j)
