import random
import pandas as pd
import math 
from datetime import datetime
start_time = datetime.now()

x = 0
y = 0
pivot = [x,y]
delta = 0.01
z = math.sin(x) + math.tan(y) + 1.25**(x+y)
z_copy = z
pivot_copy = pivot

itr = 0
while itr < 999:
    cond1 = (pivot[0]>=0) & (pivot[0]<=10)
    cond2 = (pivot[1]>=0) & (pivot[1]<=10) 
    if cond1 == cond2:  # Starting conditions 
        maxZ = math.sin(pivot[0]) + math.tan(pivot[1]) + 1.25**(pivot[0]+pivot[1])
        print(f"\n {itr+1}. deneme ====> ")
        print("*"*40)
        print("Instant Pivot point: ",pivot)
        print("Instant pivots value: ",maxZ)

        def neighbors(pivot):
            neighbors = []
            for i in range(len(pivot)):
                pivot_c = pivot.copy()
                pivot_c[i] = pivot[i] + delta
                pivot_c[i] = round(pivot_c[i],2)
                neighbors.append(pivot_c)
                
            for i in range(len(pivot)):
                pivot_c = pivot.copy()
                pivot_c[i] = pivot[i] - delta
                pivot_c[i] = round(pivot_c[i],2)
                neighbors.append(pivot_c)

            return neighbors
        
        def neighbors_value(pivots_neighbor):
            values = []
            for i in pivots_neighbor:
                x = i[0]
                y = i[1]
                z = math.sin(x) + math.tan(y) + 1.25**(x+y)
                z = round(z,4)
                values.append(z)
            
            return values 

        def neighbors_probabilities(pivots_values):
            probabs = []
            sumValues = sum(pivots_values)
            for i in pivots_values:
                values = round((i/sumValues),4)
                probabs.append(values)

            return probabs

        def probabs_frequencies(pivots_probabs):
            frequencies = []
            sum = 0
            for i in pivots_probabs:
                sum += i
                frequencies.append(sum)
            
            return frequencies


        pivots_neighbors = neighbors(pivot) # Find neighbors
        pivots_values = neighbors_value(pivots_neighbors)   # Find neighbors value
        pivots_probabs = neighbors_probabilities(pivots_values)   # Find neighbors probabilities

        data = {'Neighbors':pivots_neighbors,
                'Values':pivots_values,
                'Probabilities':pivots_probabs}
        
        df = pd.DataFrame(data)  # Occuring the data frame
        df.sort_values('Probabilities' , ascending=True , inplace = True)
        
        pivots_frequencies = probabs_frequencies(pivots_probabs) # Find frequencies
        df['Frequencies'] = pivots_frequencies  # Add Frequencies column in dataframe 
        df.iloc[0,3] = 0    # Set 1st value of frequencies is zero 
        print("\nSorted data frame: \n",df)
        
        choice = round(random.uniform(0,1),4) # Choose a random number
        print(f"\n Choosen number: {choice} \n")

        for i in df.iloc[:,3]:
            if choice <= i:
                row = df.loc[df['Frequencies']==i]
                print(row)
                print("\nChoosen neighbor: ", row.iloc[0,0])
                newPivot = row.iloc[0,0]
                newPivotsValue = row.iloc[0,1]
                break
            else:
                next

        lastZ = math.sin(newPivot[0]) + math.tan(newPivot[1]) + 1.25**(newPivot[0]+newPivot[1])
        
        if lastZ >= maxZ :
            pivot = newPivot
            print("-"*40)
            print(f"New pivot point: {newPivot} \t New pivots value: {newPivotsValue}")
        
        else:
            print(f"Last pivot point: {pivot} \t Last pivots value: {maxZ}")
        itr += 1
    else:
        print("Out of range! (x or y is not in [0;10] range)")
        break

print("*"*50)
print(f"End of the {itr+1} times tests: ")
print(f"Starting pivot point: {pivot_copy} \t Pivots value: {z_copy}")
print(f"Last pivot point: {pivot} \t last pivots value: {maxZ}")

end_time = datetime.now()
print('\nHesaplama süresi: {}'.format(end_time - start_time))