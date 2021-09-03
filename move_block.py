from collections import deque
import sys
​
dir = [[1, 0, 0, -1], [0, 1, -1, 0]]
visit = []  # visit에 가로세로, 위치 이렇게 3차원으로 잡아야할듯 기본값 0, 가로 2, 세로 3 -> 5면 다시 방문하면안됨
​
​
​
def able_move(board, cur_pos, col, dx, dy):
   n = len(board)
   if col:
       if not (0 <= cur_pos[1] + dy < n) or not (0 <= cur_pos[0] + dx < n) or not (0 <= cur_pos[1] + dy - 1 < n) or \
               board[cur_pos[1] + dy][cur_pos[0] + dx] or board[cur_pos[1] + dy - 1][cur_pos[0] + dx]:
           return False
       else:
           return True
   else:
       if not (0<= cur_pos[1] + dy < n) or not(0<=cur_pos[0] + dx<n) or not(0<=cur_pos[0] + dx - 1<n) or board[cur_pos[1] + dy][cur_pos[0] + dx] or board[cur_pos[1] + dy][cur_pos[0] + dx - 1]:
           return False
       else:
           return True
​
# def is_col(dron):#return true일 경우 세로, false인 경우 가로
#     return dron[0][0] == dron[1][0]
​
# def rotate90(board, dron):
#     return list(zip(*dron[::-1]))
​
# def rotate270(board, dron):
#     for _ in range(3):
#         dron = list(zip(*dron[::-1]))
#     return dron
​
​
def rotate(cur_pos, col):
   if col:  # 세로면
       return (cur_pos[0] + 1, cur_pos[1])
   else:
       return (cur_pos[0], cur_pos[1] + 1)
​
​
def dfs(board, drone):
   finish_pos = (len(board) - 1, len(board) - 1)
   n = len(board)
   min_cnt = sys.maxsize
   dq = deque()
   dq.append((0, drone))
   visit = set()
   visit.add(drone)
   while dq:
       move_cnt, drone = dq.popleft()
       if drone in visit:
           continue
​
       fir_drone = drone[0]
       sec_drone = drone[0]
​
       #check finish -> print, return
       if fir_drone == finish_pos or sec_drone == finish_pos:
           if move_cnt < min_cnt:
               min_cnt = move_cnt
           continue
​
       #사방향 이동
       for i in range(4):
           dx = dir[0][i]
           dy = dir[1][i]
​
           if able_move(board, fir_drone, dx, dy) and able_move(board, sec_drone, dx, dy):
               add_drone = ((fir_drone[0]+dx, fir_drone[1]+dy), (sec_drone[0]+dx, sec_drone[1]+dy))
               dq.append((move_cnt + 1, add_drone))
               visit.add(add_drone)
       #회전
       #가로인경우
       if fir_drone[1] == sec_drone[1]:
           for d in [-1, 1]:
               if 0<= fir_drone[1]+d < n and 0<= sec_drone[1]+d < n and not fir_drone[1]+d and not sec_drone[1]+d:
                   add_drone = ((fir_drone[0], fir_drone[1]+d), (sec_drone[0], sec_drone[1]+d))
                   dq.append((move_cnt+1, ))
                   visit.add(add_drone)
       else:
           for d in [-1, 1]:
               if 0<= fir_drone[0]+d < n and 0<= sec_drone[0]+d < n and not fir_drone[0]+d and not sec_drone[0]+d:
                   add_drone = ((fir_drone[0]+d, fir_drone[1]), (sec_drone[0]+d, sec_drone[1]))
                   dq.append((move_cnt+1, add_drone))
                   visit.add(add_drone)
       # if able_rotate(board, cur_pos, col):
       #     dq.append((move_cnt + 1, rotate(cur_pos, col), not col))
​
   return min_cnt
​
​
def solution(board):
   
   drone = ((0, 0), (1, 0))  # x, y    
   answer = dfs(board, drone)
   print(answer)
   return answer
   
solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])​