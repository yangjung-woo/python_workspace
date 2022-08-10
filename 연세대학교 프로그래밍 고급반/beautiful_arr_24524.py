import sys
from this import s


def main():
    S = input()
    T = input()

    arr = [0 for _ in T]  # l[k] = t[k]까지 있는 것의 개수
    t_set = set(T) # 확인하기 편하게 만든 것
    for x in s: # s에 대해 순회
        if x in t_set:  # x가 일단 t안에 있으므로 go!
            if x == T[0]:  # idx == 0 인 경우
                arr[0] += 1
            else:
                idx = T.find(x)  # 현재 x 는 t의 몇번째 idx인지 반환
                if arr[idx - 1]: # t[idx-1] 까지 만들 수 있었다면
                    arr[idx - 1] -= 1 # t[idx-1] 까지 만들 수 있는 경우의 수 하나를 빼고
                    arr[idx] += 1 # t[idx] 까지 만들 수 있는 경우의 수로 편입



    


if __name__ == '__main__':
    main()
