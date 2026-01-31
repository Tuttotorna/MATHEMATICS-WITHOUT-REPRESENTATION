"""
Omega-like Residue Estimator (minimal, representation-free).

Goal:
Estimate invariant residual structure under arbitrary recodings,
without relying on symbolic equality.

This is a seed of an operational Omega-set idea:
Residue = what remains compressible/invariant across transforms.

Run:
  python omega_residue.py
"""

import zlib


def transform_family(x):
    """
    Slightly richer recoding family (still minimal).
    Extend with more structural transforms later.
    """
    s = str(x)

    return [
        s,
        s[::-1],
        "".join(sorted(s)),
        s.upper(),
        s.lower(),
        s.replace(" ", ""),
        s.encode("utf-8").hex(),  # encoding shift
    ]


def compressed_size(s: str) -> int:
    """
    Compression proxy: smaller size => more structure.
    """
    data = s.encode("utf-8")
    return len(zlib.compress(data))


def omega_residue(x):
    """
    Omega-like residue score.

    Idea:
    If something is structurally invariant, its compressibility profile
    remains stable under recodings.

    We measure:

    - compression sizes across transforms
    - stability of those sizes
    - residue_score = 1 / (1 + variance)

    Output:
      omega_score ∈ (0,1]
    """
    outputs = transform_family(x)

    sizes = [compressed_size(o) for o in outputs]

    mean = sum(sizes) / len(sizes)
    var = sum((v - mean) ** 2 for v in sizes) / len(sizes)

    omega_score = 1.0 / (1.0 + var)

    return {
        "input": x,
        "n_transforms": len(outputs),
        "compression_sizes": sizes,
        "mean_size": round(mean, 4),
        "variance": round(var, 4),
        "omega_score": round(omega_score, 6),
    }


if __name__ == "__main__":
    demo = "Mathematics is not its encoding."

    r = omega_residue(demo)

    print("=== Omega-like Residue Demo ===")
    print("Input:", r["input"])
    print("Transforms:", r["n_transforms"])
    print("Compression sizes:", r["compression_sizes"])
    print("Mean size:", r["mean_size"])
    print("Variance:", r["variance"])
    print("Omega score:", r["omega_score"])