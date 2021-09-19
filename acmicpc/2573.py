import sys, copy
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
graph = [[] for _ in range(h)]
visit = [[False for _ in range(w)] for _ in range(h)]
for i in range(h):
    graph[i] = list(map(int, input().split()))


def bfs(x, y):
    global graph, h, w, visit
    dq = deque()
    dq.append((x,y))
    copy_graph = copy.deepcopy(graph)
    dir = [[1, 0, 0, -1], [0, 1, -1, 0]]

    visit[y][x] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            dx = x + dir[0][i]
            dy = y + dir[1][i]

            if 0 <= dx < w and 0 <= dy < h:
                if copy_graph[y][x] > 0 and graph[dy][dx] <= 0:
                    copy_graph[y][x] -= 1
                if not visit[dy][dx] and graph[dy][dx] > 0:
                    visit[dy][dx] = True
                    dq.append((dx, dy))
    graph = copy.deepcopy(copy_graph)
# 1. 섬 하나인지 check
# 2. bfs
print_year = 0
while True:
    is_exist_snow = False
    for i in range(h):
        for j in range(w):
            if graph[i][j] > 0:
                is_exist_snow = True
                break
        if is_exist_snow:
            visit = [[False for _ in range(w)] for _ in range(h)]
            bfs(j, i)
            for k in range(h):
                for l in range(w):
                    if not visit[k][l] and graph[k][l] > 0:
                        print(print_year)
                        sys.exit()
            print_year += 1
            break
    if not is_exist_snow:
        print(0)
        break
    # 이부분에 섬 체크 필요
    #visit을 bfs 함수 안이 아닌 while안에 선언해서 이미 한번 bfs를 실행했어도 break하지 않고,
    #한 while안에서 bfs한 뒤에 visit안한 graph[i][j] > 0 이 있으면 섬이 두개인 것이다.
    #if 섬 두개면 print(print_year), exit()
