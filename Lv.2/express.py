visit = []
time = {}
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

for index, route in enumerate(road) :
        if (route[0] == 1 or route[1] == 1) and route[2] <= K:
            visit.append(route[1])
            time[route[1]] = route[2]
        elif route[0] in visit and route[1] not in visit :
            if time[route[0]] + route[2] <= K :
                time[route[1]] = time[route[0]] + route[2]
                visit.append(route[1])
        elif route[0] not in visit and route[1] in visit :
            if time[route[1]] + route[2] <= K :
                time[route[0]] = time[route[1]] + route[2]
                visit.append(route[0])
        elif route[0] in visit and route[1] in visit :
            time[route[0]] = min(time[route[0]], time[route[1]] + route[2])
            time[route[1]] = min(time[route[1], time[route[0]]] + route[2])
            
print(visit)
print(1)