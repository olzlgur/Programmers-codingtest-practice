import sys, heapq

input = sys.stdin.readline

n = int(input())
answer = 0
cur = 0
dp = []

number = list(map(int, input().split()))
cur = 0
dp.append([])
if number[0] == 0 :
    dp[0].append([0, 0, 1])
else :
    dp[0].append([number[0], 0, 0])
    dp[0].append([0, 1, 1])

for i in range(1, len(number)):
    dp.append([])
    for l in dp[i-1] :
        flag = 0
        if l[1] == 0 :
            if l[0] + number[i] == 0 :
                flag = 1
            dp[i].append([l[0]+number[i], 0, l[2]+flag])
            flag = 0
            if l[0] == 0 :
                flag = 1
            dp[i].append([l[0], 1, l[2]+ flag])
        else :
            if l[0] + number[i] == 0 :
                flag = 1
            dp[i].append([l[0] + number[i], 1, l[2]+flag])
dp[-1].sort(key=lambda x : -x[2])

print(dp[-1][0][2])