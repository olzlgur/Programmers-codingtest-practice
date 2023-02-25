import copy, sys
sys.setrecursionlimit(10**5)
def solution(boards):
    global flag
    answer = []
    visited = []
    blen = len(boards[0])
    for i in range(blen) :
        visited.append([0]*blen)
    for board in boards:
        for i in range(len(board)):
            board[i] = list(board[i])
    for board in boards:
        count = 0
        for i in range(blen):
            for j in range(blen):
                if board[i][j] == "2" :
                    y, x = i, j
                elif board[i][j] == "1" :
                    count += 1
        flag = 0
        dfs(int(y), int(x), copy.deepcopy(visited), copy.deepcopy(board), 0, count)
        answer.append(flag)
    return answer

def dfs(y, x, visited, board, count, depth):
    global flag
    if depth == count :
        flag = 1

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited[y][x] = 1
    board[y][x] = "0"
    
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < len(board) and 0 <= ty < len(board) and board[ty][tx] == "1" and visited[ty][tx] == 0 :
            dfs(ty, tx, copy.deepcopy(visited), copy.deepcopy(board), count + 1, depth)

solution([["00011", "01111", "21001", "11001", "01111"]])