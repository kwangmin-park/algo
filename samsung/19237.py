import copy
​
​
n, m, k = map(int, input().split())
​
graph = []
shark_list = [[] for _ in range(m)]
for _ in range(n):
	graph.append(list(map(int, input().split()))) #0:빈칸 0이 아닌 수 x는 x번 상어
​
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#1,2,3,4 위 아래 왼쪽 오른쪽
cur_shark_dir = list(map(int, input().split()))
​
​
#상어당 4줄씩 차례로 주어진다
prefer_shark_dir = []
for i in range(n):
	each_prefer_shark_dir = []
	for j in range(4):
		each_prefer_shark_dir.append(list(map(int, input().split())))
	prefer_shark_dir.append(each_prefer_shark_dir)
​
​
perfume_graph = [[[] for _ in range(n)] for _ in range(n)]
​
for loop_count in range(1001):
​
	#종료 조건 여기에 두고, print(loop_count)
	finish_check = True
	for i in range(n):
		for j in range(n):
			if graph[i][j] > 1:
				finish_check = False
				break
		if not finish_check:
			break
	if finish_check:
		print(loop_count)
		sys.exit()
​
​
	#이부분을 입력받을때 shark_list에 shark넣어서 for 문 없앨수 있음
	move_shark_list = []
	#향기 남기기
	for i in range(n):
		for j in range(n):
			if graph[i][j] > 0:
				perfume_graph[i][j] = [graph[i][j], k]
​
​
	#상어 이동하기. 이동한 상어의 번호는 move_shark_list에 넣고, 여기에 들어있는 상어는 다시 이동하면 안 됨.
	for i in range(n):
		for j in range(n):
			if graph[i][j] > 0:
				shark_dir = cur_shark_dir[graph[i][j] - 1]				
				each_prefer_shark_dirs = prefer_shark_dir[graph[i][j] - 1][shark_dir]
​
				
				#향기 없는곳 찾기
				check_find_no_perfume = False
				for each_prefer_shark_dir in each_prefer_shark_dirs:
					nx = j + dirs[each_prefer_shark_dir - 1][0]
					ny = i + dirs[each_prefer_shark_dir - 1][1]
​
					#이 if문에 걸리면 향기 없는 칸 찾은 것임.
					if 0 <= nx < n and 0 <= ny < n and len(perfume_graph[ny][nx]) == 0:
						if not(0 < graph[ny][nx] and graph[i][j]):
							#상어 방향 변환
							cur_shark_dir[graph[i][j] - 1] = each_prefer_shark_dir
							#상어 이동
							graph[ny][nx] = graph[i][j]
						graph[i][j] = 0
						check_find_no_perfume = True
						break
				#향기 없는곳 못찾았을 경우 자신의 향기있는곳으로 이동
				if not check_find_no_perfume:
					for each_prefer_shark_dir in each_prefer_shark_dirs:
						nx = j + dirs[each_prefer_shark_dir - 1][0]
						ny = i + dirs[each_prefer_shark_dir - 1][1]
​
						#이 if문에 걸리면 향기 없는 칸 찾은 것임.
						if 0 <= nx < n and 0 <= ny < n and len(perfume_graph[ny][nx]) == 0 and perfume_graph[ny][nx][0] == graph[i][j]:
							if not(0 < graph[ny][nx] and graph[i][j]):
								#상어 방향 변환
								cur_shark_dir[graph[i][j] - 1] = each_prefer_shark_dir
								#상어 이동
								graph[ny][nx] = graph[i][j]
							graph[i][j] = 0
							break
​
​
	#겹친 상어 지우기. 근데 사실 상어 지우기는 상어 이동하면서 하는거임 ㅋㅋㄹ
​
​
	#향기 지우기
	for i in range(n):
		for j in range(n):
			if len(perfume_graph[i][j]) > 0:				
				if perfume_graph[i][j][1] - 1 == 0:
					perfume_graph[i][j] = []
				else:
					perfume_graph[i][j] = [perfume_graph[i][j][0], perfume_graph[i][j][1] - 1]
print(-1)
​
#1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지 구하는 프로그램