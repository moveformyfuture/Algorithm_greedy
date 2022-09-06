# 풀이
# (1) 한 줄씩 입력받아 행의 최소값을 확인한다. min(data)
# (2) 입력받은 최소값의 대소를 비교하여, 최댓값을 출력한다. max(data1, data2)

n, m = map(int, input().split()) # 데이터 입력 받기
result = 0

for i in range(n) : # 행의 개수만큼 반복
    data = list(map(int, input().split())) # 행을 한줄씩 입력받기

    min_value = min(data)
    result = max(min_value, 0)

print(result)


