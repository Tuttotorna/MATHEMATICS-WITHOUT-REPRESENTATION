"""
Minimal demo for MATHEMATICS-WITHOUT-REPRESENTATION.

Run:
  python examples/minimal_demo.py
"""

from invariance import invariant_residue


def main():
    samples = [
        "Mathematics is not its encoding.",
        "Bases are encodings. Truth is invariant residue.",
        "12345 12345",
        "A b A  b",
    ]

    for i, x in enumerate(samples, 1):
        r = invariant_residue(x)
        print(f"\n--- Sample {i} ---")
        print("Input:", r["input"])
        print("Transforms:", r["n_transforms"])
        print("Residue size:", r["residue_size"])
        if r["residue_size"] == 0:
            print("Residue: (none in this toy setup)")
        else:
            print("Residue:", r["residue"])


if __name__ == "__main__":
    main()