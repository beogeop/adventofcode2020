file = open("Day1.txt", "r")
list = []
iter = []

for i in file:
    list.append(int(i))

x = range(1, len(list)-1)
for j in x:
    iter.append(int(j))
    
y = 0

for num in list:
    if list[0] + list[iter[y]] != 2020:
        y + 1
    elif list[0] + list[iter[y]] == 2020:
        print(list[0] * list[iter[y]])

