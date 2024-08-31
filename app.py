p = int(input("Enter Starting Range: "))
q = int(input("Enter the Ending Range: "))
h=[]
for x in range(p,q):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x,end="")
        h.append(x)
print()

lenght = len(h)
mid = lenght//2
print( "mid addition is: ",h[mid]+h[mid-1])