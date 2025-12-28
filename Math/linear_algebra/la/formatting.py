from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence


def format_number(x: object) -> str:
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return str(x.numerator)
        return f"{x.numerator}/{x.denominator}"
    if isinstance(x, float):
        return f"{x:.6g}"
    return str(x)


def format_vector(v: Sequence[object]) -> str:
    return "[" + ", ".join(format_number(x) for x in v) + "]"


def format_matrix(A: Sequence[Sequence[object]]) -> str:
    rows = [list(map(format_number, row)) for row in A]
    if not rows:
        return "[]"

    col_count = max((len(row) for row in rows), default=0)
    widths = [0] * col_count
    for row in rows:
        for j, cell in enumerate(row):
            widths[j] = max(widths[j], len(cell))

    def fmt_row(row: Iterable[str]) -> str:
        padded = [(cell.rjust(widths[j])) for j, cell in enumerate(row)]
        return "[ " + "  ".join(padded) + " ]"

    return "\n".join(fmt_row(row) for row in rows)

