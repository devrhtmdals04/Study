from __future__ import annotations

from fractions import Fraction

from la import det, format_matrix, identity, inverse, matmul


def main() -> None:
    A = [
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0],
    ]
    A = [[Fraction(x) for x in row] for row in A]

    print("A =")
    print(format_matrix(A))
    print()
    print("det(A) =", det(A, exact=True))
    print()
    A_inv = inverse(A, exact=True)
    print("A^{-1} =")
    print(format_matrix(A_inv))
    print()
    print("A * A^{-1} =")
    print(format_matrix(matmul(A, A_inv)))
    print()
    print("I =")
    print(format_matrix(identity(3, one=Fraction(1), zero=Fraction(0))))


if __name__ == "__main__":
    main()

