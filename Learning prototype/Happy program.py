st="Happy"
#print(len(st))
for i in range(len(st)):
    print(f"{st[:i+1]:}{st[len(st)-(i+1):]:>20}")