class BinaryOperations():
    
    def __init__(self):
        pass

    def Decimal_to_Binary(self, value):
        if value > 1:
            self.Decimal_to_Binary(value//2)
        print(value % 2,sep="",end="")

    def Add(self, a, b):
        self.sum = a + b
        self.Decimal_to_Binary(self.sum)
        print()

    def Sub(self, a, b):
        if(a>b):
            self.diff = a - b
            self.Decimal_to_Binary(self.diff)
            print();
        elif(a==b):
            return 0
        else:
            print("Use optimal metod");

B = BinaryOperations()
B.Decimal_to_Binary(8)
print()
B.Add(15, 32)
B.Sub(32,15)
