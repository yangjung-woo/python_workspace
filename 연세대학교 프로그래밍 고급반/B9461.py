#p(1~10)=  1 1 2 2 3 4 5 7 9
#p(11)= 9+3 12
#p(12)= 12 +4  =16
#p(13)= 16+5  =21
#p(14)= 21 +7 =28
#P(15)= 28 +9 = 37

from collections import deque
import sys


def main():

    dq=deque()
    dq=[1,1,1,2,2,3,4,5,7,9] # P(1)~P(10) -> dq[0]~dq[9]  len 10
    flag = len(dq) -1 # 9
    T = int(sys.stdin.readline())


    for _ in range(T):
        a=int(sys.stdin.readline())
        if (a-1) > flag:
            dq=extend_dq(dq,flag+1,a)
            flag = a
        print(dq[a-1])
    
def extend_dq(dq,start,end):
    for i in range(start,end+1):
        dq_i = dq[i-1]+ dq[i-5]
        dq.append(dq_i)
    return dq

if __name__ == '__main__':
    main()
