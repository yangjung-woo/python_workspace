from math import factorial
import sys

def main():
    N,K = map(int, input().split())
    res=1
    for i in range(1,N+1):
        res= (res*i)%K
    print(res)


    


if __name__ == '__main__':
    main()
