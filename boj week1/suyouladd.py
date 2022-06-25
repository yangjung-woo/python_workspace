N, L = map(int, input().split()) #합이 N이면서 최소 길이가 L+1인 수열
# input을 띄어쓰기 구분해서 각각 N 와 L에 int형으로 인가 
# map(형태(int , float, str), 변수or 입력값)


x = []


def get_arr(length, N):
    x = N - (length * (length+1) // 2)  #첫째항 
    return x / length

for i in range(L, 101):

    a = get_arr(i, N)
    if int(a) == a :
        a = int(a)
        sub_sum = sum(range(a+i+1)) - sum(range(a+1))
        if sub_sum == N :
            x = (list(range(a + 1, a + i + 1)))
            x = list(map(str, x))
            break

print(' '.join(x) if x != [] and len(x) <= 100 else -1)
#1