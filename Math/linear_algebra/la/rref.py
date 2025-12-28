from __future__ import annotations

from fractions import Fraction
from typing import Sequence

Number = int | float | Fraction
Matrix = Sequence[Sequence[Number]]


def _is_zero(x: Number, *, exact: bool, tol: float) -> bool:
    if exact:
        return x == 0
    return abs(float(x)) <= tol


def rref(A: Matrix, *, exact: bool = False, tol: float = 1e-12) -> tuple[list[list[Number]], list[int]]:
    """
    Reduced row echelon form (Gauss-Jordan).

    - exact=True  : Fraction 기반(정확), 입력은 int/Fraction 권장
    - exact=False : float 기반(근사)
    """

    if not A:
        return [], []
    row_count = len(A)
    col_count = len(A[0])
    if any(len(row) != col_count for row in A):
        raise ValueError("rref(): matrix must be rectangular")

    M: list[list[Number]] = [list(row) for row in A]
    if exact:
        M = [[x if isinstance(x, Fraction) else Fraction(x) for x in row] for row in M]

    pivots: list[int] = []
    row = 0

    for col in range(col_count):
        if row >= row_count:
            break

        pivot_row = None
        if exact:
            for r in range(row, row_count):
                if M[r][col] != 0:
                    pivot_row = r
                    break
        else:
            pivot_row = max(range(row, row_count), key=lambda r: abs(float(M[r][col])))
            if _is_zero(M[pivot_row][col], exact=exact, tol=tol):
                pivot_row = None

        if pivot_row is None:
            continue

        if pivot_row != row:
            M[row], M[pivot_row] = M[pivot_row], M[row]

        pivot = M[row][col]
        if _is_zero(pivot, exact=exact, tol=tol):
            continue

        M[row] = [x / pivot for x in M[row]]

        for r in range(row_count):
            if r == row:
                continue
            factor = M[r][col]
            if _is_zero(factor, exact=exact, tol=tol):
                continue
            M[r] = [x - factor * y for x, y in zip(M[r], M[row], strict=True)]

        if not exact:
            for r in range(row_count):
                for c in range(col_count):
                    if _is_zero(M[r][c], exact=exact, tol=tol):
                        M[r][c] = 0.0

        pivots.append(col)
        row += 1

    return M, pivots

