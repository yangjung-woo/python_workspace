from itertools import combinations

while True:
    s = list(map(int, input().split())) #로또 조합을 s 에 삽입
    #s에 input을 _구분하여 int형으로 mapping해서 list로  인가
    #list(a[8] or 배열형태등 다수 변수집합 )  
    if s[0] == 0:
        break
    del s[0]  # s[0]을 삭제
    s = list(combinations(s, 6)) # 리스트 s 의 6개로 구성된 조합들 을 다시 s에 넣음
    for i in s:  #조합들을 출력
        for j in i:
            print(j, end=' ')
        print()
    print() #1