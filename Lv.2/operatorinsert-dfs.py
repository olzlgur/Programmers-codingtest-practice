n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

maxnum = -1e9
minnum = 1e9

def dfs(depth, total, plus, minus, mul, div):
  global maxnum, minnum

  if depth == n :
    maxnum = max(total, maxnum)
    minnum = min(total, minnum)
    return
    
  if plus:
    dfs(depth + 1, total + num[depth], plus - 1, minus, mul, div)
  if minus:
    dfs(depth + 1, total - num[depth], plus, minus - 1, mul, div)
  if mul:
    dfs(depth + 1, total * num[depth], plus, minus, mul - 1, div)
  if div:
    dfs(depth + 1, int(total / num[depth]), plus, minus, mul, div - 1)


dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])
print(maxnum)
print(minnum)