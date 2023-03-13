import pyfiglet as pyg
import numpy as np

res = pyg.figlet_format("Welcome to Terminal Battleground ")
print(res)

name = input("Enter your name :")
country = input("Enter your name :")
repo = [name]
comm = np.array(["cd", "pwd", "mkdir", "proceed"])
while True:
    a = input(name + "@" + country + ":" + repo[0] + " $")
    if a == "quit":
        exit()
    elif (a == comm).any():
        print("the given command is present")
