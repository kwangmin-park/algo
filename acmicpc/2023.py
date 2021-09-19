import sys, math
from collections import deque
input = sys.stdin.readline
n = int(input())

start_list = [2, 3, 5, 7] #첫째자리는 한 자리일 때 소수인 2, 3, 5, 7만 올 수 있다.
#그 다음부턴 1, 3, 5, 7, 9의 홀수가 올 수 있음.
next_list = [1,3,5,7]
def is_prime(num):
    for k in range(2, int(math.sqrt(num))+1):
        if num % k == 0:
            return False
    return True

def sol(val, level):
    global n

    if is_prime(val):
        if level == n:
            print(val)
        elif level < n:
            for j in range(1, 10, 2):
                sol(val*10+j, level+1)

for i in start_list:
    sol(i, 1)
