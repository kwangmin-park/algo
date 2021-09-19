import sys
import copy
from collections import deque
from collections import defaultdict
import itertools

input = sys.stdin.readline

n = int(input())

graph = [sys.maxsize for _ in range(n+1)]

graph[1] = 0
for i in range(1, n):
    if i + 1 <= n and graph[i+1] > graph[i] + 1:
        graph[i+1] = graph[i] + 1
    if i * 2 <= n and graph[i*2] > graph[i] + 1:
        graph[i*2] = graph[i] + 1
    if i * 3 <= n and graph[i*3] > graph[i] + 1:
        graph[i*3] = graph[i] + 1

print(graph[n])