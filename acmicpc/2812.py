N, K = map(int, input().split())
origin_input = input()

list = [0]*N
list[0] = origin_input[0]
list_index = 0
for i in range(1, N):
    if origin_input[i] > list[list_index]:
        while list_index > -1 and list[list_index] < origin_input[i] and K > 0:
            list_index -= 1
            K -=1
        list_index += 1
        list[list_index] = origin_input[i]
    else:
        list_index +=1
        list[list_index] = origin_input[i]
    
    if K == 0:
        for j in range(i+1, N):
            list_index +=1
            list[list_index] = origin_input[j]
        break

print(''.join(list[:list_index-K+1]))