from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Literal, Sequence

from .ops import augment
from .rref import rref

Number = int | float | Fraction


@dataclass(frozen=True)
class LinearSystemSolution:
    status: Literal["unique", "infinite", "inconsistent"]
    particular: list[Number] | None
    free_vars: list[int]
    nullspace_basis: list[list[Number]]
    pivots: list[int]
    rref: list[list[Number]]


def solve(
    A: Sequence[Sequence[Number]],
    b: Sequence[Number],
    *,
    exact: bool = False,
    tol: float = 1e-12,
) -> LinearSystemSolution:
    """
    Solve Ax=b via RREF.

    Returns:
    - unique       : particular only
    - infinite     : particular + nullspace_basis (general solution)
    - inconsistent : no solution
    """

    if not A:
        return LinearSystemSolution(
            status="unique",
            particular=[],
            free_vars=[],
            nullspace_basis=[],
            pivots=[],
            rref=[],
        )

    row_count = len(A)
    col_count = len(A[0])
    if any(len(row) != col_count for row in A):
        raise ValueError("solve(): A must be rectangular")
    if len(b) != row_count:
        raise ValueError("solve(): b length must match A rows")

    aug = augment(A, b)
    rref_aug, pivots_aug = rref(aug, exact=exact, tol=tol)

    if col_count in pivots_aug:
        return LinearSystemSolution(
            status="inconsistent",
            particular=None,
            free_vars=[],
            nullspace_basis=[],
            pivots=[c for c in pivots_aug if c < col_count],
            rref=rref_aug,
        )

    pivots = [c for c in pivots_aug if c < col_count]
    free_vars = [j for j in range(col_count) if j not in set(pivots)]

    particular: list[Number] = [0] * col_count
    for i, pivot_col in enumerate(pivots):
        particular[pivot_col] = rref_aug[i][col_count]

    if len(pivots) == col_count:
        return LinearSystemSolution(
            status="unique",
            particular=particular,
            free_vars=[],
            nullspace_basis=[],
            pivots=pivots,
            rref=rref_aug,
        )

    basis: list[list[Number]] = []
    for f in free_vars:
        v: list[Number] = [0] * col_count
        v[f] = Fraction(1) if exact else 1
        for i, pivot_col in enumerate(pivots):
            v[pivot_col] = -rref_aug[i][f]
        basis.append(v)

    return LinearSystemSolution(
        status="infinite",
        particular=particular,
        free_vars=free_vars,
        nullspace_basis=basis,
        pivots=pivots,
        rref=rref_aug,
    )

