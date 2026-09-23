import hashlib


class Block:

    def __init__(self, transaction, previous_hash):
        self.transaction = transaction
        self.previous_hash = previous_hash

        data = transaction + previous_hash

        self.hash = hashlib.sha256(data.encode()).hexdigest()


# Block 1
block1 = Block("Ali -> Umar : Rs. 500", "00000")


# Block 2
block2 = Block("Umar -> Ahmed : Rs. 200", block1.hash)

# Block 3 
block3 = Block("Ahmed -> Ali : Rs. 100", block2.hash)

print("BLOCK 1")
print("Transaction:", block1.transaction)
print("Previous Hash:", block1.previous_hash)
print("Hash:", block1.hash)

print("\nBLOCK 2")
print("Transaction:", block2.transaction)
print("Previous Hash:", block2.previous_hash)
print("Hash:", block2.hash)

print("\nBLOCK 3")
print("Transaction:", block3.transaction)
print("Previous Hash:", block3.previous_hash)
print("Hash:", block3.hash)