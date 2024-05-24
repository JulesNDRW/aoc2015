inpt = []
preslist = []
paper = 0
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
    a = l*w
    b = w*h
    c = h*l
    sides = []
    sides.append(a)
    sides.append(b)
    sides.append(c)
    sides.sort()
    SA = 2*a + 2*b + 2*c + sides[0]
    paper += SA

print(paper)