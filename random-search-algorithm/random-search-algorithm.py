import random

result = []

itr = 0 
lastZ = 0

print("Denenen seçenekler:\n","*"*50)
while(itr <= 32):
    
    x1 = random.randint(0,1)    
    x2 = random.randint(0,1)    
    x3 = random.randint(0,1)    
    x4 = random.randint(0,1)    
    x5 = random.randint(0,1)    

    result = [x1 , x2, x3, x4, x5]
    print(result)

    cons1 = 3*x1 + x2 + 3*x3 + 2*x4 +4*x5
    cons2 = x3 - x4
    cons3 = x2 - x5
    cons4 = x1 + x2 + x3 + x4 + x5
    
    if cons1>=10 and cons2<=0 and cons3<=0 and cons4>=4:
        maxZ = x1 + 3*x2 - 2*x3 + 2*x4 - x5
        result2 = [x1,x2,x3,x4,x5]

        if maxZ > lastZ :
            lastZ = maxZ
        else:
            next
    else:
        next

    itr += 1

print(f"Uygun çözüme ilişkin matris: {result2} ")
print(f"Maximize olarak bulunmuş olan sonuç ise: \nMaxZ = {lastZ}")
print("*"*50)




