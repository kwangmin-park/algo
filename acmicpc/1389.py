import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #유저수, 친구관계수

INF = sys.maxsize
input_list = [[INF for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    input_list[a-1][b-1] = 1
    input_list[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if input_list[i][j] > input_list[i][k] + input_list[k][j]:
                input_list[i][j] = input_list[i][k] + input_list[k][j]

cnt_list = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            cnt += input_list[i][j]
    cnt_list.append(cnt)

print(cnt_list.index(min(cnt_list))+1)