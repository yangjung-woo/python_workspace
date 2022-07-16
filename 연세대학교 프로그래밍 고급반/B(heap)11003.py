import heapq
import sys
def D_list(lists):
    heapq.heapify(lists)
    print_list = lists[0]
    return print_list

def main():
    N ,L= map(int,sys.stdin.readline().split())
    arr =list(map(int,sys.stdin.readline().split()))
    
    prt=[]
    for i in range(N):
        temp_list =[]
        start = i -L+1
        if (start <=0):   
            temp_list = arr[0:i+1]
        else:
            temp_list = arr[start:i+1]

        arg=D_list(temp_list)
        print(arg, end=' ')


    

   

if __name__ == '__main__':
    main()





