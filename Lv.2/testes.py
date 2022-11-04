from collections import deque

def solution(M, S, D):
    answer = 0
    y = len(M) - S[1] -1
    for i in range(len(M[0])) :
        for j in range(len(M)) :
            if M[j][i] == 0 :
                M[j][i] = 1
            else :
                M[j][i] = 0
    return bfs(len(M) - S[1] -1, S[0], len(M[0]), len(M), M, D)
def bfs(x, y, n, m, Map, D):    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if Map[ny][nx] == 0 :
                continue
            if Map[ny][nx] == 1 :
                Map[ny][nx] = Map[y][x] + 1
                queue.append((nx, ny))
            if nx == D[1] and ny == D[0] :
                break
    return Map[len(Map) - D[1]][D[0]]

solution([[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]], [0, 0], [6, 3])