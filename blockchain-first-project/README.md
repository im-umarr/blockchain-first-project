# Blockchain Project 1 — Mini Blockchain

A simple educational blockchain implementation built with Python 

## Project Overview

This project demonstrates the basic cryptographic and structural concepts behind a blockchain.

The mini-blockchain creates blocks containing transaction data, connects blocks using previous hashes, generates SHA-256 hashes, mines blocks using a nonce, and validates the integrity of the chain.

## Objectives

* Understand the basic structure of a blockchain
* Create blocks with transaction data
* Implement SHA-256 cryptographic hashing
* Link blocks using previous hashes
* Create a Genesis Block
* Implement a simple mining mechanism
* Validate blockchain integrity
* Detect data tampering

## Technologies Used

* Python
* `hashlib`
* SHA-256 Cryptographic Hashing

## Blockchain Structure

Each block contains:

* **Transaction** — Data stored inside the block
* **Previous Hash** — Hash of the previous block
* **Nonce** — Number used during the mining process
* **Hash** — SHA-256 hash generated from the block data

The blocks are connected through their previous hash:

```text
Genesis Block
     ↓
Block 1
     ↓
Block 2
     ↓
Block 3
```

## How Mining Works

The mining function repeatedly changes the nonce until the block hash starts with four zeros:

```text
0000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

This provides a simple Proof-of-Work-style mining mechanism for the educational blockchain.

## Chain Validation

The blockchain checks:

1. Whether the stored hash matches the recalculated hash.
2. Whether the current block's `previous_hash` matches the previous block's hash.
3. Whether mined blocks satisfy the required `0000` hash condition.

If all checks pass:

```text
Blockchain valid: True
```

If the blockchain data is modified:

```text
Blockchain valid: False
```

## Tampering Test

A tampering test was performed by changing the transaction of an existing block after the blockchain was created.

Original transaction:

```text
Ali -> Umar : Rs. 500
```

Changed transaction:

```text
Ali -> Umar : Rs. 5000
```

After the modification, the blockchain validation returned:

```text
Blockchain valid: False
```

This demonstrates how hashing and previous-hash links can be used to detect changes in blockchain data.

## Example Transactions

```text
Ali -> Umar : Rs. 500
Umar -> Ahmed : Rs. 200
Ahmed -> Ali : Rs. 100
```

## Project Outcome

The project successfully demonstrates:

* Block creation
* Cryptographic hashing
* SHA-256
* Genesis Block
* Blockchain linking
* Nonce
* Mining
* Chain validation
* Tampering detection

## Internship

**Program:** Blockchain Technology Internship
**Project:** Project 1 — Building a Mini-Blockchain
**Batch:** 2026

## Author

**Muhammad Umar Abid**
