# MATHEMATICS-WITHOUT-REPRESENTATION

Representation-Free Residue as an Operational Invariance Metric.

Most mathematics relies on specific encodings:

- digit bases  
- coordinates  
- symbolic alphabets  

This repository explores an alternate operational direction:

**Truth(X) = what remains invariant across arbitrary recodings.**

---

## Core Principle

Given an object **X**, apply representation changes:

- base shifts  
- permutations  
- reversals  
- compression-preserving recodings  

The **representation-free residue** is what survives these transformations.

---

## Minimal Operational Seed

This repo provides executable toy estimators:

- `residue_score`  
  (consensus under simple recodings)

- `omega_score`  
  (compression-stability residue, Omega-like)

---

## Files

- `invariance.py`  
  Minimal invariance / residue estimators.

- `README.md`  
  Concept + usage.

---

## Quick Example

```python
from invariance import residue_score, omega_score

x = "mathematical structure"

print(residue_score(x))
print(omega_score(x))


---

Status

This is an intentionally minimal research seed:

dependency-free

post-hoc

representation-agnostic

focused only on invariance residue



---

Larger Context (OMNIA / MB-X.01)

This repository is a minimal standalone seed on representation-free invariance.

A larger structural measurement ecosystem (Ω-residue, saturation limits, stop certificates) is developed in the main OMNIA project:

Main OMNIA repository: https://github.com/Tuttotorna/lon-mirror


---

Author: Massimiliano Brighindi
Signature: MB-X.01 / TruthΩ