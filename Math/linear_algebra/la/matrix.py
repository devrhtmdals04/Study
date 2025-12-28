from __future__ import annotations

from fractions import Fraction
from typing import Sequence

from .ops import identity
from .rref import rref

Number = int | float | Fraction
Matrix = Sequence[Sequence[Number]]


def det(A: Matrix, *, exact: bool = False, tol: float = 1e-12) -> Number:
    if not A:
        return Fraction(1) if exact else 1
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("det(): matrix must be square")

    M: list[list[Number]] = [list(row) for row in A]
    if exact:
        M = [[x if isinstance(x, Fraction) else Fraction(x) for x in row] for row in M]

    sign: Number = Fraction(1) if exact else 1.0

    for col in range(n):
        pivot_row = None
        if exact:
            for r in range(col, n):
                if M[r][col] != 0:
                    pivot_row = r
                    break
        else:
            pivot_row = max(range(col, n), key=lambda r: abs(float(M[r][col])))
            if abs(float(M[pivot_row][col])) <= tol:
                pivot_row = None

        if pivot_row is None:
            return Fraction(0) if exact else 0.0

        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]
            sign = -sign

        pivot = M[col][col]
        for r in range(col + 1, n):
            factor = M[r][col] / pivot
            if exact and factor == 0:
                continue
            if not exact and abs(float(factor)) <= tol:
                continue
            for c in range(col, n):
                M[r][c] = M[r][c] - factor * M[col][c]

    diag_prod: Number = Fraction(1) if exact else 1.0
    for i in range(n):
        diag_prod *= M[i][i]
    return sign * diag_prod


def inverse(A: Matrix, *, exact: bool = False, tol: float = 1e-12) -> list[list[Number]]:
    if not A:
        return []
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("inverse(): matrix must be square")

    one: Number = Fraction(1) if exact else 1
    zero: Number = Fraction(0) if exact else 0
    I = identity(n, one=one, zero=zero)
    aug = [list(row) + I[i] for i, row in enumerate(A)]

    rref_aug, pivots = rref(aug, exact=exact, tol=tol)
    if any(p >= n for p in pivots):
        raise ValueError("inverse(): matrix is not invertible")

    for i in range(n):
        for j in range(n):
            val = rref_aug[i][j]
            if i == j:
                if exact and val != 1:
                    raise ValueError("inverse(): matrix is not invertible")
                if not exact and abs(float(val) - 1.0) > tol:
                    raise ValueError("inverse(): matrix is not invertible")
            else:
                if exact and val != 0:
                    raise ValueError("inverse(): matrix is not invertible")
                if not exact and abs(float(val)) > tol:
                    raise ValueError("inverse(): matrix is not invertible")

    return [row[n:] for row in rref_aug[:n]]

