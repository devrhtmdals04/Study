from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description="2x2 선형변환 시각화 (그리드/단위원)")
    parser.add_argument("--show", action="store_true", help="이미지 저장 후 창으로도 표시")
    parser.add_argument("--out", default="outputs/viz02_linear_transform_2d.png", help="저장 경로")
    args = parser.parse_args()

    import matplotlib

    if not args.show:
        matplotlib.use("Agg")

    import matplotlib.pyplot as plt

    A = np.array([[2.0, 1.0], [1.0, 1.5]])

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="#aaa", linewidth=1)
    ax.axvline(0, color="#aaa", linewidth=1)
    ax.grid(True, alpha=0.25)

    # unit circle
    t = np.linspace(0, 2 * np.pi, 400)
    circle = np.stack([np.cos(t), np.sin(t)], axis=1)
    circle_T = circle @ A.T
    ax.plot(circle[:, 0], circle[:, 1], color="#999", linewidth=1, label="unit circle")
    ax.plot(circle_T[:, 0], circle_T[:, 1], color="#ff7f0e", linewidth=2, label="A(unit circle)")

    # grid lines
    grid = np.linspace(-2.0, 2.0, 9)
    s = np.linspace(-2.0, 2.0, 200)
    for c in grid:
        line_v = np.stack([s, np.full_like(s, c)], axis=1)
        line_h = np.stack([np.full_like(s, c), s], axis=1)
        ax.plot(line_v[:, 0], line_v[:, 1], color="#bbb", linewidth=0.8, alpha=0.7)
        ax.plot(line_h[:, 0], line_h[:, 1], color="#bbb", linewidth=0.8, alpha=0.7)

        line_v_T = line_v @ A.T
        line_h_T = line_h @ A.T
        ax.plot(line_v_T[:, 0], line_v_T[:, 1], color="#1f77b4", linewidth=1.0, alpha=0.9)
        ax.plot(line_h_T[:, 0], line_h_T[:, 1], color="#1f77b4", linewidth=1.0, alpha=0.9)

    # basis vectors
    e1 = np.array([1.0, 0.0])
    e2 = np.array([0.0, 1.0])
    Ae1 = A @ e1
    Ae2 = A @ e2

    ax.quiver(0, 0, e1[0], e1[1], angles="xy", scale_units="xy", scale=1, color="#333", width=0.006)
    ax.quiver(0, 0, e2[0], e2[1], angles="xy", scale_units="xy", scale=1, color="#333", width=0.006)
    ax.quiver(0, 0, Ae1[0], Ae1[1], angles="xy", scale_units="xy", scale=1, color="#d62728", width=0.006)
    ax.quiver(0, 0, Ae2[0], Ae2[1], angles="xy", scale_units="xy", scale=1, color="#d62728", width=0.006)

    ax.set_title(f"A = [[{A[0,0]:.2g}, {A[0,1]:.2g}], [{A[1,0]:.2g}, {A[1,1]:.2g}]]")
    ax.legend(loc="upper left")

    # limits (include transformed circle)
    pts = np.vstack([circle, circle_T])
    lim = max(3.0, float(np.max(np.abs(pts))) * 1.25)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

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
