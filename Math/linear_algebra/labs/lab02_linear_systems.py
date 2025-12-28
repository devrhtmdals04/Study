from __future__ import annotations

from fractions import Fraction

from la import format_matrix, format_vector, solve


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
    print("RREF([A|b]) =")
    print(format_matrix(sol.rref))
    print()
    print("status =", sol.status)
    print("particular =", None if sol.particular is None else format_vector(sol.particular))
    if sol.nullspace_basis:
        print("nullspace basis:")
        for v in sol.nullspace_basis:
            print("  ", format_vector(v))


if __name__ == "__main__":
    main()

