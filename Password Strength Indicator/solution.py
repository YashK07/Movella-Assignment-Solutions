#take use input
#main function
import re
#a dictionary to map rules with the prompt messages
d = {"rule1":["Should contain atleast 8 characters",0],"rule2":["Should contain atleast 2 special chracters",0],"rule3":["Should contain atleast 2 numbers",0],"rule4":["Should not start with any number",0]}

def rule1(s,w): 
    if(len(s)>=8):
        d['rule1'][1] = w
        return w

    
    else:
        d['rule1'][1] = (w/8) * len(s)
        return (w/8) * len(s)

def rule2(s,w):
    count = 0
    regexp = re.compile('[^0-9a-zA-Z]+')
    for i in s:
        if(regexp.search(i)):
            count+=1
            
    if(count>=2):
        d['rule2'][1] = w
        return w
    
    else:
        d['rule2'][1] = (w/2) * count
        return (w/2) * count

def rule3(s,w):
    count = 0
    for i in s:
        if(str.isdigit(i)):
            count+=1
            
    if(count>=2):
        d['rule3'][1] = w
        return w
    
    else:
        d['rule3'][1] = (w/2) * count
        return (w/2) * count


def rule4(s,w):
    if(not str.isdigit(s[0])):
        d['rule4'][1] = w
        return w
    
    else:
        d['rule4'][1] = 0
        return 0
    

if(__name__=="__main__"):
    print("Enter the password: ")
    inp = input(str())
    strength = rule1(inp,0.4) + rule2(inp,0.25) + rule3(inp,0.25) + rule4(inp,0.1)
    scores = [d[i][1] for i in d]
    scores_1 = scores.copy()
    scores_1.sort()
    print("--------Password Strength Analysis-------")
    if(strength<0.75):
        if(strength<0.5):
            #print(strength)
            print("The strength of your password is: Weak!")

        elif((strength>=0.5) & (strength<0.75)):
            print("The strength of your password is: Average")

#finding the 2 rules the two rules that contribut lowest to the score
        min1 = scores_1[0]
        rule1 = list(d.keys())[scores.index(min1)]
        min2 = scores_1[1]
        if(min2==min1):
            scores.remove(min1)
            rule2 = list(d.keys())[scores.index(min2)+1]
        else:
            rule2 = list(d.keys())[scores.index(min2)]
        print("Score less than 75. These two rules contributing lowest to the strength of your password: \n" + "1. " + d[rule1][0] + "\n2. " + d[rule2][0])
        


            
    elif((strength>=0.75) & (strength<0.90)):
        print("The strength of your password is: Good!") 
        
    else:
        print("The strength of your password is: Very Good!!")    
