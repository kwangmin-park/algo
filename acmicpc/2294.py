import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

graph = [sys.maxsize for _ in range(k+1)]
for coin in coins:
    if coin < k + 1:
        graph[coin] = 1

for i in range(k):
    if graph[i] != sys.maxsize:
        for coin in coins:
            if i + coin < k+1 and graph[i+coin] > graph[i] + 1:
                graph[i+coin] = graph[i] + 1
if graph[k] == sys.maxsize:
    print(-1)
else:
    print(graph[k])