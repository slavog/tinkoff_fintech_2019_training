n, m, k = map(int, input().split())
cities = [i for i in range(1, n+1)]
crashed = []
roads = {}
total = [0]
module = 998244353
# словарь со всеми дорогами из каждого города
for _ in range(m):
    crashed.append(input().split())
for i in range(1, n+1):
    roads[i] = [j for j in range(1, n+1) if i != j]
for z in crashed:
    roads[int(z[0])].remove(int(z[1]))
    roads[int(z[1])].remove(int(z[0]))


# исходя из нужного расстояния нужно построить маршрут
def searching_way(cur_city, step):
    if cur_city == 1 and step == k+1:
        total[0] += 1
    elif cur_city != 1 and step == k+1:
        return
    else:
        for way in roads[cur_city]:
            searching_way(way, step+1)


searching_way(1, 1)
print(*total)
