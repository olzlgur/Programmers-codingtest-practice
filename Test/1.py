def solution(bakery_schedule, current_time, k):
    bread = 0
    curHour, curMin = map(int, current_time.split(":"))
    
    for index in range(len(bakery_schedule)) :
        time, n = bakery_schedule[index].split()
        bakeHour, bakeMin = map(int, time.split(":"))
        if curHour < bakeHour or (curHour == bakeHour and curMin <= bakeMin) :
            break
    for i in range(index, len(bakery_schedule)) :
        time, n = bakery_schedule[i].split()
        bread += int(n)
        endTime = time
        if k <= bread :
            break
    
    if bread < k :
        return -1
    
    endHour, endMin = map(int, endTime.split(":"))


    return (endHour*60 + endMin) -(curHour * 60 + curMin)