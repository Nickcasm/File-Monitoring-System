import time
import random
from datetime import datetime as dt

def genRandWord():
    choice = random.choice(["CDS","different"])
    if choice == "different":
        randomWordLength = random.randint(1,9)
        word = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz", randomWordLength))
        return word
    else:
        return choice
while True:    
    with open("file1.txt","a") as file1,open("file2.txt","a") as file2:
        file1.write(genRandWord()+" ")
        file2.write(genRandWord()+" ") 
    time.sleep(5)    