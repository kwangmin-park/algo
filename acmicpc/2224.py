import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
a = ord('z') - ord('A')
graph = [[INF for _ in range(a+1)] for _ in range(a+1)]
for i in range(n):
   q,w,e = input().split()
   graph[ord(q)-ord('A')][ord(e)-ord('A')] = 1
for k in range(a+1):
   for o in range(a+1):
      for p in range(a+1):
        graph[o][p] = min(graph[o][p],graph[o][k]+graph[k][p])
cnt = 0
for i in range(a+1):
   for j in range(a+1):
      if i != j and graph[i][j] != INF:
         cnt += 1
print(cnt)
for i in range(a+1):
   for j in range(a+1):
      if i != j and graph[i][j] != INF:
         print(chr(i+ord('A')), '=>', chr(j+ord('A')))