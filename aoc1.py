def main():
    instructions = input("")
    floor = proc(instructions)
    print("Floor", floor)

def proc(instr):
    n = 0
    for i in instr:
        if i == "(":
            n += 1
        else:
            n -= 1
    return n

main()
