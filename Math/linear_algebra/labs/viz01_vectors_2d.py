from __future__ import annotations

import argparse
from pathlib import Path

from la import dot, norm, projection


def _arrow(ax, v: list[float], *, color: str, label: str) -> None:
    ax.quiver(
        0,
        0,
        v[0],
        v[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=color,
        width=0.006,
    )
    ax.text(v[0], v[1], f"  {label}", color=color, va="center")


def main() -> None:
    parser = argparse.ArgumentParser(description="2D 벡터 시각화 (u, v, proj_u_on_v)")
    parser.add_argument("--show", action="store_true", help="이미지 저장 후 창으로도 표시")
    parser.add_argument("--out", default="outputs/viz01_vectors_2d.png", help="저장 경로")
    args = parser.parse_args()

    import matplotlib

    if not args.show:
        matplotlib.use("Agg")

    import matplotlib.pyplot as plt

    u = [2.0, 1.0]
    v = [1.0, 3.0]
    p = [float(x) for x in projection(u, v)]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color="#aaa", linewidth=1)
    ax.axvline(0, color="#aaa", linewidth=1)
    ax.grid(True, alpha=0.25)

    _arrow(ax, u, color="#d62728", label="u")
    _arrow(ax, v, color="#1f77b4", label="v")
    _arrow(ax, p, color="#2ca02c", label="proj_u_on_v")

    ax.set_aspect("equal", adjustable="box")
    max_len = max(norm(u), norm(v), norm(p))
    lim = max(1.0, max_len * 1.2)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_title(f"u·v={dot(u, v):.3g}, ||u||={norm(u):.3g}, ||v||={norm(v):.3g}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    print(f"saved: {out_path}")

    if args.show:
        plt.show()
    else:
        plt.close(fig)


if __name__ == "__main__":
    main()
