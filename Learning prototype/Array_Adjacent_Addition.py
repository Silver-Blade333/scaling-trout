num = []
p = input("enter the values separated by comma:")
num = p.split(",")
# print(len(num))
# for x in num:
# num[x]=int(num[x])
# print(type(num))
try:
    if 0 < len(num) < 1000:
        for i in range(len(num)):
            # num[i]=float(num[i])
            # print(type(num[i]))
            if 10**3 > float(num[i]) > 10**-3 and i <= (len(num)-2):
                a = list()
                for i in range(len(num)-1):
                    # print(len(num)-1)
                    a.append(float(num[i])+float(num[i+1]))
        print(a)
except:
    print("Illegal entry")
