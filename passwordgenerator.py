import random
import time 


def Passwordgenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    length_of_password = int(input("How long would you like password"))
    length_of_numbers = int(input("how many numbers in it"))
    length_of_symbols = int(input("how many symbols in it"))
    length_of_letters = int(input("how many numbers in it"))
    if length_of_password == (length_of_symbols + length_of_numbers + length_of_letters):
        print("Randomizing")
        time.sleep(1)
        x = 0
        y = 0
        z = 0
        a = 0
        password = []
        letterslist = []
        numberslist = []
        symbolslist = []
        while x < length_of_password:
            x += 1

            while y < length_of_letters:
                letterpick = letters[random.randint(0,len(letters)-1)]
                letterslist.append(letterpick)
                y += 1
                
            while z < length_of_numbers:
                numberpick = numbers[random.randint(0,len(numbers)-1)]
                numberslist.append(numberpick)
                z += 1 
                
            while a < length_of_symbols:
                symbolpick = symbols[random.randint(0,len(symbols)-1)]
                symbolslist.append(symbolpick)
                a += 1
                

        listoflists = [letterslist,numberslist,symbolslist]
        for list in listoflists:
            for i in list:
                password.append(i) 

        random.shuffle(password)
        print(*password, sep="")
    else:
       print("number of letters, symbols and numbers must equal length of passcode")



        

Passwordgenerator()


