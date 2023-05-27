l = []

for i in range(8):
    ele = int(input())
    l.append(ele)
    
print(l)
s = set(l)
L = list(s)
L = sorted(L)
print(L)
print(L[-2])