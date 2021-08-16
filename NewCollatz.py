import math
con = 4/3
for j in range(3,1000000,2):
    x = j
    fail = True
    for i in range(0,1000):
        if(x%2 == 0):
            x = round(x*.5)
        else:
            x = x * con
            x = round(x)
        #print(x)
        if(x == 4):
            fail = False
            break
    if(fail == True):
        print('dumb')
        print(x)
        
        
