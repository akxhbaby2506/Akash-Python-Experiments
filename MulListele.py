def MullList(n):
    
    l = []
    print("Enter the elements inside the list:")
    for i in range(n):
        ele = int(input())
        l.append(ele)
    print(l)
    
    mull = 1
    for i in range(len(l)):
        mull = mull*l[i]
    print(mull)
    
MullList(4)