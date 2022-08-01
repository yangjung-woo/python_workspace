import sys


def main():
    dic ={}
    newdic = {}
    cnt = 0
    while True:
        in_arr = sys.stdin.readline().rstrip()
        if not in_arr:
            break
        
        if in_arr in dic:
            dic[in_arr] += 1
            
        else: 
            dic[in_arr] =1
            
        cnt +=1
    #name_list = list(dic.keys())
    #name_list.sort()
    #for tree in name_list:
    #    print("%s %.4f" %(tree , dic[tree]/cnt*100))

    newdic= dict(sorted(dic.items()))
    
    for key , value in newdic.items():
        print ("%s %.4f" %(key , value/cnt*100))

    


if __name__ == '__main__':
    main()