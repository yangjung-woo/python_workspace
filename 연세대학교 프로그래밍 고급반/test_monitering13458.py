import sys
def main():
    cnt =0
    N = int(sys.stdin.readline())
    A_lis =list(map(int,sys.stdin.readline().split()))
    B,C = map(int,sys.stdin.readline().split())
    for i in range(len(A_lis)): # 모든 방에 총 감독 배정
        A_lis[i]= A_lis[i]-B
        cnt+=1
        if A_lis[i] >0:
            if A_lis[i]% C !=0:
                plus_cnt=A_lis[i] // C +1
            else:
                plus_cnt =A_lis[i]//C
            cnt +=plus_cnt
    print(cnt)


if __name__ == '__main__':
    main()
