import heapq

def solution(K, user_scores):
    answer = 0
    rankBoard = []
    nameBoard = []
    for record in user_scores:
        name, score = record.split()
        score = int(score)
        if len(rankBoard) < K:
            if name not in nameBoard:
                rankBoard.append([score, name])
                nameBoard.append(name)
                answer += 1
            else :
                rankBoard.sort(key=lambda x: -x[0])
                for index in range(len(rankBoard)):
                    if rankBoard[index][1] == name and rankBoard[index][0] < score: 
                        rankBoard[index][0] = score
                        rankBoard.sort(key=lambda x: -x[0])
                        if rankBoard[index][1] != name:
                            answer += 1
        elif name not in nameBoard:
            rankBoard.sort(key=lambda x: -x[0])
            if rankBoard[-1][0] < score:
                tName = rankBoard[-1][1]
                rankBoard[-1] = [score, name]
                for i in range(len(nameBoard)):
                    if nameBoard[i] == tName:
                        nameBoard[i] = name
                answer += 1
        else:
            rankBoard.sort(key=lambda x: -x[0])
            for index in range(len(rankBoard)):
                if rankBoard[index][1] == name and rankBoard[index][0] < score:
                    rankBoard[index][0] = score
                    rankBoard.sort(key=lambda x: -x[0])
                    if rankBoard[index][1] != name:
                        answer += 1
    return answer