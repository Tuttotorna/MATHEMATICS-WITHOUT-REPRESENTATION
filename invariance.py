"""
Representation-free invariance (minimal core).

Goal:
Measure what remains stable under arbitrary recodings.

This is not semantics.
This is structural residue.
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
    Compute invariant residue as intersection of fingerprints
    across transformations.

    In this minimal version:
    residue = set of hashes that remain identical.
    """
    outputs = transform_family(x)
    hashes = [fingerprint(o) for o in outputs]

    # Invariant = hashes that appear more than once
    residue = {h for h in hashes if hashes.count(h) > 1}

    return {
        "input": x,
        "n_transforms": len(outputs),
        "hashes": hashes,
        "residue": list(residue),
        "residue_size": len(residue),
    }


if __name__ == "__main__":
    demo = "Mathematics is not its encoding."
    result = invariant_residue(demo)

    print("=== Representation-Free Invariance Demo ===")
    print("Input:", result["input"])
    print("Transforms:", result["n_transforms"])
    print("Residue size:", result["residue_size"])
    print("Residue:", result["residue"])