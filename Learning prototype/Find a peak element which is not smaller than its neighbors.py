a=list((input("Enter the values separated by comma:")).split(","))
for i in range(len(a)):
    a[i] = int(a[i])
#print(type(a))
#print(type(a[i]))
#print(a)
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        break
print(a[i+1])