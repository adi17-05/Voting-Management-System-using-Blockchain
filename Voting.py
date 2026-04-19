import hashlib
import time

# -------------------- ENTITIES --------------------

class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False


class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name


# -------------------- BLOCKCHAIN --------------------

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, prev_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print("\n------------------------")
            print(f"Index: {block.index}")
            print(f"Time: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Prev Hash: {block.previous_hash}")


# -------------------- SYSTEM --------------------

voters = {}
candidates = {}
blockchain = Blockchain()

# -------------------- MENU FUNCTIONS --------------------

def add_candidate():
    cid = input("Enter Candidate ID: ")
    if cid in candidates:
        print("❌ Candidate already exists")
        return

    name = input("Enter Candidate Name: ")
    candidates[cid] = Candidate(cid, name)
    print("✅ Candidate added")


def add_voter():
    vid = input("Enter Voter ID: ")
    if vid in voters:
        print("❌ Voter already exists")
        return

    name = input("Enter Voter Name: ")
    voters[vid] = Voter(vid, name)
    print("✅ Voter added")


def cast_vote():
    vid = input("Enter Voter ID: ")
    if vid not in voters:
        print("❌ Voter not found")
        return

    voter = voters[vid]

    if voter.has_voted:
        print("❌ Voter has already voted")
        return

    cid = input("Enter Candidate ID: ")
    if cid not in candidates:
        print("❌ Candidate not found")
        return

    vote_data = f"{voter.name} voted for {candidates[cid].name}"
    blockchain.add_block(vote_data)

    voter.has_voted = True
    print("✅ Vote cast successfully")


def print_blockchain():
    blockchain.print_chain()


def validate_chain():
    if blockchain.is_valid():
        print("✅ Blockchain is valid")
    else:
        print("❌ Blockchain is NOT valid")


# -------------------- MENU LOOP --------------------

def menu():
    while True:
        print("\n===== Voting Blockchain System =====")
        print("1. Add Candidate")
        print("2. Add Voter")
        print("3. Cast Vote")
        print("4. Print Blockchain")
        print("5. Validate Chain")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            add_voter()
        elif choice == "3":
            cast_vote()
        elif choice == "4":
            print_blockchain()
        elif choice == "5":
            validate_chain()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice")


# -------------------- RUN --------------------
menu()