# iQuHACK22

Project : QEC Bingo
QEC Preliminaries -
The [[5,1,3]] code is a five qubit quantum error correction code (QECC) which uses 9 qubits in total, 5 data qubits and 4 ancilla qubits. This code can handle atmost one arbitrary Pauli error on a single qubit, i.e. X/Y/Z error on any one of the qubits.

Layout -
The basic layout of the game is a 4x4 grid which contains numbers ranging from 0 to 15, i.e. 0000 to 1111 in binary. In the beginning the grid is randomly generated, and each player has a separate grid.

At each turn, a player gives an input, which can be any of the Pauli matrices i.e. X or Y or Z or I which in turn triggers the cells in the plaer's respective grid. If the full diagonal or a straight line has been trigerred, that player wins.

Implementation -
We can implement this code and use quantum-inspire's classical simulator since our idea uses 9 qubits. Here the basic idea being -

Player A gives input i in the form of a string.
Input gets processed and a quantum circuit is constructed with qiskit.
The quantum circuit is then sent to quantum-inspire.
Quantum-inspire returns the syndrome, and Player A and B mark their corresponding cell based on the returned syndrome.
The above steps are repeated between the Player A and B, until one wins.
