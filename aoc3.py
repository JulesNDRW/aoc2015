x = 0
y = 0
hitmark = ["0x0"]
with open("d3_input.txt", "r") as file:
    instructions = file.read()
for i in instructions:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == "<":
        x -= 1
    elif i == ">":
        x += 1
    coord = str(x) + "x" + str(y)
    hitmark.append(coord)
newmark = list(dict.fromkeys(hitmark))
print(len(newmark))