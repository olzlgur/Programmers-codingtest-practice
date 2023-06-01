# 택배 배달과 수거하기
# dark
# light
# sublime
# vim
# emacs
#  Python3 
# 문제 설명

# 재할용 택배 상자.png
# 당신은 일렬로 나열된 n개의 집에 택배를 배달하려 합니다. 배달할 물건은 모두 크기가 같은 재활용 택배 상자에 담아 배달하며, 배달을 다니면서 빈 재활용 택배 상자들을 수거하려 합니다. 
# 배달할 택배들은 모두 재활용 택배 상자에 담겨서 물류창고에 보관되어 있고, i번째 집은 물류창고에서 거리 i만큼 떨어져 있습니다. 또한 i번째 집은 j번째 집과 거리 j - i만큼 떨어져 있습니다. (1 ≤ i ≤ j ≤ n) 
# 트럭에는 재활용 택배 상자를 최대 cap개 실을 수 있습니다. 트럭은 배달할 재활용 택배 상자들을 실어 물류창고에서 출발해 각 집에 배달하면서, 빈 재활용 택배 상자들을 수거해 물류창고에 내립니다. 각 집마다 배달할 재활용 택배 상자의 개수와 수거할 빈 재활용 택배 상자의 개수를 알고 있을 때, 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리를 구하려 합니다. 각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있습니다.
# 다음은 cap=4 일 때, 최소 거리로 이동하면서 5개의 집에 배달 및 수거하는 과정을 나타낸 예시입니다.

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    delPoint = len(deliveries) - 1
    sumDel = sum(deliveries)
    sumPic = sum(pickups)
    for i in range(len(pickups)-1, -1, -1):
         if pickups[i] != 0:
            picPoint = i
            break
    while True:
        if sumPic == 0 and sumDel == 0:
            break
        delIndex, delWeight = 0, 0
        picIndex, picWeight = 0, 0
        if sumDel != 0:
            for i in range(delPoint, -1, -1):
                if cap < delWeight + deliveries[i]:
                    if delWeight + deliveries[i] == cap:
                        delPoint = i-1
                        sumDel -= deliveries[i]
                        deliveries[i] = 0
                    else:    
                        deliveries[i] -= (cap-delWeight)
                        sumDel -= (cap-delWeight)
                        delWeight = cap
                        delPoint = i
                        delIndex = max(i, delIndex)
                    break
                delWeight += deliveries[i]
                delIndex = max(i, delIndex)
                sumDel -= deliveries[i]
                deliveries[i] = 0
        if sumPic != 0:    
            for i in range(picPoint, -1, -1):
                if cap < picWeight + pickups[i]:
                    if picWeight + pickups[i] == cap:
                        picPoint = i-1
                        sumPic -= pickups[i]
                        pickups[i] = 0
                    else:    
                        pickups[i] -= (cap-picWeight)
                        sumPic -= (cap-picWeight)
                        picWeight = cap
                        picPoint = i
                        picIndex = max(i, picIndex)
                    break                
                picWeight += pickups[i]
                sumPic -= pickups[i]
                pickups[i] = 0
                picIndex = max(i, picIndex)
                
        answer += (max(delIndex+1, picIndex+1)*2)
        
    return answer
