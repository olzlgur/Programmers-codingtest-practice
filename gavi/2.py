from itertools import permutations
def solution(dots, lines):
    useLine = []
    maxDot = max(dots)
    for i in range(len(lines)-1, -1, -1):
        useLine.append(lines[i])
        for tu in permutations(useLine, len(useLine)):
            cur = dots[0]
            for t in tu:
                cur = cur + t
                if maxDot <= cur:
                    return len(useLine)
                else :
                    for d in dots:
                        if cur < d:
                            cur = d
                            break
    return -1