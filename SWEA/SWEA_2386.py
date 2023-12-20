#2386. [AtCoder Beginner Contest 073] C. Write and Erase D3
T = int(input())

for tc in range(1,1+T):
    N = int(input())
    a_list = []
    for n in range(N):
        a = int(input())
        if a in a_list:
            #a_list.pop(a_list.index(a)) # pop은 N 번째 원소를 삭제 
            a_list.remove(a) # remove 는 해당 원소를 삭제 
        else:
            a_list.append(a)
    answer = len(a_list)

    print(f'#{tc} {answer}')