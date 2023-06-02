from collections import defaultdict
from queue import Queue
from math import comb


# 에르되시 수 계산 함수
def calculate_erdos(n, m, names, authors):
    factorial = [1, 1]
    for i in range(2, n+1):
        factorial.append(factorial[-1] * i)
    # 에르되시 수 초기화
    erdos_numbers = defaultdict(lambda: float("inf"))
    erdos_numbers["erdos"] = 0
    
    # 그래프 초기화
    graph = defaultdict(list)
    for paper in authors:
        for author1 in paper:
            for author2 in paper:
                if author1 != author2:
                    graph[author1].append(author2)
    
    # BFS를 이용한 에르되시 수 계산
    q = Queue()
    q.put("erdos")
    while not q.empty():
        current_author = q.get()
        current_number = erdos_numbers[current_author]
        for neighbor in graph[current_author]:
            if erdos_numbers[neighbor] == float("inf"):
                erdos_numbers[neighbor] = current_number + 1
                q.put(neighbor)
                
    # 시루의 에르되시 수와 6 이하인 공동 작업 동료의 수 계산
    siroo_erdos_number = erdos_numbers["siroo"]
    count = sum(1 for number in erdos_numbers.values() if number < 6)
    print(count, factorial)
    # 조합 계산
    cnt = 0
    for k in range(0, count):
        cnt += factorial[k]

    cnt2 = 0
    for k in range(0, n-count):
        cnt2 += factorial[k]

    print()        
    return cnt * (cnt2+1)




print(calculate_erdos(8, 8, ["justi","cehui","jhnah","erdos","aaaaa","bbbbb","ccccc","ddddd"],	[["erdos","justi"],["justi","cehui"],["cehui","jhnah"],["jhnah","aaaaa"],["aaaaa","bbbbb"],["bbbbb","ccccc"],["ccccc","ddddd"],["ccccc","ddddd"]]))