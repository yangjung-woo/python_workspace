N =int(input())
F_list = [0,1,1]

for i in range (3,N+1):
    inserts= F_list[i-1]+F_list[i-2]
    F_list.append(inserts)

print(F_list[N])