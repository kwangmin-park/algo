import sys
import copy
from collections import deque
from collections import defaultdict
import itertools

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
graph.reverse()

for i in range(n-1):
    copy_graph = copy.deepcopy(graph[i+1])
    for j in range(len(graph[i])):
        if j > 0:
            graph[i+1][j-1] = max(graph[i+1][j-1], copy_graph[j-1] + graph[i][j])
        if j < len(graph[i]) - 1:
            graph[i + 1][j] = max(graph[i + 1][j], copy_graph[j] + graph[i][j])
print(graph[-1][0])