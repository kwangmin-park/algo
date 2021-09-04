import copy
​
# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2
​
dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
graph = [[0 for _ in range(4)] for _ in range(4)]
fish_list = [0 for _ in range(16)]
​
​
shark_x = 0
shark_y = 0
shark_dir = 0
answer = 0
​
for i in range(4):
	a = list(map(int, input().split()))
	for j in range(4):
		graph[i][j] = (a[j*2]-1, a[j*2+1]-1) #물고기 번호, 방향
		fish_list[a[j*2]-1] = (j, i, a[j*2+1]-1)
​
​
initial_shark = graph[0][0]
fish_list[initial_shark[0]] = 0
answer += initial_shark[0]+1
shark_dir = initial_shark[1]
​
dq = deque()
dq.append((shark_x, shark_y, shark_dir, initial_shark[0]+1, fish_list))
​
while dq:
	x, y, dir, cnt, fish_list = dq.popleft()
	#물고기 이동
	for fish_index in range(16):
		if fish_list[fish_index] == 0:
			continue
​
		fish_x, fish_y, fish_dir = fish_list[fish_index]
		check_exist_shuffeld_fish = False
		for tmp_dir in range(8)
			nx = fish_x + dirs[fish_dir][0]
			ny = fish_y + dirs[fish_dir][1]
​
			if 0 <= nx < 4 and 0 <= ny < 4 and (x != nx or y !=  ny):				
				for i in range(16):
					if fish_list[i] == 0:
						continue
​
					if fish_list[i][0] == nx and fish_list[i][1] == ny:
						check_exist_shuffeld_fish = True
						tmp_fish = fish_list[i]
						fish_list[i] = fish_list[fish_index]
						fish_list[fish_index] = tmp_fish
						break
			if check_exist_shuffeld_fish:
				break
			fish_dir = (fish_dir + 1) % 8
​
	#상어 이동
	check_fish_exist = False
	for i in range(3):
		nx = x + dirs[dir][0] * (i+1)
		ny = y + dirs[dir][1] * (i+1)
​
		if not(0 <= nx < 4 and 0 <= ny < 4):
			continue
		
		for j in range(16):
			if fish_list[j] == 0:
						continue
			if fish_list[j][0] == nx and fish_list[j][1] == ny:.
				check_fish_exist = True
				tmp_fish_list = copy.deepcopy(fish_list)
				tmp_fish_list[j] = 0
				dq.append((nx, ny, fish_list[j][2], cnt+j+1, tmp_fish_list))
				break
	if not check_fish_exist and cnt > answer:
		answer = cnt
​
print(answer)​