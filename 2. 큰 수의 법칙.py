# 풀이 : 가장 큰 수를 K번 더하고, 두번째 큰 수를 한번 더한다.
n, m, k = map(int, input().split()) # n, m, k를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기

data.sort() # 입력받은 데이터 오름차순 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째 큰 수

result = 0

while True :
    if (m != 0) :
        for i in range(k) :
            result += first
            m -= 1
            if (m == 0):
                break

        result += second
        m -= 1

    if (m==0) :
        break

print(result)

