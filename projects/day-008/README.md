# Day 8 — Caesar Cipher

## What I Built
A Caesar cipher encoder/decoder that shifts letters by a user-defined number. Supports both encryption and decryption, preserves non-alphabet characters (spaces, punctuation), and loops so you can run multiple encodes/decodes in one session.

## Concepts Practiced
- Functions with parameters
- List indexing and modulo wrapping (`%`)
- While loops with a restart prompt
- `.lower()` for case-insensitive input

## How to Run
```bash
python Caesar_Cipher.py
```

## Notes
Decoding is handled by flipping the shift negative (`shift_amount *= -1`) rather than writing a separate decode function — same logic, one function.
