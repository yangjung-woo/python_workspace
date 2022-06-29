
def lookin(lis):
    now_max= lis[0]
    cnt =1
    for j in lis:
        if j > now_max: 
            cnt+=1
        now_max =max(now_max, j)
    return cnt

n =int(input())
li = [int(input()) for i in range(n)]

print(lookin(li))
li.reverse()
print(lookin(li))
