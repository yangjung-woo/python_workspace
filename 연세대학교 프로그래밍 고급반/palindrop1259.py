#answer ="yes"

# list [ a:b :c ]  : a~ b까지 C 간격으로  if c<0 역순으로
# answer[::-1]  = sey
while(1):
    x= int(input())
    if (x==0):break
    else:
        str_x= str(x)

        if str_x == str_x[::-1]:
            print("yes")
        else: print("no")
