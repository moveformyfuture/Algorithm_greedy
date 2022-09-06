
n, k = map(int, input().split())
result = 0

while (n >= k) :
    if (n % k == 0) : 
        n //= k
        result += 1
    else : 
        n -= 1
        result += 1
while (n < k) :
    n -= 1
    result += 1

print(result)