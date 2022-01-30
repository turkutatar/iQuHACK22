# iQuHACK22 QuTech Quantum Error Correction Challenge

# Project : QEC Bingo Game

## Team
*Abhay Kamble,
*Bernard Wo,
*Oskar Slovik,
*Wridhdhisom Karar,
*Fatma Türkü Tatar, Junior Electrical Engineering Undergraduate, Cankaya University

*Presentation [Slides](https://docs.google.com/presentation/d/1AlDr8H5LY_8CyQQnUTHNoNZCA1F4KANMGV6-wCRXGGM/edit?usp=sharing)
*Original [Repo](https://github.com/turkutatar/iQuHACK22) - for all files/commits

### Technologies Used
QX single-node simulator Quantum-Inspire backend

### QEC Preliminaries 
The [[5,1,3]] code is a five qubit quantum error correction code (QECC) which uses 9 qubits in total, 5 data qubits and 4 ancilla qubits. This code can handle atmost one arbitrary Pauli error on a single qubit, i.e. X/Y/Z error on any one of the qubits.

### Layout 
The basic layout of the game is a 4x4 grid which contains numbers ranging from 0 to 15, i.e. 0000 to 1111 in binary. In the beginning the grid is randomly generated, and each player has a separate grid.

![ex_grid](https://user-images.githubusercontent.com/73556839/151690729-09667da5-074a-458c-b45c-01ee4809add7.png)

At each turn, a player gives an input, which can be any of the Pauli matrices i.e. X or Y or Z or I which in turn triggers the cells in the plaer's respective grid. If the full diagonal or a straight line has been trigerred, that player wins.

### Implementation 
We can implement this code and use quantum-inspire's classical simulator since our idea uses 9 qubits. 

### How to play the game?
Player A gives input i in the form of a string.
Input gets processed and a quantum circuit is constructed with qiskit.
The quantum circuit is then sent to quantum-inspire.
Quantum-inspire returns the syndrome, and Player A and B mark their corresponding cell based on the returned syndrome.
The above steps are repeated between the Player A and B, until one wins.

### What is quantum about this game?
We are mapping probabilistic syndromes which is not possible with regular computers.

### How to run the code?
Run main.py

### Our team's personal experience on the iQuHACK weekend
Our team is highly diverse in terms of nationalies and education levels. We created a supportive and hard working environment together and everyone did their part as perfect as it can be within 24 hours. We are glad we hacked together:)






