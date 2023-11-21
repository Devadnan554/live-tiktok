from colorama import Fore, Back, Style
def users():
    file = open("users.txt","r")
    y = 1
    for x in file:
        print(Fore.RED+"[ "+str(y) +" ]"+ " "+Fore.BLUE+ x)
        y +=1