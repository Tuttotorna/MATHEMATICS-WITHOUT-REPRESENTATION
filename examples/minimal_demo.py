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
        print("len_mode:", r["len_mode"])
        print("bag_mode:", r["bag_mode"])
        print("len_consensus:", r["len_consensus"])
        print("bag_consensus:", r["bag_consensus"])
        print("residue_score:", r["residue_score"])


if __name__ == "__main__":
    main()