n, m = map(int, input().split())
M = []
for _ in range(n):
  M.append(list(map(int, input())))        
def main():
    dfs(0, 0, n, m)
    print(M[n-1][m-1])
def dfs(x, y, n, m):
    if x == n and y == m:
        return   
    if x + 1 < n and (M[x+1][y] == 1 or M[x+1][y] > M[x][y]):
        M[x+1][y] = M[x][y] + 1
        dfs(x+1, y, n, m)
    if x - 1 >= 0 and (M[x-1][y] == 1 or M[x-1][y] > M[x][y]):
        M[x-1][y] = M[x][y] + 1
        dfs(x-1, y, n, m)
    if y + 1 < m and (M[x][y+1] == 1 or M[x][y+1] > M[x][y]):
        M[x][y+1] = M[x][y] + 1
        dfs(x, y+1, n, m)
    if y - 1 >= 0 and (M[x][y-1] == 1 or M[x][y-1] > M[x][y]):
        M[x][y-1] = M[x][y] + 1
        dfs(x, y-1, n, m)
main()