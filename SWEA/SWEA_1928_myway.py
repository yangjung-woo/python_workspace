# base 64 디코딩 문제 
# dic 리스트에 인코딩 값 넣기
dic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/' ]

# 문자에 해당하는 index를 받아옴 
# index 를  binary  이진법으로 표현한다 그리고 맨 앞 
# bin(8) = '0b1000'  맨앞 0b는 지워주기 위해 bin(8)[2:]  

# 64 를 포현할 수 표현 할 수 있는 6bit 단위 문자열이 생성되야함 
# 부족한 갯수만큼 0을 채워줘야 함 

# base 64인코딩 원리 : 8bit 바이너리 파일을 6bit 로 표현한다
T = int(input())

for tc in range(1,1+T):
    line = list(input())
    
    value = ""
    for i in range(len(line)):
        num =dic.index(line[i])
        bin_num = bin(num)[2:]

        while len(bin_num)<6:
            bin_num = '0'+bin_num
        value += bin_num# 6비트씩 끊어서 이어 붙임 
    answer = ""
    for j in range(len(line)*6 // 8): # 6비트를 8비트로 나누어보자 
        data = int(value[j*8 : j*8+8], 2) # 8 비트 단위로 slicing 해서 
        # string 을 이진수로 표현한 data 
        answer += chr(data)

    print('#%d %s' % (i, answer))
