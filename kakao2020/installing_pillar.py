def solution(n, build_frame):
   answer = [[]]
   graph = [[-1 for _ in range(n)] for _ in range(n)]
   
   for each_build in build_frame:
       x = each_build[0]
       y = each_build[1]
       kind = each_build[2]
       is_build = each_build[3]
       
       if kind:#보인경우
           if is_build and ((y > 0 and graph[y-1][x] == 0) or ((x > 0 and x+1 < n and graph[y][x-1] == 1 and graph[y][x+1] == 1))):
               graph[y][x] = 1
           if not is_build and graph[y][x] == 1:
               graph[y][x] = -1
       else:#기둥인경우
           if is_build and (y == 0 or (y > 0 and graph[y-1][x] == 0) or (x > 0 and y > 0 and graph[y-1][x] == -1 and graph[y-1][x-1] == 1)):
               graph[y][x] = 0
           if not is_build and graph[y][x] == 0:
               graph[y][x] = -1
   return answer​