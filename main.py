import pyfiglet as pyg

res= pyg.figlet_format("Welcome to Terminal Battleground ")
print(res)

name=input("Enter your name :")
country=input("Enter your name :")
repo=[name]
while True:
    a=input(name+"@"+country +":" + repo[0]+" $")
    if(a=="quit"):
        exit()