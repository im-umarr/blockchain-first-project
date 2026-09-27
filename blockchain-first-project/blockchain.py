import hashlib


class Block:
    def __init__(self, transaction, previous_hash):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = self.transaction + self.previous_hash + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self):
        while not self.hash.startswith("0000"):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain = []

    def create_genesis_block(self):
        genesis_block = Block("Genesis Block", "00000")
        self.chain.append(genesis_block)

    def add_block(self, transaction):
        previous_block = self.chain[-1]

        new_block = Block(
            transaction,
            previous_block.hash
        )

        new_block.mine_block()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            calculated_hash = hashlib.sha256(
                (
                    current_block.transaction
                    + current_block.previous_hash
                    + str(current_block.nonce)
                ).encode()
            ).hexdigest()

            if current_block.hash != calculated_hash:
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if not current_block.hash.startswith("0000"):
                return False

        return True


# Create Blockchain
blockchain = Blockchain()

# Create Genesis Block
blockchain.create_genesis_block()

# Add Blocks
blockchain.add_block("Ali -> Umar : Rs. 500")
blockchain.add_block("Umar -> Ahmed : Rs. 200")
blockchain.add_block("Ahmed -> Ali : Rs. 100")


# Display Blockchain
for block in blockchain.chain:
    print("Transaction:", block.transaction)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("Nonce:", block.nonce)
    print("--------------------")


# Validate Blockchain
print("Blockchain valid:", blockchain.is_chain_valid())