import re
import time

instructions = []
comp = []
with open("d7.5.txt", "r") as file:
    for line in file:
        instructions.append(line.strip())    

wires = {}
for i in instructions:
    if re.search(r"(AND|OR|LSHIFT|RSHIFT|NOT)", i) is None: #input
        _ = i.split(" -> ") 
        try:
            check = int(_[0])
            wires.update({ _[1] : _[0]})
            comp.append(i)
        except ValueError:
            continue


def check_exist(x):
    global wires
    if "NOT" in x:
        _ = x.split(" ")
        vara = _[1]
        return vara in wires
    elif re.search(r"(AND)", x): 
        _ = x.split(" ")
        vara, varb = _[0], _[2]
        if vara == "1":
            return varb in wires
        else:
            return vara in wires and varb in wires
    elif re.search(r"(OR)", x):
        _ = x.split(" ")
        vara, varb = _[0], _[2]
        return vara in wires and varb in wires
    elif re.search(r"(LSHIFT|RSHIFT)", x):
        _ = x.split(" ")
        vara = _[0]
        return vara in wires
    elif re.match(r"\D{1,2} -> \D{1,2}", x):
        _ = x.split(" ")
        vara = _[0]
        return vara in wires
    else:
        return False


def operate(x):
    global wires
    global comp
    _ = x.split(" ")
    if "NOT" in x:
        inp, out = _[1], _[3]
        value = ~int(wires[inp]) & 0xffff
        wires.update({ out: value })
    elif re.match(r"\D{1,2} -> \D{1,2}", x):
        inp, out = _[0], _[2]
        wires.update({ out : int(wires[inp]) })
    elif re.search(r"(LSHIFT|RSHIFT|OR|AND)", x):
         inpa, inpb, out = _[0], _[2], _[4]
         if "LSHIFT" in x:
             value = int(wires[inpa]) << int(inpb)
             wires.update({ out : value })
         elif "RSHIFT" in x:
             value = int(wires[inpa]) >> int(inpb)
             wires.update({ out : value })
         elif "OR" in x:
             one = int(wires[inpa]) if inpa in wires else 0
             two = int(wires[inpb]) if inpb in wires else 0
             value = one | two 
             wires.update({ out : value})
         elif "AND" in x:
             if inpa == "1":
                 value = 1 & int(wires[inpb])
                 wires.update({ out : value})
             else:
                value = int(wires[inpa]) & int(wires[inpb])
                wires.update({ out : value})
    comp.append(x)

while len(comp) < len(instructions):
    for x in instructions:
        if x not in comp and check_exist(x) is True: 
                operate(x)


print(wires["a"])