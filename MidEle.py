# this code is to find the middle element by reducing its time complexity by half

def midEle(s):
    
    beg = 0
    end = len(s)-1
    
    while(beg<end):
        
        beg = beg + 1
        end = end - 1
        
        if(beg>end):
            print("Even Mid Ele: ",s[end],",",s[beg])
            break
        elif (beg==end):
            print("Odd Mid Ele: ",s[beg])
            break
        
midEle("Akash Babu")
midEle("1234567890")
midEle("123456789")
midEle("123456789098765432345678987654ewasdfgyu765redcvghu7654edgy654waszxfr432qasxcvbnko987ygbnki87654ewsdcvb njhytre321234567890oijnmkiuytredcvbnju765redcvbhu65esdcvbhuy65redc66756567y8y6r56r465645r45r459")