import sys, copy
from collections import deque


dir_list = [(1,0),(0,1),(-1,0),(0,-1)] # x, y L:왼쪽으로 90도, D: 오른쪽으로 90도
n = int(input())
k = int(input()) #사과 개수
apple_graph = []
drift_graph = {}
for i in range(k):
    a, b = map(int, input().split())
    apple_graph.append((b-1, a-1))
l = int(input())
for i in range(l):
    a, b = input().split()
    a = int(a)
    drift_graph[a] = b

cur_pos = (0, 0)
cur_len = 1
pos_list = [cur_pos]
cur_vector = 0
cur_time = 0

while True:
    cur_time += 1
    dx = dir_list[cur_vector][0]
    dy = dir_list[cur_vector][1]
    cur_pos = (cur_pos[0]+dx, cur_pos[1]+dy)
    # last_pos = pos_list.pop()
    if not(0 <= cur_pos[0] < n) or not(0 <= cur_pos[1] < n) or cur_pos in pos_list:
        print(cur_time)
        sys.exit()
    pos_list.insert(0, cur_pos)
    if cur_pos in apple_graph:
        apple_graph.remove(cur_pos)
    else:
        last_pos = pos_list.pop()
        # pos_list.append(last_pos)
    if cur_time in drift_graph.keys():
        tmp_vector = drift_graph[cur_time]
        if tmp_vector == 'L':
            cur_vector -= 1
            if cur_vector < 0:
                cur_vector = 3
        elif tmp_vector == 'D':
            cur_vector += 1
            if cur_vector >= 4:
                cur_vector = 0