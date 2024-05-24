x = 0
y = 0
a = 0
b = 0
pos = 0
hitmark = ["0x0"]
with open("d3_input.txt", "r") as file:
    instructions = file.read()
for i in instructions:
    if pos % 2 == 0: #even, Santa
        if i == "^":
            y += 1
        elif i == "v":
            y -= 1
        elif i == "<":
            x -= 1
        elif i == ">":
            x += 1
        coord = str(x) + "x" + str(y)
    else: #odd, Robo
        if i == "^":
            b += 1
        elif i == "v":
            b -= 1
        elif i == "<":
            a -= 1
        elif i == ">":
            a += 1        
        coord = str(a) + "x" + str(b)
    hitmark.append(coord)
    pos += 1
newmark = list(dict.fromkeys(hitmark))
print(len(newmark))