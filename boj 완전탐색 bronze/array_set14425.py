import sys


def main():
    N,M =map(int,sys.stdin.readline().split())
    arr_list=[]
    cnt = 0
    for _ in range(N):
        arr_list.append(sys.stdin.readline().rstrip())
    for i in range(M):
        arr=sys.stdin.readline().rstrip()
        if sys.stdin.readline().rstrip() in arr_list:
            cnt +=1
    print(cnt)
if __name__ == '__main__':
    main()