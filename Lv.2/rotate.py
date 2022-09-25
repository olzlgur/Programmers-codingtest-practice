# 괄호 회전하기
# dark
# light
# sublime
# vim
# emacs
#  Python3 
# 문제 설명

# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# s의 길이는 1 이상 1,000 이하입니다.

def solution(s):
    answer = 0    
    
    for i in range(0, len(s)):
        answer += checkstack(s)
        s = s[1:] + s[0]
    
    return answer

def checkstack(s):
    stack = []

    for c in s:
        if c == '(' or c == '[' or c == '{' :
            stack.append(c)
        elif len(stack) > 0 :
            temp = stack.pop()
            if temp == '(' and c != ')':
                return 0
            elif temp == '[' and c!= ']':
                return 0
            elif temp == '{' and c!= '}':
                return 0
        else :
            return 0
    if len(stack) > 0 :
        return 0
    print(stack)
    return 1