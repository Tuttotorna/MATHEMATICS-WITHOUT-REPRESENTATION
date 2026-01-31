# MATHEMATICS-WITHOUT-REPRESENTATION

A minimal research thread on **representation-free structural invariance**.

This repository explores a strict idea:

**Mathematical truth is what remains invariant under arbitrary recodings.**

Bases, digits, tokenizations, coordinates, and symbolic encodings are not fundamental.
They are anthropological interfaces.

The goal is to study mathematics as:

- transformations
- invariants
- residual structure
- representation-independent constraints

This is not philosophy.
This is an operational direction: measure what survives encoding.

---

## Core Principle

Given an object `X`, apply a family of representation changes:

- base change (future)
- permutation
- compression
- re-encoding
- re-tokenization

Then measure the invariant residue:

**Truth(X) = what cannot be removed by recoding.**

---

## Why this exists

Most mathematics is still practiced through human encodings:

- positional notation
- coordinate frames
- fixed symbolic alphabets

This project treats representation as noise.

Only the invariant residue matters.

---

## Minimal Operational Core

The repository provides a first executable toy kernel:

- `transform_family(x)` generates recodings
- `invariant_residue(x)` measures consensus residue

Output:

- `residue_score ∈ [0,1]`

Where:

- `1.0` = fully invariant under the transform family  
- `0.0` = no stable residue detected

This is a seed, not a final metric.

---

## Files

- `invariance.py`  
  Minimal representation-free residue estimator

- `examples/minimal_demo.py`  
  Small batch demo over multiple inputs

---

## Quick Run (10 seconds)

Run:

```bash
python invariance.py
python examples/minimal_demo.py

You will see:

length consensus

character-bag consensus

residue_score



---

Relation to OMNIA (MB-X.01)

This thread is conceptually aligned with:

Ω (Omega-set): invariant residual estimation

OMNIA-LIMIT: certified structural saturation (SNRC)


But this repository is intentionally independent:

no ecosystem dependencies

no prime focus

no narrative layers


Only representation-free invariance as a standalone seed.


---

Status

Frozen seed. Next step (optional): replace toy consensus with a true Omega-like estimator.


---

Author: Massimiliano Brighindi
Signature: MB-X.01 / TruthΩ