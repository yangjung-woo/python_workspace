import sys

def main():
    N = int(input())
    lis=[]
    for _ in range(N):
        deadline,score = map(int,input().split())  # day , rate
        lis.append((deadline,score))
    lis.sort() # 튜플 정렬 1순위 deadline 2 순위 score 오름차순 정렬
    do = []
    date = lis[-1][0] # deadline이 가장 큰
    answer =0
    while True:
        if date ==0:
            break
        while lis and lis[-1][0]>= date:
            do.append(lis.pop()[1])
            if not lis:
                break
        date -=1
        if not do:
            continue
        do.sort()
        answer +=do.pop()
    print(answer)


    


if __name__ == '__main__':
    main()
