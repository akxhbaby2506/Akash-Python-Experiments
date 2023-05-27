def DecimaltoBinary(num):
    
    if num>1:
        DecimaltoBinary(num//2)
    print(num%2, end='')

a = int(input("a = "))
b = int(input("b = "))

sum = a + b
DecimaltoBinary(sum)
print()
#Decimal to Binary using in-built function

def binary(num):
    print(bin(num)[2:])
binary(52)