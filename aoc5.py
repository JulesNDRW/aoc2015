
import re
codes_list = []
code = 0
with open("d5_input.txt", "r") as file:
    for line in file:
        codes_list.append(line.strip())
#list of each code has been created
#each test
def a(co):
    if re.search(r"(ab|cd|pq|xy)", co):
        return False
    else:
        return True
def b(co):
    return bool(re.search(r".*[aeiou].*[aeiou].*[aeiou].*", co))

def c(co):
    return bool(re.search(r"(.)\1", co))

for i in codes_list: #going through each code
    if a(i) and b(i) and c(i):
        code += 1

print(code)
