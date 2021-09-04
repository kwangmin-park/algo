# your code goes here
n, m, t = map(int, input().split())
​
one_graph = []
for _ in range(n):
	one_graph.append(list(map(int, input().split())))
one_graph = [] + one_graph
rotate_list = []
for _ in range(t):
	x, d, k = map(int, input().split())
	rotate_list.append((x, d, k)) #xi, di, ki
	#di = 0: 시계방향, 1: 반시계방향
​
for x, d, k in rotate_list:
	
	k = k % 4
	if d == 1:
		k = (4-k) % 4
	#k는 이제 시계방향으로 k번만 회전시키면됨
	for x_index in range(x, n+1, x):
		for k_index in range(k):
			one_graph[x_index] = one_graph[x_index][m-1] + one_graph[x_index][:m-1]
	
	#회전 끝. 인전한 것 중 같은 수 삭제.
	for x_index in range(1, n+1):
		#j인접
		check_nearby = False
		sum_val = 0
		for k_index in range(m):
			sum_val = one_graph[x_index][k_index]
			sum += val
			if k_index == 0:
				if val == one_graph[x_index][k_index+1]:
					one_graph[x_index][k_index+1] = 0
					one_graph[x_index][k_index] = 0
					check_nearby = True
				if val == one_graph[x_index][m-1]:
					one_graph[x_index][m-1] = 0
					one_graph[x_index][k_index] = 0
					check_nearby = True
​
			elif k_index == m-1:
				if val == one_graph[x_index][0]:
					one_graph[x_index][0] = 0
					one_graph[x_index][k_index] = 0
					check_nearby = True
				if val == one_graph[x_index][k_index-1]:
					one_graph[x_index][k_index-1] = 0
					one_graph[x_index][k_index] = 0
					check_nearby = True
​
			else:
				if val == one_graph[x_index][k_index+1]:
					one_graph[x_index][k_index+1] = 0
					one_graph[x_index][k_index] = 0
					check_nearby = True
				if val == one_graph[x_index][k_index-1]:
					one_graph[x_index][k_index-1] = 0
					one_graph[x_index][k_index] = 0
					check_nearby = True
​
​
			#i인접
			if x_index != 1:
				for k_index in range(m):
					if val == one_graph[x_index+1][k_index]:
						one_graph[x_index+1][k_index] = 0
						one_graph[x_index][k_index] = 0
						check_nearby = True
			if x_index != n:
				for k_index in range(m):
					if val == one_graph[x_index-1][k_index]:
						one_graph[x_index-1][k_index] = 0
						one_graph[x_index][k_index] = 0
						check_nearby = True
​
			#인접한것중 같은 값이 없는 경우
			if check_nearby:
				average_val = sum / m
				for k_index in range(m):
					if one_graph[x_index][k_index] > average_val:
						one_graph[x_index][k_index] -= 1
					elif one_graph[x_index][k_index] != 0 and one_graph[x_index][k_index] < average_val:
						one_graph[x_index][k_index] += 1
​
​
answer = 0
for x_index in range(1, n+1):
	for k_index in range(m):
		answer += one_graph[x_index][k_index]
​
print(answer)