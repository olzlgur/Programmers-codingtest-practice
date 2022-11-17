# 문제
# BOJ 거리는 보도블록 N개가 일렬로 놓여진 형태의 도로이다. 도로의 보도블록은 1번부터 N번까지 번호가 매겨져 있다.

# 스타트의 집은 1번에 있고, 링크의 집은 N번에 있다. 스타트는 링크를 만나기 위해서 점프해가려고 한다.

# BOJ거리의 각 보도블록에는 B, O, J 중에 하나가 쓰여 있다. 1번은 반드시 B이다.

# 스타트는 점프를 통해서 다른 보도블록으로 이동할 수 있다. 이때, 항상 번호가 증가하는 방향으로 점프를 해야 한다. 만약, 스타트가 현재 있는 곳이 i번이라면, i+1번부터 N번까지로 점프를 할 수 있다. 한 번 k칸 만큼 점프를 하는데 필요한 에너지의 양은 k*k이다.

#    BOJ를 외치면서 링크를 만나러 가려고 한다. 따라서, 스타트는 B, O, J, B, O, J, B, O, J, ... 순서로 보도블록을 밟으면서 점프를 할 것이다.

# 스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 1 ≤ N ≤ 1,000이 주어진다.

# 둘째 줄에는 보도블록에 쓰여 있는 글자가 1번부터 순서대로 주어진다.

# 출력
# 스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 출력한다. 만약, 스타트가 링크를 만날 수 없는 경우에는 -1을 출력한다.

# 예제 입력 1  복사
# 9
# BOJBOJBOJ
# 예제 출력 1  복사
# 8
# 예제 입력 2  복사
# 9
# BOJBOJBOJ
# 예제 출력 2  복사
# 8
# 예제 입력 3  복사
# 8
# BJJOOOBB
# 예제 출력 3  복사
# -1
# 예제 입력 4  복사
# 13
# BJBBJOOOJJJJB
# 예제 출력 4  복사
# 50
# 예제 입력 5  복사
# 2
# BO
# 예제 출력 5  복사
# 1
# 예제 입력 6  복사
# 15
# BJBOJOJOOJOBOOO
# 예제 출력 6  복사
# 52

N = int(input())
street = input()
dp = [0] * N
dic = {"B" : "O", "O" : "J", "J" : "B"}
visited = [0] * N
visited[0] = 1

for i in range(N) :
    if visited[i] == 1:
        for j in range(i+1, N):
            if street[j] == dic[street[i]] :
                if dp[j] == 0 or dp[j] > dp[i] + (j-i) * (j-i):
                    dp[j] = dp[i] + (j-i) * (j-i)
                    visited[j] = 1

print(dp)