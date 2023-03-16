import heapq

def solution(N, coffee_times):
    answer = []
    machine = []
    time = [0] * (len(coffee_times))
    for index in range(len(coffee_times)):
        if len(machine) < N:
            heapq.heappush(machine, coffee_times[index])
            time[index] = (coffee_times[index], index + 1)
        else :
            t = heapq.heappop(machine)
            time[index] = (t + coffee_times[index], index + 1)
            heapq.heappush(machine, coffee_times[index] + t)
    time.sort(key=lambda x : x[0])
    for tu in time:
        answer.append(tu[1])
    return answer