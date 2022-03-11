import random as rn

stat = 0
while (stat == 0):
    # random solution:
    Xm = []
    for i in range(0,6):
        Xm.append(rn.randint(0,1))

    # calculate pivot solution:
    x1 = Xm[0]
    x2 = Xm[1]
    x3 = Xm[2]
    x4 = Xm[3]
    x5 = Xm[4]
    x6 = Xm[5]

    cons1 = (3*x1 + x2 + 3*x3 + 2*x4 + 4*x5 + x6) >= 11
    cons2 = (x3 - x4) <= 0
    cons3 = (x2 - x5) <= 0
    cons4 = (x2 + x4 + x6) >=3
    
    if cons1 == cons2 == cons3 == cons4 == True:       
        maxZ = x1 + 3*x2 - 2*x3 + 2*x4 - x5 +2*x6
        print(f"\nTrying random pivot matrix {Xm} => ",maxZ)
        stat = 1
    else:
        stat = 0

stat = 0
while(stat <= 9):
    # find 3 neighbors index: 
    index = []
    for i in range(0,3):
        index.append(rn.randint(0,5))


    # set neighbors index are different each other:
    itr=0
    while(itr==0):
        for j in range(0,3):
            if index.count(index[j]) > 1:
                index[j] = rn.randint(0,5)
                itr = 0
            else:
                itr = 1



    # find the best neighbor:
    for i in index:
        Xc=Xm.copy()
        if Xm[i] == 1:
            Xc[i] = 0
        else:
            Xc[i] = 1
        print("\nTrying neighbor",Xc)
        x1 = Xc[0]
        x2 = Xc[1]
        x3 = Xc[2]
        x4 = Xc[3]
        x5 = Xc[4]
        x6 = Xc[5]

        lastZ = x1 + 3*x2 - 2*x3 + 2*x4 - x5 +2*x6
        print("last highest result get right the conditions:",maxZ)
        print("Neighbors result:",lastZ)
        print("*"*30)
        
        cons1 = (3*x1 + x2 + 3*x3 + 2*x4 + 4*x5 + x6) >= 11
        cons2 = (x3 - x4) <= 0
        cons3 = (x2 - x5) <= 0
        cons4 = (x2 + x4 + x6) >=3

        if cons1 == cons2 == cons3 == cons4 == True:
            if lastZ >= maxZ:
                maxZ = lastZ
                xMax = Xc
                Xm = xMax
            else:
                Xmax = Xm
        else:
            xMax = Xm
        
    stat += 1

print("The best matrix: ",xMax)
print("The best result of end of tests: ",maxZ)