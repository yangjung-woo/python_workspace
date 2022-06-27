from itertools import combinations

n,m =map(int,input().split())
arr = list(map(int,input().split()))
total=0
total_list =[]
arr.sort
for i in range(len(arr)):
  if (arr[i]>m): arr.pop(arr[i])

combi= list(combinations(arr,3))

for k in range(len(combi)):
    total = sum(combi[k])#for l in combi[k]:    total+= l
    if (total<=m): total_list.append(total) 
    total =0 
total_list.sort(reverse =True)
print(total_list[0])
