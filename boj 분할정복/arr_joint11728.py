import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    arr_1 =list(map(int, sys.stdin.readline().split()))
    arr_2 =list(map(int, sys.stdin.readline().split()))
    #result = arr_1 + arr_2
    #result.sort()
    #print(*result)
    # 분할정복
    answer =[]
    pointer_1 =0
    pointer_2 =0
    lenth_1 =len(arr_1)
    lenth_2 =len(arr_2)
    while pointer_1 != lenth_1 or pointer_2 != lenth_2:
        if pointer_1 == lenth_1:
            answer.append(arr_2[pointer_2])
            pointer_2 += 1
        
        elif pointer_2 == lenth_2:
            answer.append(arr_1[pointer_1])
            pointer_1 += 1
        else:
            if arr_1[pointer_1] < arr_2[pointer_2]:
                answer.append(arr_1[pointer_1])
                pointer_1 += 1
            else:
                answer.append(arr_2[pointer_2])
                pointer_2 += 1
    print(*answer)


if __name__ == '__main__':
    main()


