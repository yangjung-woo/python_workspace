import sys


def main():

    T = int(sys.stdin.readline())
    for _ in range(T):

        flag = True
        call_list = []
        N= int(sys.stdin.readline())
        for _ in range(N):
            call_list.append(sys.stdin.readline().rstrip())
        call_list.sort()

        for i in range(len(call_list)-1):  # 정렬하기 때문에 모든 문자열을 비교하는 이중 for문 대신 가까운 문자열 2개만
            if call_list[i] == call_list[i+1][0:len(call_list[i])]:
                flag = False
                print("NO")
                break
        if flag == True:
            print("YES")

if __name__ == '__main__':
    main()

 