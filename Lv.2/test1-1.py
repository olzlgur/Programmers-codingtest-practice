def solution(members, commands, messageIDs):
    answer = []
    read = []
    temp = []
    my = "MY"
    for j in commands:
        temp.append(j[2])
        if j[1] == my:  
            read += temp
            temp = []
    for m in messageIDs:
        if m in read :
            answer.append("true")
        else:
            answer.append("false")
    print(answer)
    return answer

solution(["A", "B"], [["W", "MY", "1"], ["W", "A", "7"], ["W", "B", "4"], ["W", "MY", "9"], ["W", "A", "11"], ["R", "B", ""]], ["7", "11"])