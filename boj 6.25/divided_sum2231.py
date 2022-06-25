n =int(input())
sangsungja =[]
total = 0
for i in range(n+1):
    arr= list(map(int,str(i)))
    total = i +sum(arr)
    if (total)==n: 
        print(i) 
        break
    if i==n:
        print(0)
