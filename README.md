# MATHEMATICS-WITHOUT-REPRESENTATION

A minimal research thread on **representation-free structural invariance**.

This repository is a minimal standalone seed on representation-free invariance.

A larger structural measurement ecosystem (Ω-residue, saturation limits, stop certificates)
is developed in the main OMNIA project:

Main OMNIA repository: https://github.com/Tuttotorna/lon-mirror

This repo remains intentionally lightweight and dependency-free.


This repository explores a strict operational idea:

**Mathematical truth is what remains invariant under arbitrary recodings.**

Bases, digits, tokenizations, coordinates, and symbolic encodings are not fundamental.
They are anthropological interfaces.

The goal is to study mathematics as:

- transformations
- invariants
- residual structure
- representation-independent constraints

No metaphors. Only measurable residue.

---

## Core Principle

Given an object `X`, apply a family of representation changes:

- permutation
- reversal
- encoding shifts
- compression-preserving recodings
- (future) base changes, token shifts

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

## Modules

### 1) Toy Residue Consensus (`invariance.py`)

A first executable kernel:

- generates simple recodings
- measures consensus on structural features

Output:

- `residue_score ∈ [0,1]`

This is a seed, not a final metric.

---

### 2) Omega-like Residue Estimator (`omega_residue.py`)

A more meaningful step:

Residue is measured **without symbolic equality**.

Key idea:

If structure is invariant, its **compressibility profile**
remains stable under recodings.

We compute:

- compression sizes across transforms
- variance of those sizes
- an Omega-like score:

```text
omega_score = 1 / (1 + variance)

Output:

omega_score ∈ (0,1]

higher = more invariant structural residue


This is an operational bridge toward Ω-residue measurement.


---

Files

invariance.py Minimal representation-free residue score (toy)

omega_residue.py Omega-like residue via compression stability

examples/minimal_demo.py Demo for residue_score

examples/omega_demo.py Demo for omega_score



---

Quick Run (10 seconds)

Run:

python invariance.py
python examples/minimal_demo.py

python omega_residue.py
python examples/omega_demo.py

You will see:

consensus residue scores

compression-based Omega-like residue scores



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

Operational seed complete.

Next steps (optional):

richer transform families

true superposition residue estimators

formal stop/saturation certificates

---

## Larger Context (OMNIA / MB-X.01)


---

Author: Massimiliano Brighindi
Signature: MB-X.01 / TruthΩ

