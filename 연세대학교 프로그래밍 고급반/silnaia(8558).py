import sys


def main():
    N = int(sys.stdin.readline())
    result =1
    for i in range(2,N+1):
        result *= i
    result %= 10
    print(result) 




if __name__ == '__main__':
    main()





