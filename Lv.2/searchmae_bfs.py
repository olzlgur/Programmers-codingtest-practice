from collections import deque

n, m = map(int, input().split())
M = []
for _ in range(n):
  M.append(list(map(int, input())))        
def main():
    bfs(0, 0)
    print(M[n-1][m-1])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if M[nx][ny] == 0:
                continue

            if M[nx][ny] == 1:
                M[nx][ny] = M[x][y] + 1

                queue.append((nx, ny))
            
    return M[n-1][m-1]
main()