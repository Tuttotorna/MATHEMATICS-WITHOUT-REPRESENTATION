"""
Representation-free invariance (minimal core).

Goal:
Measure what remains stable under arbitrary recodings.

This is not semantics.
This is structural residue.

Run:
  python invariance.py
"""

import hashlib


def fingerprint(obj) -> str:
    """
    Stable hash fingerprint of any Python-representable object.
    """
    data = repr(obj).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def transform_family(x):
    """
    Minimal transformation family (toy, extend later).

    These are recodings, not "meaning changes".
    """
    s = str(x)

    return [
        s,                      # identity
        s[::-1],                # reversal
        "".join(sorted(s)),     # permutation (sorted)
        s.upper(),              # alphabetic recode
        s.lower(),
        s.replace(" ", ""),     # whitespace removal
    ]


def invariant_residue(x):
    """
    Compute a toy invariant residue score under recodings.

    We avoid strict hash equality (too brittle).
    We measure consensus on simple structural features:
      - length (after stripping spaces)
      - character multiset (sorted chars, after stripping spaces)

    Output:
      residue_score in [0,1]
      consensus features that survived across transforms
    """
    outputs = transform_family(x)

    feats = []
    for o in outputs:
        s = str(o).replace(" ", "")
        feats.append(
            {
                "len": len(s),
                "bag": "".join(sorted(s)),
            }
        )

    lens = [f["len"] for f in feats]
    bags = [f["bag"] for f in feats]

    len_mode = max(set(lens), key=lens.count)
    bag_mode = max(set(bags), key=bags.count)

    len_consensus = lens.count(len_mode) / len(lens)
    bag_consensus = bags.count(bag_mode) / len(bags)

    # strict multiplicative gate
    residue_score = len_consensus * bag_consensus

    return {
        "input": x,
        "n_transforms": len(outputs),
        "len_mode": len_mode,
        "bag_mode": bag_mode,
        "len_consensus": round(len_consensus, 4),
        "bag_consensus": round(bag_consensus, 4),
        "residue_score": round(residue_score, 4),
    }


if __name__ == "__main__":
    demo = "Mathematics is not its encoding."
    r = invariant_residue(demo)

    print("=== Representation-Free Invariance Demo ===")
    print("Input:", r["input"])
    print("Transforms:", r["n_transforms"])
    print("len_consensus:", r["len_consensus"])
    print("bag_consensus:", r["bag_consensus"])
    print("residue_score:", r["residue_score"])