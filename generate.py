from random import randint
from fractions import Fraction

file = open("Gauss_inverse/matrix.txt", 'w')
matrix = ""
n = randint(2,50)
choice = input("Use fractions? (Y/N) -> ").lower()
for i in range(n):
    for j in range(n):
        a = randint(1,100)
        b = randint(1,100) if choice == "y" else 1
        matrix += str(Fraction(a,b)) + " "
    matrix += '\n'
file.write(matrix)
print("MATRIX GENERATED SUCCESSFULLY!", n, "x", n)