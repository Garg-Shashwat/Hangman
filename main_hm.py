import Words
import random
import re
from os import system
import sys

def difficulty():
    _ = system('cls')
    while True:
        try:
            difficult = input("Please Select Difficulty:\n1.Easy\n2.Medium\n3.Hard\nE.Exit\n(1/2/3/E):").strip().lower()
            _ = system('cls')
            difficult = int(difficult)
            if difficult == 1:
                tries=12
                break
            elif difficult == 2:
                tries=8
                break
            elif difficult == 3:
                tries=4
                break
            else:
                print("Enter a Valid Difficulty")
        except:
            if difficult == 'e':
                sys.exit("Program terminated: User Interruption")
            print("Invalid input")
    return tries, difficult

def rndm_word(difficult):
    num = random.randint(0,len(Words.words_dict)-1)
    if difficult == 1:
        words = random.choice(Words.easy[num])
    elif difficult == 2:
        words = random.choice(Words.medium[num])
    elif difficult == 3:
        words = random.choice(Words.hard[num])
    index = Words.words_dict[num]
    return words, index

replay = 'y'
while replay == 'y':
    tries, difficult = difficulty()
    word, topic = rndm_word(difficult)
    guessed_letters = []
    solved = False
    test = re.sub('[a-zA-Z]','*', word)
    _ = system('cls')
    while tries > 0:
        print("____________________________________________________")
        print("Topic: " + topic)
        print("Lives:", tries)
        print("____________________________________________________")
        print("Word: "+ test)
        a = input("Enter a character: ").upper()
        _ = system('cls')
        if len(a)==1 and a.isalpha():
            if a in guessed_letters:
                print("You have already guessed this word")
                continue
            elif a in word:
                guessed_letters.append(a)
                to_list = list(test)
                for i in range(len(word)):
                    if a == word[i]:
                        to_list[i] = a
                test = "".join(to_list)
            else:
                tries-=1
                print('Letter not found')
            if '*' not in test:
                solved = True
                break
        elif len(a)==len(word) and a==word:
            solved = True
            break
        else:
            print("Invalid input!")
            continue
    _ = system('cls')
    print('The answer is:',word)
    if solved:
        print("Congrats you won!!!\n:D")
    else:
        print("Sorry you are hanged\n:(")
    replay = input("Want to play again?(Y/N)").strip().lower()
    if replay != '[yYnN]':
        print("Invalid Input")