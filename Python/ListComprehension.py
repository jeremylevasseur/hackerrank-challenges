from pprint import pprint

def cuboidDimensions(x, y, z, n):

    coordinates = []

    for i in range(x + 1):

        for j in range(y + 1):

            for k in range(z + 1):

                if i + j + k != n:

                    coordinates.append([i, j, k])


    pprint(coordinates)
    return coordinates



x = 1
y = 1
z = 2
n = 3

cuboidDimensions(x, y, z, n)