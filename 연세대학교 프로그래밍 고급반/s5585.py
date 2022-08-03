import sys

def main():
    N = int(input())
    M=1000-N
    cnt =0
    while M !=0:

        if M >= 500:
            M = M -500
            cnt +=1
        elif M>= 100:
            M=M-100
            cnt +=1
        elif M>= 50:
            M=M-50
            cnt +=1
        elif M>= 10:
            M=M-10
            cnt +=1
        elif M>= 5:
            M=M-5
            cnt +=1
        elif M >=1:
            M=M-1
            cnt +=1
            
    print (cnt)




    


if __name__ == '__main__':
    main()
