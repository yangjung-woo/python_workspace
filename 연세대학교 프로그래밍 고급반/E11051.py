from math import factorial
import sys

def main():
    N,K = map(int, input().split())
    top= 1

    for i in range(K):
        top= top*N
        N-=1
    print ((top // factorial(K)) % 10007)
    


if __name__ == '__main__':
    main()
