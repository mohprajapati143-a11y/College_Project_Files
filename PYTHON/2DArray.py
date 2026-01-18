import numpy as np

array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print("2-d array:")
print(array_2d)

print("\nElement at(1,2):", array_2d[1, 2])
print(" first row:", array_2d[0])

array_2d[0, 1] = 99
print("\n Modified array:")
print(array_2d)

print("\nElement in the array:")
for row in array_2d:
    for element in row:
        print(element, end=' ')

print("\nMOHIT PRAJAPATI")
print("FYCS")
print("22549")
