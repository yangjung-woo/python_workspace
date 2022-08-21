import sys

def multi(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = multi(n, k//2)
    if k % 2:
        return tmp * tmp * n % 1000000007
    else:
        return tmp * tmp % 1000000007

def demofac(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % 1000000007
    return n

def main():
    N,K = map(int, input().split())
    top = demofac(N)
    bot = demofac(N-K) * demofac(K) % 1000000007

    print(top * multi(bot, 1000000007-2) % 1000000007)
    


if __name__ == '__main__':
    main()
