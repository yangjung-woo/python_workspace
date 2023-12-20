import sys

#def isprime(input):
#    for i in range(2,math.sqrt(input)):
#        if input % i ==0:
#            return False
#        else:
#            return True

n= int(input())

for i in range(1,n+1):
    sum=0
    arr = map(int,sys.stdin.readline().split())
    for ai in arr:
        if ai%2 !=0:
            sum=sum+ai
    print("#"+str(i),str(sum))



