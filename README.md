# iQuHACK22 QuTech Quantum Error Correction Challenge

# Project : QEC Bingo Game

## Team
* [Abhay Kamble](https://github.com/abzsd), CS Undergrad @BITS Goa
* [Bernard Wo](https://github.com/bernwo) MSc Applied Physics @ Delft University of Technology,
* [Oskar Słowik](https://github.com/Feigenbaum4669) PhD candidate @ Center for Theoretical Physics PAS,
* Wridhdhisom Karar,
* [Fatma Türkü Tatar](https://github.com/turkutatar), Electrical Engineering Undergraduate @ Cankaya University

## Documentation
* Presentation [Slides](https://docs.google.com/presentation/d/1AlDr8H5LY_8CyQQnUTHNoNZCA1F4KANMGV6-wCRXGGM/edit?usp=sharing)
* Original [Repo](https://github.com/turkutatar/iQuHACK22) - for all files/commits
* Jupyter Notebook in [Repo](https://github.com/turkutatar/iQuHACK22/blob/QEC-Bingo-v2.0/main.ipynb)

### Technologies Used
```QX single-node simulator``` Quantum-Inspire backend

### QEC Preliminaries 
The [[5,1,3]] code is a five qubit quantum error correction code (QECC) which uses 9 qubits in total: 5 physical qubits and 4 ancilla qubits. This code encodes one logical qubit and can correct an arbitrary single qubit error, e.g. X/Y/Z error on any of physical qubits.

### Layout 
The basic layout of the game is a 4x4 grid which contains numbers ranging from 0 to 15, i.e. 0000 to 1111 in binary. Those numbers correspond to all possible error symdromes. In the beginning the grid is randomly generated, and each player has a separate grid.

![ex_grid](https://user-images.githubusercontent.com/73556839/151690729-09667da5-074a-458c-b45c-01ee4809add7.png)

At each turn, a player gives an input, which can be no error (I) or any of the single-qubit Pauli errors (X, Y, Z). The syndrome of a chosen input triggers the cells in the player's respective grid. If the full diagonal or a straight line has been trigerred, that player wins.

### Implementation 
We can implement this code and use quantum-inspire's classical simulator since our idea uses 9 qubits. 

### How to play the game?
Player A gives input i in the form of a string.
Input gets processed and a quantum circuit is constructed with qiskit.
The quantum circuit is then sent to quantum-inspire.
Quantum-inspire returns the syndrome, and Player A and B mark their corresponding cell based on the returned syndrome.
The above steps are repeated between the Player A and B, until one wins.

### What is quantum about this game?
The players are introducing quantum errors whose syndromes are detected by a QEC code running on a quantum computer.

### How to run the code?
Run ```main.py```

### Our team's personal experience on the iQuHACK weekend
Our team is highly diverse in terms of nationalies and education levels. We created a supportive and hard working environment together and everyone did their part as perfect as it can be within 24 hours. We are glad we hacked together:)






