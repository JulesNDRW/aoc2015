instr = input()
n = 0
pos = 0
for i in instr:
    if i == "(":
        n += 1
        pos += 1
    else:
        n -= 1
        pos += 1
    if n < 0:
        break
print(pos)