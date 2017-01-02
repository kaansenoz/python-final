#Kaan Senoz Soru 1
with open('string.txt', 'r') as r:

    list = []

    all = r.readlines()

for column in all :
    list.append(int(column[11:14]))
    list.sort()

print list
