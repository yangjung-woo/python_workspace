import sys
import math

def main():
    N,M =map(int, sys.stdin.readline().split())
    total =1
    for i in range(M):
        total =total *(N-i)
    sub= math.factorial(M)
    print (total//sub)

if __name__ == '__main__':
    main()