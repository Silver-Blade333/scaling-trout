number = int(input("Enter the number to find it's prime factors:"))
num = number
F = []
n = 2
if number == 1:
    print(number, "neither prime nor composite")
else:
    while n <= num:
        if num % n == 0:
            F.append(n)
            num = num/n
        if num % n != 0:
            n += 1
    print(F)




