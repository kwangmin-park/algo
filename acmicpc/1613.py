import sys
input = sys.stdin.readline
 
def floydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if adjMatrix[i][k] and adjMatrix[k][j]:
                    adjMatrix[i][j] = 1
 
 
N, K = map(int,input().split())
adjMatrix = [[0] * N for _ in range(N)]
 
for _ in range(K):
    a, b = map(int,input().split())
 
    adjMatrix[a-1][b-1] = 1
 
floydWarshall()
 
s = int(input())
 
for _ in range(s):
    a, b = map(int,input().split())
    
    if adjMatrix[a-1][b-1] == 1:
        print(-1)
    elif adjMatrix[b-1][a-1] == 1:
        print(1)
    else:
        print(0)