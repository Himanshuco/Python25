"Calculating maximum and minimum"

import sys
min =sys.maxsize
max=0
index=0
a =[2,9,0,4,5,-1]
for i in a:
    if(i<min):
        min=i
print("Minimum value is:",min)


for i in range(0,len(a)):
    if(a[i]>max):
        max=a[i]
        index=i
print("The maximum value is",max,'at index : ',index)