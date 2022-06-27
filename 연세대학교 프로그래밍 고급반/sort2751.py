import sys

n= int(input())
arr =[]
for _ in range(n):
    insert= int(sys.stdin.readline())
    # if insert not in arr:  어차피 중복수 안들어가는 문제 
    arr.append(insert)


        
arr.sort()
for i in arr:    
    print(i)
# input  보다 sys.stdlin.readline() 이 더 적게걸린다
#  
#input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,
#개행 문자를 삭제한 값을 리턴하기 때문에 느리다