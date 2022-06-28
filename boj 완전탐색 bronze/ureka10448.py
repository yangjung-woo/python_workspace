# Tn = n(n+1)/2   모든 자연수는 3개의 Tn으로 표현가능한데 아닌경우의 수를 구하는 프로그램 작성

def  isthatTrue (input):
    for j in total:
        for k in total:
            for l in total:
                if(input==j+k+l): return 1
    return 0

n =int(input())
arr=[]
total=[]
a=1
# 모든 삼각수 미리 계산해서 total list 에 저장

while ((a) *(a+1) /2 <1000):
    total.append((a) *(a+1) /2)
    a+=1



for _ in range(n):
    arr.append(int(input()))
for _ in range(n):
    print(isthatTrue(arr[_]))




