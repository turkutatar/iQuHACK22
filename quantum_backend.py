from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer
# import numpy as np

# To-Do keep track of used inputs.
def generate_QuantumCircuit(input_str: str):
    """
    Returns a QuantumCircuit given an input string containing the information about the data qubit error.
    """
    input_str = input_str.upper() # Normalise the input string to always be uppercase.
    valid_inputs = ["I","X0","Y0","Z0","X1","Y1","Z1","X2","Y2","Z2","X3","Y3","Z3","X4","Y4","Z4"]

    assert input_str in valid_inputs, "Please enter a valid input!"

    # Initialising the quantum circuit.
    ancilla_qubits = QuantumRegister(4,name='a')
    data_qubits = QuantumRegister(5,name='d')
    creg = ClassicalRegister(4)
    qc = QuantumCircuit(ancilla_qubits,data_qubits,creg)

    # Encoding the 5 data qubits into 1 logical qubit.
    qc.h(data_qubits)
    # for i in range(5):
    #     qc.cz(data_qubits[i],data_qubits[(i+1)%5])
    qc.cz(data_qubits[0],data_qubits[1])
    qc.cz(data_qubits[2],data_qubits[3])
    qc.cz(data_qubits[1],data_qubits[2])
    qc.cz(data_qubits[3],data_qubits[4])
    qc.cz(data_qubits[0],data_qubits[4])
    qc.barrier()

    if len(input_str) != 1: # elso do nothing. (I.e., the input was "I", which is the identity).
        if input_str[0] == "X":
            qc.x(data_qubits[int(input_str[1])])
        if input_str[0] == "Y":
            qc.y(data_qubits[int(input_str[1])])
        if input_str[0] == "Z":
            qc.z(data_qubits[int(input_str[1])])
        qc.barrier()

    # Stabiliser operations.
    qc.h(ancilla_qubits)
    qc.barrier()
    qc.cx(ancilla_qubits[0],data_qubits[0])
    qc.cz(ancilla_qubits[0],data_qubits[1])
    qc.cz(ancilla_qubits[0],data_qubits[2])
    qc.cx(ancilla_qubits[0],data_qubits[3])
    qc.barrier()
    qc.cx(ancilla_qubits[1],data_qubits[1])
    qc.cz(ancilla_qubits[1],data_qubits[2])
    qc.cz(ancilla_qubits[1],data_qubits[3])
    qc.cx(ancilla_qubits[1],data_qubits[4])
    qc.barrier()
    qc.cx(ancilla_qubits[2],data_qubits[0])
    qc.cx(ancilla_qubits[2],data_qubits[2])
    qc.cz(ancilla_qubits[2],data_qubits[3])
    qc.cz(ancilla_qubits[2],data_qubits[4])
    qc.barrier()
    qc.cz(ancilla_qubits[3],data_qubits[0])
    qc.cx(ancilla_qubits[3],data_qubits[1])
    qc.cx(ancilla_qubits[3],data_qubits[3])
    qc.cz(ancilla_qubits[3],data_qubits[4])
    qc.barrier()
    qc.h(ancilla_qubits)
    qc.barrier()

    # Add the measurements into the circuit
    qc.measure(ancilla_qubits,creg)
    return qc
    
qc = generate_QuantumCircuit("Y4")
qc.draw("mpl")