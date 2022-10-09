def main():
    answer = 0
    a, b = input().split()
    arr = [0]
    cnt, k = 1, 1
    for i in range(1, int(b)+1):
        arr.append(k)        
        if cnt == k :
            k += 1
            cnt = 0       
        cnt +=1
        if int(a) <= i :
            answer += arr[i]
    return answer
main()