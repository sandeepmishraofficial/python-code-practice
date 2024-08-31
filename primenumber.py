p = int(input("Enter Starting Range: "))
q = int(input("Enter Ending Range: "))
h = []

for x in range(p, q):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x, end=" ")
        h.append(x)

print()

length = len(h)
mid = length // 2
print(h[mid] + h[mid - 1])
