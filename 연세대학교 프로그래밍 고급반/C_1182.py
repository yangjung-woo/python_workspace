from itertools import combinations
import sys


def main():
    N, S = map(int,sys.stdin.readline().split())
    cnt =0
    lst= list( map(int,sys.stdin.readline().split()))
    for i in range(1,N+1):
       in_lis= (combinations(lst,i)) # combination 은 list 반환 
       for k in in_lis:
        if sum(k)==S:
            cnt+=1
    print(cnt)




if __name__ == '__main__':
    main()



