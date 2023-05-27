l = ["Akash","Nagraj","Rakshith","Varun","Hegde","Sushruth"]

while True:
    print("Hello...This is Babu Bot, Let me check your name in the list")
    n = input("Enter your name: ")
    n = n.title()
    
    if n in l:
        print("Hello ",n," your name is in the list")
        rem = input("Would you like to be removed from the list y/n?")
        
        if(rem=="y"):
            print("OK! you will be removed")
            l.remove(n)
            print(l)
        else:
            print("You are there in the list")
    else:
        print("Hello ",n," your name is not there in the list")
        adder = input("Do you want to be added in this list y/n?")
        if (adder=="y"):
            l.append(n)
            print("Okayy...Your name is added to the list")
            print(l)
            
        else:
            print("Allright your name wont be added to the list")