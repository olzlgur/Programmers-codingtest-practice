# 파일명 정렬
# 세 차례의 코딩 테스트와 두 차례의 면접이라는 기나긴 블라인드 공채를 무사히 통과해 카카오에 입사한 무지는 파일 저장소 서버 관리를 맡게 되었다.

# 저장소 서버에는 프로그램의 과거 버전을 모두 담고 있어, 이름 순으로 정렬된 파일 목록은 보기가 불편했다. 파일을 이름 순으로 정렬하면 나중에 만들어진 ver-10.zip이 ver-9.zip보다 먼저 표시되기 때문이다.

# 버전 번호 외에도 숫자가 포함된 파일 목록은 여러 면에서 관리하기 불편했다. 예컨대 파일 목록이 ["img12.png", "img10.png", "img2.png", "img1.png"]일 경우, 일반적인 정렬은 ["img1.png", "img10.png", "img12.png", "img2.png"] 순이 되지만, 숫자 순으로 정렬된 ["img1.png", "img2.png", "img10.png", img12.png"] 순이 훨씬 자연스럽다.

# 무지는 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.

# 소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.

# 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.

# HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
# NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
# TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

import re

def solution(files):
    answer = []
    result = []
    print(type(tmp))
    for index in range(len(files)):            
        head = re.findall(r'[a-zA-Z]+[-. ]*', files[index])[0]
        number = re.findall(r'[0-9]{1,5}',files[index])[0]
        tail = re.sub('^[a-zA-Z]+[-. ]*[0-9]+', '', files[index])
        if tail == None :
            answer.append([head, number, index])
        else :
            answer.append([head, number, tail, index])
        
    answer.sort(key = lambda x : (x[0].lower(), int(x[1]), int(x[-1])))
    
    for index in range(len(answer)):
        result.append(''.join(answer[index][:-1]))
    
    return result