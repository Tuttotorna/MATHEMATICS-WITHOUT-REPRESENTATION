# MATHEMATICS-WITHOUT-REPRESENTATION

**Representation-Free Residue as an Operational Invariance Metric**

Most mathematics relies on specific encodings:

- digit bases  
- coordinates  
- symbolic alphabets  

This repository explores an alternate operational direction:

> **Truth(X) = what remains invariant across arbitrary recodings.**

Instead of fixing a single representation, we measure the **structural residue**
that survives transformation families.

---

## Core Principle

Given an object **X**, apply representation changes:

- base shifts  
- permutations  
- reversals  
- encoding swaps  
- compression-preserving recodings  

Then define:

- **Residue(X)** = invariant part under these transformations  
- **Truth(X)** = representation-free structural stability  

---

## Minimal Operational Seed

This repo provides two executable toy estimators:

### `residue_score`
A simple consensus measure under basic recodings.

### `omega_score`
An Omega-like compression-stability residue:

- high Ω → stable structure survives recoding  
- low Ω → collapse toward noise / drift  

Compression acts as a practical probe:

> **Structure = what remains compressible and invariant.**

---

## Files

- `invariance.py`  
  Minimal invariance + residue estimators.

- `README.md`  
  Concept, usage, context.

---

## Quick Example

```python
from invariance import residue_score, omega_score

x = "mathematical structure"

print("Residue score:", residue_score(x))
print("Omega score:", omega_score(x))


---

Status

This repository is intentionally minimal:

dependency-free

post-hoc

representation-agnostic

focused only on invariance residue


It is meant as a standalone executable seed, not a full framework.


---

## Larger Context (OMNIA / MB-X.01)

This repository is a minimal standalone seed on representation-free invariance.

A larger structural measurement ecosystem (Ω-residue, saturation limits, stop certificates)
is developed in the main OMNIA project:

Main OMNIA repository:
https://github.com/Tuttotorna/lon-mirror

This repo remains intentionally lightweight and entry-level.

## Author

Massimiliano Brighindi  
MB-X.01 / TruthΩ
