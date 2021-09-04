import sys
import itertools
import copy

n, m, h = map(int, input().split())
graph = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

answer = [0 for _ in range(m)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b - 1][a - 2][a - 1] = 1
    graph[b - 1][a - 1][a - 2] = 1
    answer[a - 1] += 1

min_answer = sys.maxsize
# initial 가로선 개수 = m
# total 가로선 개수 = h

arr = [i for i in range(m)]
for temp_arr in itertools.permutations(arr, m):
    answer_temp = copy.deepcopy(answer)
    for k in range(m):
        # k = 시작점 기준(가로)
        cur_row_index = 0
        cur_col_index = k

        if 1 <= cur_col_index < m - 1 and not graph[cur_row_index][cur_col_index][cur_col_index + 1] and not \
        graph[cur_row_index][cur_col_index][cur_col_index - 1]:
            if cur_col_index < k:
                cur_col_index += 1
                answer_temp[cur_col_index] += 1
                if answer_temp[cur_col_index] > h:
                    print(-1)
                    sys.exit()
            elif cur_col_index > k:
                cur_col_index -= 1
                answer_temp[cur_col_index - 1] += 1
                if answer_temp[cur_col_index - 1] > h:
                    print(-1)
                    sys.exit()
        elif cur_col_index == m - 1:
            if cur_col_index > k:
                cur_col_index -= 1
                answer_temp[cur_col_index - 1] += 1
                if answer_temp[cur_col_index - 1] > h:
                    print(-1)
                    sys.exit()
        elif cur_col_index == 0:
            if cur_col_index < k:
                cur_col_index += 1
                answer_temp[cur_col_index] += 1
                if answer_temp[cur_col_index] > h:
                    print(-1)
                    sys.exit()
        else:
            if cur_col_index + 1 < m and graph[cur_row_index][cur_col_index][cur_col_index + 1]:
                cur_col_index += 1
            elif cur_col_index - 1 >= 0 and graph[cur_row_index][cur_col_index][cur_col_index - 1]:
                cur_col_index -= 1

    tmp_min_answer = 0
    for each_answer in answer_temp:
        tmp_min_answer += each_answer
    min_answer = min(min_answer, tmp_min_answer - m)
print(min_answer)​