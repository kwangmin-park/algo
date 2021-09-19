from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1

while True:
   n = int(input())
   if n == 0:
     break
   s = []
   for i in range(n):
     s.append(list(map(int, input().split())))

   dp = [[100000000] * n for i in range(n)]
   dp[0][0] = s[0][0]

   dq = deque()
   dq.append((s[0][0], 0, 0))
   while dq:
     c, a, b = dq.popleft()

     for i in range(4):
         x = a + dx[i]
         y = b + dy[i]
         if 0 <= x < n and 0 <= y < n and dp[x][y] > dp[a][b] + s[x][y]:
             dp[x][y] = dp[a][b] + s[x][y]
             dq.append((dp[x][y], x, y))

   print("Problem %d: %d" % (cnt, dp[n - 1][n - 1]))
   cnt += 1