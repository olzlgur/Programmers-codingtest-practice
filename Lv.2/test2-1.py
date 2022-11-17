from itertools import permutations

def solution(dictionary, command):
    answer = []
    answertemp = []
    dictemp = []
    cnt = 1
    dictemp += dictionary
    stringtemp = ""
    for word in permutations(dictionary, 2):
        for c in word :
            stringtemp += c
        dictionary.append(stringtemp)
        stringtemp = ""
    for com in command :
        answer += answertemp
        if com[0] == "prefix" :
            for keyword in dictionary :
                if keyword[:len(com[1])] == com[1] :
                    answer.append(keyword) 
        elif com[0] == "postfix" :
            for keyword in dictionary :
                if keyword[len(keyword) - len(com[1]):] == com[1] :
                    answer.append(keyword)
        elif com[0] == "lengthMatch" :
            for keyword in dictionary :
                if len(keyword) == len(com[1]) and keyword[:com[1].find("@")] == com[1][:com[1].find("@")]:
                    answer.append(keyword)
        if cnt == 1 :
            for index in range(len(answer)) :
                if answer[index] in dictemp :
                    answertemp.append(word)
            cnt = 0
        dictionary = answer
    print(answer)
    return answer
solution(["123", "456", "789"], [["prefix", "123"]])