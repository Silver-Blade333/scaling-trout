a=list(input("Enter the values separated by comma:").split(","))
for i in range(len(a)):
    a[i]=int(a[i])
print("The Maximum value is ", max(a))
print("The Minimum value is ", min(a))