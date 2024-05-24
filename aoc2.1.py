inpt = []
preslist = []
ribbon = 0
#read input and create list of dimensions
with open("d2_input.txt", "r") as file:
    for line in file:
        inpt.append(line)
#split dimensions into individual numbers
for i in inpt:
    item = i.split("x")
    preslist.append(item)
#look at each present individually, each present is a list
for pr in preslist:
    l = int(pr[0])
    w = int(pr[1])
    h = int(pr[2])
    sides = []
    sides.append(l)
    sides.append(w)
    sides.append(h)
    sides.sort()
    x = sides[0]
    y = sides[1]
    ribbon += 2*x + 2*y + l*w*h

print(ribbon)