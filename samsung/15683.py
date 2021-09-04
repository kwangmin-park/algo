# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#4 상, 1우 , 2 하, 3 좌
cctv_list = [
    [[]],

    [[4],
     [1],
     [2],
     [3]],

    [[1, 3],
     [4, 2]],

    [[4, 1],
     [1, 2],
     [2, 3],
     [3, 4]],

    [[4, 1, 2],
     [1, 2, 3],
     [2, 3, 4],
     [3, 4, 1]],

    [[4, 1, 2, 3]]
]

visit = [[0 for _ in range(m)] for _ in range(n)]
final_graph_list = []
min_val = sys.maxsize


def cnt_zero_elem(graph):
    val = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                val += 1
    return val


def fill_graph(graph, dir, x, y):
    global n, m
    if dir == 4:
        for i in range(y-1, -1, -1):
            if graph[i][x] == 6:
                break
            graph[i][x] = '#'
    elif dir == 1:
        for j in range(x+1, m):
            if graph[y][j] == 6:
                break
            graph[y][j] = '#'
    elif dir == 2:
        for i in range(y+1, n):
            if graph[i][x] == 6:
                break
            graph[i][x] = '#'
    elif dir == 3:
        for j in range(x-1, -1, -1):
            if graph[y][j] == 6:
                break
            graph[y][j] = '#'
    return graph


def dfs(graph, visit):
    for i in range(n):
        for j in range(m):
            if i == 1 and j == 3:
                a = 3
            if graph[i][j] != '#' and 1 <= graph[i][j] <= 5 and not visit[i][j]:
                a = cctv_list[graph[i][j]]
                for dir_list in cctv_list[graph[i][j]]:
                    tmp_graph = copy.deepcopy(graph)
                    tmp_visit = copy.deepcopy(visit)
                    for each_dir in dir_list:
                        tmp_graph = fill_graph(tmp_graph, each_dir, j, i)
                    tmp_visit[i][j] = 1
                    # visit[i][j] = 1
                    dfs(tmp_graph, tmp_visit)
                    # dfs(tmp_graph, visit)
    dfs_check = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] != '#' and 1 <= graph[i][j] <= 5 and not visit[i][j]:
                dfs_check = False
                break
    if dfs_check:
        final_graph_list.append(graph)
        return True

dfs(graph, visit)
loop_graph = list(set(final_graph_list))
for each_graph in loop_graph:
    min_val = min(min_val, cnt_zero_elem(each_graph))

print(min_val)​