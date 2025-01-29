from fractions import Fraction
import time

def parse_matrix(matrix: str) -> list[list[Fraction]]:
    matrix_txt = matrix.split("\n")
    matrix: list = []
    for i in range(len(matrix_txt)):
        if matrix_txt[i].strip() != '':
            new_line = matrix_txt[i].split()
            matrix.append([Fraction(new_line[j]) for j in range(len(new_line))])
    return matrix


def print_matrix(matrix: list[list[Fraction]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            item = matrix[i][j]
            if '/' in str(item):
                a, b = str(item).split('/')
                if len(a)>10 and len(b)>10:
                    item = round(int(a)/int(b), 4)
            print(item, end='\t')
        print()
    return None


def isSquare(matrix: list[list[Fraction]]) -> bool:
    for line in matrix:
        if len(matrix) != len(line):
            return False
    return True


def inverse(matrix: list[list[Fraction]]):
    I = [[1 if i==j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    pivots = 1
    for j in range(len(matrix)):
        cur = matrix[j][j]
        if cur == 0: return 0, 0
        pivots *= cur
        for i in range(len(matrix)):
            if i!=j:
                k = -matrix[i][j]/cur
                for t in range(j, len(matrix)):
                    matrix[i][t] += matrix[j][t]*k
                for t in range(len(I)):
                    I[i][t] += I[j][t]*k
    for i in range(len(I)):
        cur = matrix[i][i]
        matrix[i][i] = cur / cur
        for j in range(len(I)):
            I[i][j] /= cur

    return pivots, I


def main():
    start = time.time()
    file = open("Gauss_inverse/matrix.txt", 'r', encoding="utf-8")
    matrix = parse_matrix(file.read())
    print(f"{"REQUESTED MATRIX":=^50}")
    print_matrix(matrix)
    print(f"{"=":=^50}"+'\n')
    if not isSquare(matrix):
        print("MATRIX IS NOT SQUARE")
        return -1
    A = inverse(matrix)
    det = A[0]
    if det == 0:
        print("DETERMINANT IS ZERO")
        return -1
    print("DETERMINANT =", det, "=", det.numerator/det.denominator, '\n')
    print(f"{"INVERSE MATRIX":=^50}")
    print_matrix(A[1])
    print(f"{"=":=^50}"+'\n')
    end = time.time()
    print(f"PROGRAM ENDED IN {round(end-start, 5)} sec.")


if __name__ == "__main__":
    main()