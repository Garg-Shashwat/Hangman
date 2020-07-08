import Words
import random
import re
from os import system

def rndm_word():
    words = []
    num = random.randint(0,len(Words.words_dict)-1)
    words.append(random.choice(Words.words_list[num]))
    words.append(Words.words_dict[num])
    return words
    
result = rndm_word()
word, topic = result[0], result[1]
guessed_letters = []
tries = 6
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
        if '*' not in test:
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