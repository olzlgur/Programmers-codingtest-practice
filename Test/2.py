import sys
sys.setrecursionlimit(10**5)

def solution(p, b):
    answer = []

    for i in range(len(p)) :
        if p[i] != i and p[i]!= -1:
            p[i] = find(p, i)
    for i in range(len(b)) :
        if p[b[i]] == -1 :
            answer.append(p.count(b[i])+1)
        else :
            answer.append(0)

    return answer
    
def find(parent, x):
    if parent[x]!= -1 :
        parent[x] = find(parent, parent[x])
    return x


solution(([2,2,-1,1,5,-1,5]), [2, 5])