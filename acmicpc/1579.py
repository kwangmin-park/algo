import sys
import copy
from collections import deque
from collections import defaultdict
import itertools

input = sys.stdin.readline

n = int(input())
step = [0 for _ in range(n+1)]
graph = [[0 for _ in range(2)] for _ in range(n+1)]

for i in range(1, n+1):
    step[i] = int(input())
    
if n == 0:
    print(0)
    sys.exit(0)
elif n == 1:
    print(step[1])
    sys.exit(0)
elif n == 2:
    print(step[1]+step[2])
    sys.exit(0)

graph[1][1] = step[1] # 0 : 그 전 스텝과 연속
graph[1][0] = step[1] # 0 : 그 전 스텝과 연속
graph[2][1] = step[2] # 1 : 그 전 스텝과 연속이 아님
graph[2][0] = step[1] + step[2]

for i in range(3, n+1):
    if graph[i][1] < max(graph[i-2]) + step[i]:
        graph[i][1] = max(graph[i][1], max(graph[i-2]) + step[i])
    if graph[i][0] < graph[i-1][1] + step[i]:
        graph[i][0] = max(graph[i][0], graph[i-1][1] + step[i])


print(max(graph[-1]))