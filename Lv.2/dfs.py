def main() :
    inputlist = list(map(int,input().split()))
    [i for i in range(int(inputlist[0]))]
    print(i)
    linelist = []
    dic = {}

    for i in range(inputlist[1]) :
        linelist = list(map(int,input().split()))
        if linelist[0] in dic :
            dic[linelist[0]].append(linelist[1])
        else:
            dic[linelist[0]] = [linelist[1]]
    
def dfs(node) :
    

main()