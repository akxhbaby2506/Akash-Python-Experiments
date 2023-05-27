def AddList(n):
    l = []
    #Input list elements
    print("Elements inside the list")
    for i in range(n):
        ele = int(input())
        l.append(ele)
    print(l)
    
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    print(sum)
    
AddList(6)