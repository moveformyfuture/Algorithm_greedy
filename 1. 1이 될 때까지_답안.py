
n, k = map(int, input() .split())
result = 0
# N 이 K 이상이라면 K로 계속 나누가
while n >= k:
# N 어 K 로 나누어 떨 어 지지 않는다면 N 에서 1 씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
# K로 나누기
    n //= k
    result += 1
# 마지막으로 남은 수얘 대하여 1 씩 빼기
while n > 1:
    n -= 1
    result += 1
print(result)