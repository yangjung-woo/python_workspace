
N = int(input())
picture =[]
minimum = 36
pic_a =pic_b =0
for i in range(N):
    row =[]
    for j in range(5):
        row.append(input())
    picture.append(row)
for A in range(N):
    for B in range(A+1,N):
        cnt =0
        for horizon in range(5): #가로
            for vertex in range(7): #세로
                if picture[A][horizon][vertex] != picture[B][horizon][vertex]:
                    cnt+=1
        if minimum>cnt:
            minimum=cnt
            pic_a= A+1
            pic_b =B+1

print(pic_a , pic_b)
