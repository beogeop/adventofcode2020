file = open("input.txt", "r")
list = []

for line in file:
    index = 0
    index1 = 0
    for i in range(0, len(line)):
        curr = line[i]
        if curr == ":":
            index = i
        elif curr == "-":
            index1 = i

    target = line[index-1]
    low = line[0:index1]
    high = line[index1+1:index1+3]

    if 