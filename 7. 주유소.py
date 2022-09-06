# 풀이 : 도시를 지나가면서 min_cost를 갱신
# (1) min_cost 초기화
# (2) 도시를 지나가면서 min_cost와 현재 cost를 비교하여 갱신

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0] #첫 기름값
sum = 0
for i in range(N-1): # 마지막 목적지는 의미 없으므로 n-1
    if min_cost > costs[i]: # 이전 기름값과 현재 기름값 비교
        min_cost = costs[i]
    sum += (min_cost * roads[i])
    
print(sum)