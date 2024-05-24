import re
codes_list = []
code = 0
with open("d5_input.txt", "r") as file:
    for line in file:
        codes_list.append(line.strip())

def a(co):
    return bool(re.search(r"(..).*\1", co))
def b(co):
    return bool(re.search(r"(.).\1", co))

for i in codes_list:
    if a(i) and b(i):
        code += 1

print(code)
