list_tuple = [(12, 23), (54, 134), (45, 23), (65, 32)]

for coordinates in list_tuple:
    print(coordinates[0], coordinates[1])

list_tuple.remove((12, 23))
print(list_tuple)