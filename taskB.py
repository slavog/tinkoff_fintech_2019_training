K, N = map(int, input().split())
dist_north = []
dist_between = []
n = 1
result_list = []
for village in range(N):
    dist_north.append(int(input()))
for village in range(N-1):
    x = dist_north[n] - dist_north[n-1]
    dist_between.append(x)
    n += 1
dist_between.append(K - dist_north[-1] + dist_north[0])
for _ in dist_between:
    result_list.append(sum(dist_between) - _)
print(min(result_list))
