import sys
import copy
from collections import deque
from collections import defaultdict
import itertools

input = sys.stdin.readline

n = int(input())

graph = [sys.maxsize for _ in range(n+1)]
graph[0] = 0
bag_list = [3, 5]

dq = deque()
dq.append((0))
while dq:
    cur = dq.popleft()
    for bag in bag_list:
        if cur + bag <= n and graph[cur+bag] > graph[cur] + 1:
            graph[cur+bag] = graph[cur] + 1
            dq.append((cur + bag))

if graph[n] == sys.maxsize:
    print(-1)
else:
    print(graph[n])
