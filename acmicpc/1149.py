import sys
import copy
from collections import deque
from collections import defaultdict
import itertools

input = sys.stdin.readline

n = int(input())
colors = [[sys.maxsize for _ in range(3)] for _ in range(n+1)]
graph = [[sys.maxsize for _ in range(3)] for _ in range(n+1)]

for i in range(1, n+1):
    color = list(map(int, input().split()))
    for j in range(3):
        colors[i][j] = color[j]

graph[1] = colors[1]
for i in range(1, n):
    graph[i+1][0] = min(graph[i][1], graph[i][2]) + colors[i+1][0]
    graph[i+1][1] = min(graph[i][0], graph[i][2]) + colors[i+1][1]
    graph[i+1][2] = min(graph[i][0], graph[i][1]) + colors[i+1][2]

print(min(graph[n]))
a = 3
