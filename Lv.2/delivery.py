import copy

cost = []

def solution(N, road, K):
    global cost
    answer = 0
    town = []
    
    visited = [0] * (N+1)
    cost = [0] * (N+1)
    for i in range(N+1):
        town.append([])
        
    for r in road :
        town[r[0]].append((r[1], r[2]))
        town[r[1]].append((r[0], r[2]))
    dfs(1, town, visited)
    for i in range(1, len(cost)):
        if cost[i] <= K:
            answer += 1
    return answer
    
def dfs(n, town, visited):
    global cost
    visited[n] = 1
    for t in town[n] :
        if visited[t[0]] == 0 and (cost[t[0]] == 0 or cost[n] + t[1] < cost[t[0]]) :
            cost[t[0]] = cost[n] + t[1]
            dfs(t[0], town, copy.deepcopy(visited))
            
            
            