cm_list=[]
for _ in range(9):
        cm_list.append( int(input()) )
total =sum(cm_list)
for i in range(9):
    for j in range(i+1,9):
        if 100 == (total - (cm_list[i] + cm_list[j])): 
            num1,num2=cm_list[i],cm_list[j]
            cm_list.remove(num1)
            cm_list.remove(num2)
            if len(cm_list) ==7:
                cm_list.sort() # 오름차순 정리
                for i in range(len(cm_list)):
                    print(cm_list[i])
                break
    if len(cm_list) ==7:
        break

        
    


