from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description="3D 벡터 시각화")
    parser.add_argument("--show", action="store_true", help="이미지 저장 후 창으로도 표시")
    parser.add_argument("--out", default="outputs/viz03_vectors_3d.png", help="저장 경로")
    args = parser.parse_args()

    import matplotlib

    if not args.show:
        matplotlib.use("Agg")

    import matplotlib.pyplot as plt

    u = np.array([2.0, 1.0, -1.0])
    v = np.array([1.0, 3.0, 2.0])

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.quiver(0, 0, 0, *u, color="#d62728", linewidth=2)
    ax.quiver(0, 0, 0, *v, color="#1f77b4", linewidth=2)
    ax.text(*u, "  u", color="#d62728")
    ax.text(*v, "  v", color="#1f77b4")

    lim = float(np.max(np.abs(np.vstack([u, v])))) * 1.25
    lim = max(lim, 1.0)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("3D vectors")

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
