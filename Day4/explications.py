list_1 = [444, 5155, 8818]
list_2 = [100, 101, 1011]
list_3 = [200, 1599, 202]


list_4 = [
    [444, 5155, 8818],  # i
    [100, 101, 1011],  # i
    [200, 1599, 202]  # i
]

list_5 = [
    list_1,
    list_2,
    list_3
]

# print(list_4[0][0])  # list_4[0] <=> i
# print(list_4[1][0])  # list_4[1] <=> i
# print(list_4[2][0])  # list_4[2] <=> i

# print(list_4[0][1])  # list_4[0] <=> i
# print(list_4[1][1])  # list_4[1] <=> i
# print(list_4[2][1])  # list_4[2] <=> i

# print(list_4[0][2])  # list_4[0] <=> i
# print(list_4[1][2])  # list_4[1] <=> i
# print(list_4[2][2])  # list_4[2] <=> i


# Afficher la première colonne de ta matrice
# list_4 = [
#     [444, 5155, 8818],  # i = 0 (0, 1, 2)
#     [100, 101, 1011],  # i = 1 (0,1,2)
#     [200, 1599, 202]  # i = 2 (0,1,2)
# ]
for i in list_4:
    print(i[0], i[1], i[2]) # afficher la première ligne
