import os
import pandas as pd
import numpy as np

class bcolors: # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

TRIGGERED = "XX"

def isWin(my_array):
    output = False
    for i in range(4):
        if np.all(my_array[:,i]==TRIGGERED):
            output = True
            break
    if not output:
        for i in range(4):
            if np.all(my_array[i,:]==TRIGGERED):
                output = True
                break
    if not output:
        if np.all(np.diag(my_array)==TRIGGERED):
            output = True
    if not output:
        if np.all(np.diag(np.fliplr(my_array))==TRIGGERED):
            output = True
    return output
        

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') or None # function to clear interpreter terminal.
clear()


my_array = np.array([str(i) for i in range(16)])
# print(my_array)
np.random.shuffle(my_array)
my_array = my_array.reshape([4,4])
df = pd.DataFrame(my_array)

while True:
    print(df.to_string(index=False,header=False))
    if isWin(my_array):
        break
    ans = input("\nInsert number: ")
    clear()
    # print(my_array[my_array==ans])
    my_array[my_array==ans] = TRIGGERED
    df = pd.DataFrame(my_array)
print("\n🎉🥳 \033[92mYou won! Congratulations!\033[0m 🎉🥳")
