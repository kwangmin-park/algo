import sys


is_able_finish = False
dir = [[1, 0, 0, -1], [0, 1, -1, 0]]


def rotate_key(key_map, key_n):
    key_map_copy = [[0 for _ in range(key_n)] for _ in range(key_n)]
    for i in range(key_n):
        for j in range(key_n):
            if 0 <= key_n - 1 - i < key_n:
                key_map_copy[j][key_n - 1 - i] = key_map[i][j]
            key_map_copy[i][j] = 0
    return key_map_copy


def move_key(key_map, key_n, move_x, move_y):
    key_map_copy = [[0 for _ in range(key_n)] for _ in range(key_n)]
    for i in range(key_n):
        for j in range(key_n):
            if 0 <= i + move_y < key_n and 0 <= j + move_x < key_n:
                key_map_copy[i + move_y][j + move_x] = key_map[i][j]
    return key_map_copy


def is_blank(key_map, key_n):
    for i in range(key_n):
        for j in range(key_n):
            if key_map[i][j]:
                return False
    return True


def is_feet_key(key_map, lock_map, key_n):
    for i in range(key_n):
        for j in range(key_n):
            if lock_map[i][j] == key_map[i][j]:
                return False
    return True


def dfs(key, lock):
    global is_able_finish, dir
    if is_able_finish:
        return True
    if is_blank(key, len(key)):
        return False
    if is_feet_key(key, lock, len((key))):
        is_able_finish = True
        return True

    tmp_key_map = key[:]
    for i in range(3):
        tmp_key_map = rotate_key(tmp_key_map[:], len(tmp_key_map))
        dfs(tmp_key_map[:], lock)

    for i in range(4):
        move_x = dir[0][i]
        move_y = dir[0][i]
        dfs(move_key(key[:], len(key[:]), move_x, move_y), lock)


def solution(key, lock):
    global is_able_finish
    dfs(key[:], lock[:])

    answer = is_able_finish
    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],    [[1, 1, 1], [1, 1, 0], [1, 0, 1]])​