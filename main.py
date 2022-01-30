import pandas as pd
import numpy as np
import helper_functions as hf
import quantum_backend as qb


if __name__ == '__main__':
    hf.clear()
    default_valid_inputs = ["I","X0","Y0","Z0","X1","Y1","Z1","X2","Y2","Z2","X3","Y3","Z3","X4","Y4","Z4"]
    backend = qb.get_QI_backend(backend_type="QX single-node simulator")

    my_array = np.array([str(i) for i in range(16)])
    np.random.shuffle(my_array) # mutates the array
    my_array = my_array.reshape([4,4])
    df = pd.DataFrame(my_array)

    while True:
        print(df.to_string(index=False,header=False))
        if hf.isWin(my_array):
            break
        while True: # Get user input.
            input_error = input("\nInsert single-qubit error: ")
            if input_error in default_valid_inputs:
                print("Running circuit on Quantum-Inspire...")
                break
            else:
                print("Please enter valid inputs only.")
        qc_job = qb.execute_QuantumCircuit(input_error,backend=backend,shots=256)
        result_dict = qc_job.result().get_counts()
        ans_bin = max(result_dict, key=result_dict.get)
        ans = str(int(ans_bin, 2))

        hf.clear()

        my_array[my_array==ans] = hf.TRIGGERED
        df = pd.DataFrame(my_array)
    print(f"\n🎉🥳 {hf.OKGREEN}You won! Congratulations!{hf.ENDC} 🎉🥳")

