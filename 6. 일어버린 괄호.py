# 풀이 : -를 만날때 가장 큰 수를 뺀다.
# (1) -를 뺀 체로 데이터를 입력받는다.
# (2) 더해야 하는 값을 마지막에 빼준다.


arr = input().split('-') # -를 뺀 체로 데이터를 입력받기
sum = 0

# arr[0]에서 +를 기준으로 나눈 후 + 실행
for i in arr[0].split('+'):
    sum += int(i)

# arr[1:]의 값을 sum에서 모두 빼주기
for i in arr[1:]:
    for j in i.split('+'):
        sum -= int(j)
        
print(sum)