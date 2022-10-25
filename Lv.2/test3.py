def solution(S, C):
    sl = list(S)

    if len(list(set(sl))) == len(sl):
        return 0

    for index, value in enumerate(C):
        temp = 0
        cnt = sl[:value].count('$')
        sl.insert(cnt + value, '$')
        for c in ''.join(sl).split('$') :
            if len(list(set(c))) != len(c):
                temp += 1
        print(sl)
        if temp == 0 :
            print(index+1)
            return index + 1
        if index +1 == len(C) :
            return -1
    

solution("aaaaa", [1, 2, 3, 4])