import sys



def main():

    y ,x = map(int, sys.stdin.readline().split())
    blocks_height =list(map(int,sys.stdin.readline().split()))
    goim =0
    total =0
    for i in range(1,x-1):
        left_max= max(blocks_height[:i])
        right_max =max(blocks_height[i+1:])
        high_gap= min(left_max,right_max)
        if high_gap <= blocks_height[i] :
            goim =0
        else: # high_gap > 현재위치 블록 즉 물이 고일수 있음
            goim =high_gap -blocks_height[i]
        total +=goim 

    print(total)
if __name__ == '__main__':
    main()

 