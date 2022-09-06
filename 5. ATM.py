# 풀이
# (1) time을 받아 오름차순으로 정렬한다.(속도가 낮은 순으로 반복되어야 함)
# (2) 누적해서 더해준다.

n = input()
time = list(map(int, input().split()))

time.sort()
sum = 0
cum_sum = 0

for i in range(len(time)) : 
    sum += time[i]
    cum_sum += sum

print(cum_sum)