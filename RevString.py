def pusher(s):
    
    rev = ""
    j = len(s)-1
    
    while(0<=j):
        if(s[j]==" "):
            j = j - 1
            
        rev = rev + s[j]
        j = j - 1
    print(rev)
    
pusher("Akash is a good boy")
