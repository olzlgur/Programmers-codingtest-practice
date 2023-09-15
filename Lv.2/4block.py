# 문제 설명

# 프렌즈4블록
# 블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
# board map
# 만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
# board map
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
# board map
# 만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
# board map
# 위 초기 배치를 문자로 표시하면 아래와 같다.
# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ
# 각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다
# 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.
# 입력 형식
# 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
# 2 ≦ n, m ≦ 30
# board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
# 출력 형식
# 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.
# 입출력 예제
# m	n	board	answer
# 4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
# 6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
# 예제에 대한 설명
# 입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
# 입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.

dx = [0, 1]
dy = [1, 0]
r, c = 0, 0
board2 = []

def dfs(y, x):
    global r, c, board2, cnt
    flag = 0
    if y == r-1 and x == c-1:
        return
    if y + 1 < r and x + 1 < c and board2[y][x] != '-' and board2[y][x] == board2[y][x+1] and board2[y][x+1] == board2[y+1][x] and board2[y+1][x] == board2[y+1][x+1]: 
        flag = 1
    
    if x < c-1:
        dfs(y, x+1)
    elif y < r-1:
        dfs(y+1, 0)
    
    
    if flag == 1:
        board2[y][x] = '-'
        board2[y][x+1] = '-'
        board2[y+1][x] = '-' 
        board2[y+1][x+1] = '-'
        cnt = -1
        
def down():
    global board2
    
    for y in range(r-2, -1, -1):
        for x in range(c):
            if board2[y][x] != '-':
                tmp = y + 1
                while True:
                    if tmp == r or board2[tmp][x] != '-':            
                        w = board2[y][x]
                        board2[y][x] = '-'
                        board2[tmp-1][x] = w
                         
                        break
                    
                    tmp += 1 
    
def solution(m, n, board):
    global r, c, borad2, cnt
    
    answer = 0
    r, c = m, n
    
    for idx in range(r):
        board2.append(list(board[idx]))
    
    cnt = -1
    
    while cnt!= 0:
        cnt = 0
        dfs(0, 0)
        down()
    
    for idx1 in range(r):
        for idx2 in range(c):
            if board2[idx1][idx2] == '-':
                answer += 1

    return answer
