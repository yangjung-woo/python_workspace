k,n =map(int, input().split())
cm_list =[]
for _ in range(k):
    cm_list.append(int(input()))
bottom ,top = 1, max(cm_list)    # 길이 최솟값 최댓값
while bottom <= top:
    mid =(bottom+top)//2
    cnt =0
    for i in cm_list:
        cnt += i//mid
    if cnt >= n:
        bottom =mid +1
    else:
        top=mid-1
print(top)


