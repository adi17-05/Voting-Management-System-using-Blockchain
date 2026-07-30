# 🗳️ Voting Management System using Blockchain

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Blockchain](https://img.shields.io/badge/Blockchain-SHA256-success)
![Security](https://img.shields.io/badge/Security-Immutable-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**A secure Blockchain-based Voting Management System that records votes as immutable blocks, ensuring vote integrity, transparency, and protection against tampering.**

</div>

---

# 📑 Table of Contents

- Overview
- Features
- Technology Stack
- Blockchain Architecture
- Workflow
- Project Structure
- Functional Modules
- Installation
- Usage
- Blockchain Validation
- Future Enhancements
- Contributing
- License
- Author

---

# 📄 Overview

The Voting Management System using Blockchain is a secure voting application that leverages blockchain technology to record votes in an immutable ledger. Every vote is stored as a blockchain block linked through cryptographic hashes, ensuring that once a vote is cast, it cannot be modified or deleted.

The system allows administrators to register voters and candidates, enables eligible voters to cast a single vote, and validates the blockchain to detect any tampering.

This project demonstrates the practical application of blockchain concepts such as cryptographic hashing, block chaining, and chain validation in a voting system.

---

# ✨ Features

- 🗳️ Secure blockchain-based voting
- 👤 Voter registration
- 🏆 Candidate registration
- ✅ One vote per voter
- 🔒 SHA-256 cryptographic hashing
- ⛓️ Immutable blockchain ledger
- ✔️ Blockchain integrity validation
- 📋 Complete blockchain visualization
- 💻 Simple command-line interface

---

# 🛠 Technology Stack

## Programming Language

- Python

## Blockchain

- SHA-256 Hashing
- Custom Blockchain Implementation

## Libraries

- hashlib
- time

---

# ⛓️ Blockchain Architecture

```text
Genesis Block
      │
      ▼
Block 1
(Voter A → Candidate X)
      │
      ▼
Block 2
(Voter B → Candidate Y)
      │
      ▼
Block 3
(Voter C → Candidate X)
      │
      ▼
Block N
```

Each block contains:

- Block Index
- Timestamp
- Vote Information
- Previous Block Hash
- Current Block Hash

---

# 🔄 Project Workflow

```text
Start Application
        │
        ▼
Register Candidates
        │
        ▼
Register Voters
        │
        ▼
Cast Vote
        │
        ▼
Verify Voter Eligibility
        │
        ▼
Create Blockchain Block
        │
        ▼
Append Block to Chain
        │
        ▼
Validate Blockchain
```

---

# 📂 Project Structure

```text
Voting-Management-System/

├── Voting.py
├── Voting.ipynb
├── README.md
└── .gitignore
```

---

# ⚙️ Functional Modules

## 👤 Voter Management

- Register new voters
- Prevent duplicate voter registration
- Track voting status
- Ensure one vote per voter

---

## 🏆 Candidate Management

- Register candidates
- Prevent duplicate candidate entries
- Maintain candidate records

---

## 🗳️ Vote Casting

- Verify voter identity
- Verify candidate existence
- Record vote securely
- Prevent multiple voting attempts

---

## ⛓️ Blockchain Management

- Create Genesis Block
- Add new blocks
- Generate SHA-256 hash
- Link blocks securely
- Store vote history

---

## ✔️ Blockchain Validation

The blockchain validation process verifies:

- Current block hash integrity
- Previous hash linkage
- Chain consistency
- Detection of tampered blocks

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/voting-management-blockchain.git

cd voting-management-blockchain
```

---

## Install Python

Ensure Python 3.10 or later is installed.

---

## Run the Project

```bash
python Voting.py
```

---

# 💻 Usage

After launching the application, the following menu appears:

```text
===== Voting Blockchain System =====

1. Add Candidate
2. Add Voter
3. Cast Vote
4. Print Blockchain
5. Validate Chain
6. Exit
```

### Example Workflow

### Step 1

Register candidates.

```text
Candidate ID : C101
Candidate Name : Alice
```

---

### Step 2

Register voters.

```text
Voter ID : V001
Voter Name : John
```

---

### Step 3

Cast vote.

```text
Voter ID : V001

Candidate ID : C101
```

---

### Step 4

Print Blockchain.

Each vote appears as a blockchain block.

```text
Block 1

Index

Timestamp

Vote Data

Hash

Previous Hash
```

---

### Step 5

Validate Blockchain.

Output

```text
Blockchain is Valid
```

---

# 🔐 Security Features

- SHA-256 hashing
- Immutable blockchain ledger
- Previous hash linking
- Blockchain integrity verification
- Duplicate voting prevention
- Duplicate voter prevention
- Duplicate candidate prevention

---

# 📊 Blockchain Validation

The validation algorithm checks:

- Hash recalculation
- Previous hash matching
- Block integrity
- Complete chain consistency

If any block is modified, the blockchain becomes invalid.

---

# 🎯 Applications

- College Elections
- Student Council Elections
- Organization Voting
- Corporate Polling
- Secure Digital Elections
- Blockchain Learning Projects

---

# 🔮 Future Enhancements

- Graphical User Interface (GUI)
- Web-based voting portal
- User authentication
- Digital signatures
- Encrypted voting
- Distributed blockchain network
- Smart contract integration
- Biometric authentication
- Database integration
- Cloud deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Aditya D**

Computer Science Engineer

- 📧 Email: adityadivakar1705@gmail.com

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support helps improve the project and encourages future development.