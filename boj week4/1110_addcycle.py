n =int(input())
origin= n
cnt =0

while(1):
    a= n // 10
    b= n % 10
    c=(a+b)%10
    n=(b*10) +c
    cnt = cnt +1
    if(origin==n):break
print(cnt)
   
        
      



