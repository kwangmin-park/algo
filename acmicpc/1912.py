import sys
input = sys.stdin.readline
n = int(input())
answer = [-sys.maxsize for _ in range(n)]
graph = list(map(int, input().split()))
answer[0] = graph[0]

if n == 1:
    print(answer[0])
    exit(0)

for idx, val in enumerate(graph):
    if idx == 0: continue
    if val > answer[idx-1] + val:
        answer[idx] = val
    else:
        answer[idx] = answer[idx-1] + val

answer = max(answer)
print(answer)