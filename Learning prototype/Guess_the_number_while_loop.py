import random
cp = random.randint(1, 20)
num = int(input("Guess my pick between 1 to 20(Total 4 attempts):"))
attempt = 0
# if num == cp:
#     print("You Won!")
while num != cp and attempt < 3:
    if num > cp:
        print("You can't find my secret, Its smaller than you expect")
    else:
        print("I have a better choice which is larger than this")
    #print(attempt)
    attempt += 1
    num = int(input("Try again: "))
if attempt <= 3 and num != cp:
    print("Sorry all you're efforts in Loss. My number is ", cp)
else:
    print("You Won!")