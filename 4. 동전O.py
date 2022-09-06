# 풀이
# (1) data를 하나씩 입력
# (2) reversed(data) 함수로 list의 뒤에서 부터 가져오기
# (3) 몫(//), 나머지(%)를 이용해 반복

n, k = map(int, input().split()) # n, k를 입력받음
coin_lst = list()

for i in range(n):
    coin_lst.append(int(input())) # data를 하나씩 입력받음

count = 0

for i in reversed(range(n)): # reverse(data) : data를 역순으로 불러옴
    count += k//coin_lst[i] # 카운트 값에 K를 동전으로 나눈 몫을 더해줌
    k = k % coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)