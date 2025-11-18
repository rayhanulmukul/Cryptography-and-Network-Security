# CSE-4232 – Cryptography & Network Security Lab

This repository operationalizes the full assignment lifecycle for **CSE-4232 (Cryptography & Network Security Laboratory)**, encapsulating encryption, hashing, primality testing, and secure key-exchange workflows.

All deliverables conform to departmental specification and are structured for rapid execution, grading, and portfolio demonstration.

---

## Repository Structure

```
Cryptography-and-Network-Security/
│
├── 01_Caesar_Cipher/
├── 02_Polygram_Substitution/
├── 03_Transposition_Cipher/
├── 04_Double_Transposition/
├── 05_One_Time_Pad/
├── 06_Lehmann_Primality_Test/
├── 07_Rabin_Miller_Primality_Test/
├── 08_MD5_Implementation/
├── 09_SHA_Implementation/
├── 10_RSA_Encryption_Decryption/
├── 11_Diffie_Hellman_Key_Exchange/
├── 12_PGP_Authentication_Confidentiality.py
│
└── reports/Assignment_Question.pdf
```

---

## Assignment Portfolio

**01 – Caesar Cipher**

* Shift-based monoalphabetic encryption & decryption

**02 – Polygram Substitution Cipher**

* Block size = 3 reversible mapping

**03 – Transposition Cipher**

* Width-driven matrix permutation + reversal

**04 – Double Transposition Cipher**

* Two-stage transposition chain

**05 – One-Time Pad**

* Random non-repeating key stream + reversible recovery

**06 – Lehmann Primality Test**

* Probabilistic primality evaluation

**07 – Rabin–Miller Primality Test**

* Deterministic for low bit-size, probabilistic for large integers

**08 – MD5 Hashing**

* Custom digest computation

**09 – SHA Hashing**

* Secure Hash Algorithm implementation and verification

**10 – RSA Encryption / Decryption**

* Key generation → Ciphertext → Decryption workflow

**11 – Diffie–Hellman Key Exchange**

* Shared secret derivation over public channels

**12 – PGP Authentication + Confidentiality**

* Combined digital signature + encryption pipeline (PGP model)

---

## Technology Stack

Python, C/C++, OpenSSL, GMP, NumPy, Custom Big Integer Logic

---

## Execution Workflow

```
cd 0X_Assignment
python main.py
```

or compile the C/C++ equivalent.

---

## Academic Attribution

CSE-4232 Laboratory
Department of Computer Science & Engineering
University of Rajshahi
