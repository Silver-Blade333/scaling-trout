a = [10, 3, 5]
t = 0
#print(len(a))
if len(a) <= 1000:
    for i in a:
        if -10**6 <= i <= 10**6:
            t = t + i
            #print(t)
        else:
         continue
else:
    print("Please enter only 1000 elements")
print(t)
