file = open("input.txt", "r")
list = []
list1 = []
list2 = []
list3 = []

for i in file:
    list.append(i)

for i in list:
    list1.append(i.split())
    
for j in list1:
    list2.append(j[0].split("-"))

for i in list1:
    x = i[1].replace(":", "")
    list3.append(x)

print(list3)