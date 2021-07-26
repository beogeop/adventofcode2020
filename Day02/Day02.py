file = open("input.txt", "r")
list = []
list1 = []
list2 = []

for i in file:
    list.append(i)

for i in list:
    list1.append(i.split())
    for j in list1:
        list2.append(int(j[0]).split("-"))

print(list2)