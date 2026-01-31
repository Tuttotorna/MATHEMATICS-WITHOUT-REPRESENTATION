"""
Omega-like residue demo for MATHEMATICS-WITHOUT-REPRESENTATION.

Run:
  python examples/omega_demo.py
"""

from omega_residue import omega_residue


def main():
    samples = [
        "Mathematics is not its encoding.",
        "AAAAA AAAAA AAAAA",               # high redundancy
        "abcdefghijklmnopqrstuvwxyz",       # low redundancy
        "12345 12345 12345 12345",          # repeated pattern
        "random-ish: 9f3a1c7e2b0d",          # mixed
    ]

    for i, x in enumerate(samples, 1):
        r = omega_residue(x)

        print(f"\n--- Sample {i} ---")
        print("Input:", r["input"])
        print("Transforms:", r["n_transforms"])
        print("Mean size:", r["mean_size"])
        print("Variance:", r["variance"])
        print("Omega score:", r["omega_score"])
        print("Compression sizes:", r["compression_sizes"])


if __name__ == "__main__":
    main()