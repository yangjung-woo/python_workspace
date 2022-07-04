N =int(input())
deli_list =[-1 for _ in range(N+1)]


for i in range(0,N+1):
    insert_a =78888
    insert_b=78888
    insert_c=78888
    insert_d=78888

    if deli_list[i-3] !=-1:
       insert_a= deli_list[i-3]+1
    if deli_list[i-5] !=-1:
        insert_b= deli_list[i-5]+1
    if i %3 ==0:
        insert_c = i/3
    if i %5 ==0:
        insert_d = i/5

    deli_list[i]=min(insert_a,insert_b,insert_c,insert_d)

if deli_list[N]== 78888:
    print(-1)
else:
    print(deli_list[N])
