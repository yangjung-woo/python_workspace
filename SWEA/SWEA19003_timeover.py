# 팬린드롬 문제 D3   정답률 32.03
# N: 문자열 갯수 , M 문자열 길이 
from itertools import permutations # 순열 
#from itertools import combinations # 조합 

def check_penlindrop(strs):
    
    if strs[: :] == strs[: :-1]:
        return len(strs)
    else:
        return 0
'''
li = []
als = []
for _ in range(3):
    li.append(str(input()))# 한 문자씩 넣고 싶을땐 list(string )
for i in range(1,4):
    a =list(map(''.join, permutations(li,i))) # 순열 혹은 조합을 list형식으로 바꾸려면 list(permutate (list , i))    문자열들로 나타내려면  list( map(''.join, permutate()  ) 
    als.append(a)   # 리스트 내 문자열 끼리 합치기  "".join(list)

print(sum(als,[])) # 리스트 끼리 합칠수도 았다  sum(list,[])

'''
T = int(input())


for tc in range(1,T+1):
    li = []
    als = []
    maximum = 0 # 케이스마다 초기화 
    N,M = map(int, input().split())
    for i in range(N):
        li.append(input())
    for j in range(1+N):
        temp = list(map(''.join, permutations(li,j)))
        als.append(temp)
    arr_list = sum(als,[])

    for check in arr_list:
        if maximum < check_penlindrop(check):
            maximum = check_penlindrop(check)
    
    del(li,als)
    answer = maximum

    print("#{} {}".format(tc , answer))

