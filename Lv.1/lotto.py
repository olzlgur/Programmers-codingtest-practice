# 문제 설명
#로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다. 

#순위	당첨 내용
# 1 6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외

# 제한사항
# lottos는 길이 6인 정수 배열입니다.
# lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
# 0은 알아볼 수 없는 숫자를 의미합니다.
# 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
# lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
# win_nums은 길이 6인 정수 배열입니다.
# win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
# win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
# win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다. 

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    tmp = 0

    for num in lottos :
        if num == 0 :
            zero += 1
        elif num in win_nums :
            cnt += 1
    tmp = zero + cnt 

    if tmp < 2 :
        answer.append(6)
    else :
        answer.append(7-tmp)
    if cnt < 2 :
        answer.append(6)
    else :
        answer.append(7-cnt)

    return answer