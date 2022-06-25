def Xor (n):
    mod= n%4
    if(mod ==0): return n
    elif(mod ==1): return 1
    elif(mod==2): return n+1
    elif(mod==3): return n+1

a,b =map(int, input().split())
result= Xor(a)^Xor(b)
print(result)