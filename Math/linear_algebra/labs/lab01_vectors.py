from __future__ import annotations

import math

from la import dot, norm, projection


def main() -> None:
    u = [2, 1, -1]
    v = [1, 3, 2]

    print("u =", u)
    print("v =", v)
    print("u·v =", dot(u, v))
    print("||u|| =", norm(u))
    print("||v|| =", norm(v))

    cos_theta = dot(u, v) / (norm(u) * norm(v))
    cos_theta = max(-1.0, min(1.0, float(cos_theta)))
    print("angle(u, v) [deg] =", math.degrees(math.acos(cos_theta)))

    print("proj_u_on_v =", projection(u, v))


if __name__ == "__main__":
    main()

