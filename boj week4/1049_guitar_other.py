
n, m = map(int, input().split())
six_packacge=list()
one_thing= list()

for i in range(m):
    a,b=map(int, input().split())
    six_packacge.append(a)
    one_thing.append(b)

lowest_six =min(six_packacge)
lowest_one =min(one_thing)
if lowest_six< lowest_one*6:  # 패키지 최솟값이 낱개보다 작을때 여기를 간과
   
   ## 6개 미만을 구매할 경우 
    if(lowest_six<(n%6)*lowest_one): #6개짜리를 구매하는게 더 싸다   
        print( (n//6)*lowest_six + lowest_six)
    else: # 6개미만은 낱개를 사는게 더 싸다 
        print((n//6)*lowest_six +(n%6)*lowest_one)

else:print(n*lowest_one) #패키지 값보다 낱개로사는게 더 쌀 경우 