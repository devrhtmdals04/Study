from __future__ import annotations

import math
from fractions import Fraction
from typing import Iterable, Sequence

Number = int | float | Fraction
Vector = Sequence[Number]
Matrix = Sequence[Sequence[Number]]


def dot(u: Vector, v: Vector) -> Number:
    if len(u) != len(v):
        raise ValueError("dot(): vectors must have the same length")
    return sum(a * b for a, b in zip(u, v, strict=True))


def norm(v: Vector) -> float:
    return math.sqrt(float(dot(v, v)))


def projection(u: Vector, v: Vector) -> list[Number]:
    vv = dot(v, v)
    if vv == 0:
        raise ValueError("projection(): cannot project onto the zero vector")
    scale = dot(u, v) / vv
    return [scale * x for x in v]


def transpose(A: Matrix) -> list[list[Number]]:
    if not A:
        return []
    row_lengths = {len(row) for row in A}
    if len(row_lengths) != 1:
        raise ValueError("transpose(): matrix must be rectangular")
    return [list(col) for col in zip(*A, strict=True)]


def matmul(A: Matrix, B: Matrix) -> list[list[Number]]:
    if not A or not B:
        return []
    a_rows, a_cols = len(A), len(A[0])
    if any(len(row) != a_cols for row in A):
        raise ValueError("matmul(): A must be rectangular")
    b_rows, b_cols = len(B), len(B[0])
    if any(len(row) != b_cols for row in B):
        raise ValueError("matmul(): B must be rectangular")
    if a_cols != b_rows:
        raise ValueError("matmul(): shapes do not align")

    Bt = transpose(B)
    out: list[list[Number]] = []
    for i in range(a_rows):
        out.append([dot(A[i], Bt[j]) for j in range(b_cols)])
    return out


def matvec(A: Matrix, x: Vector) -> list[Number]:
    if not A:
        return []
    cols = len(A[0])
    if any(len(row) != cols for row in A):
        raise ValueError("matvec(): matrix must be rectangular")
    if len(x) != cols:
        raise ValueError("matvec(): shapes do not align")
    return [dot(row, x) for row in A]


def identity(n: int, *, one: Number = 1, zero: Number = 0) -> list[list[Number]]:
    if n < 0:
        raise ValueError("identity(): n must be >= 0")
    return [[one if i == j else zero for j in range(n)] for i in range(n)]


def augment(A: Matrix, b: Iterable[Number]) -> list[list[Number]]:
    b_list = list(b)
    if len(A) != len(b_list):
        raise ValueError("augment(): A rows and b length must match")
    return [list(row) + [b_list[i]] for i, row in enumerate(A)]

