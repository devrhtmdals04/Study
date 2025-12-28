#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

from la import det, format_matrix, format_vector, inverse, solve


def main() -> None:
    A = [
        [1, 2, -1],
        [2, 3, 1],
        [-1, 1, 2],
    ]
    b = [1, 5, 0]

    A = [[Fraction(x) for x in row] for row in A]
    b = [Fraction(x) for x in b]

    sol = solve(A, b, exact=True)

    print("A =")
    print(format_matrix(A))
    print("b =", format_vector(b))
    print()
    print("status =", sol.status)
    print("particular =", None if sol.particular is None else format_vector(sol.particular))
    print()
    print("det(A) =", det(A, exact=True))
    print("A^{-1} =")
    print(format_matrix(inverse(A, exact=True)))


if __name__ == "__main__":
    main()
