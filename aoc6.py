#generating lights
grid = {}
for i in range(1000): #this i refers to the x axis, you move to a new column each loop
    y = 0
    for _ in range(1000): #goes up the column
        light = str(i)+"x"+str(y)
        grid.update({light:False})
        y += 1

#reads the instructions
instr_list = []
with open("d6_input.txt", "r") as file:
    for line in file:
        instr_list.append(line.strip())

#extraction process
def isolate(x):
    #"turn on 417,480 through 860,598"
    _ = []
    _ = x.split(" ")
    start = _[2] #"417,480"
    end = _[4] #"860,598"
    s_x, s_y = start.split(",") #417, 480
    e_x, e_y = end.split(",") #860, 598
    return s_x, s_y, e_x, e_y
#define three types of instructions
def on(x):
    #"turn on 417,480 through 860,598"
    global grid
    s_x, s_y, e_x, e_y = isolate(x)
    x = int(s_x)
    y = int(s_y)
    ex = int(e_x)
    ey = int(e_y)
    for i in range(ex-x+1):
        coordy = y
        for w in range(ey-y+1):
          coordx = x + i
          coordy = y + w
          coord = str(coordx)+"x"+str(coordy)
          grid[coord] = True
def off(x):
    #"turn off 23,935 through 833,962"
    global grid
    s_x, s_y, e_x, e_y = isolate(x)
    x = int(s_x)
    y = int(s_y)
    ex = int(e_x)
    ey = int(e_y)
    for i in range(ex-x+1):
        coordy = y
        for w in range(ey-y+1):
          coordx = x + i
          coordy = y + w
          coord = str(coordx)+"x"+str(coordy)
          grid[coord] = False
def toggle(x):
    #"toggle 720,196 through 897,994"
    global grid
    _ = []
    _ = x.split(" ")
    start = _[1]
    end = _[3]
    s_x, s_y = start.split(",")
    e_x, e_y = end.split(",")
    x = int(s_x)
    y = int(s_y)
    ex = int(e_x)
    ey = int(e_y)
    for i in range(ex-x+1):
        coordy = y
        for w in range(ey-y+1):
          coordx = x + i
          coordy = y + w
          coord = str(coordx)+"x"+str(coordy)
          if grid[coord] is True:
              grid[coord] = False
          elif grid[coord] is False:
              grid[coord] = True

#follow instructions
for i in instr_list:
    if i.startswith("turn on"):
        on(i)
    elif i.startswith("turn off"):
        off(i)
    elif i.startswith("toggle"):
        toggle(i)

#checks how many lights in the grid are on.
lights = 0
for val in grid.values():
    if val:
        lights += 1
print(lights)
print(grid)