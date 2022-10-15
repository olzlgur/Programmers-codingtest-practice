from itertools import *

def main():
    min, max = 1e9, -1e9
    num = int(input())
    arr = input().split()
    temp = list(map(int, input().split()))
    operator = setarr(temp[0], '+') + setarr(temp[1], '-') + setarr(temp[2], '*') + setarr(temp[3], '//')
    strex = arr[0]
    if num == 2 :
        print(eval(arr[0]+operator[0]+arr[1]))
        print(eval(arr[0]+operator[0]+arr[1]))
        return
    for tu in permutations(operator) :
        for i in range(1, num) :
            strex = str(eval(strex + tu[i-1] + arr[i]))
        if eval(strex) > max :
            max = eval(strex)
        if eval(strex) < min:
            min = eval(strex)
        strex = arr[0]
    print(max)
    print(min)
def setarr(a, b):
    temparr = []
    for i in range(a) :
        temparr.append(b)
    return temparr
main()