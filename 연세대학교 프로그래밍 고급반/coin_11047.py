import sys


def main():
    N , k = map(int, sys.stdin.readline().split())
    coin_list =[]
    cnt =0
    for _ in range(N):
        coin_list.append(int(input()))
    for i in reversed(range(N)): # N-1 부터 0까지 
        cnt += k //coin_list[i]
        k = k% coin_list[i]
        if k ==0:
            break

    
    #while k !=0:
    #    moc =0
    #    for i in range(N):
    #        if coin_list[i]<=k<coin_list[i+1] and k//coin_list[i]>0:
    #            moc= k//coin_list[i]
    #            cnt += moc
    #            k= k%coin_list[i]
    print(cnt)



    


if __name__ == '__main__':
    main()
