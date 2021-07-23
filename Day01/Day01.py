file = open("input.txt", "r")
list = []

for i in file:
    list.append(int(i))

for i, v1 in enumerate(list):
    for j, v2 in enumerate(list[i+1:]):
        if v1 + v2 == 2020:
            print(v1 * v2)
        for v3 in list[i+j+1:]:
            if v1 + v2 + v3 == 2020:
                print(v1 * v2 * v3)
    
    