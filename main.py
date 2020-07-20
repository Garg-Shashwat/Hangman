
import random
import re
from os import system

easy=[["APPLE","BANANA","ORANGE","MANGO","PEAR"],["IT","THE MEG","TROY","NOAH","ZODIAC"],["DARK","NARUTO","FRIENDS","BABIES","LUCIFER","GOTHAM"],["GOD OF WAR","HORIZON","ASSASSIN'S CREED","GTA","COD","PUBG"]]
medium=[["AVACADO","STRAWBERRY"],["THE ITALIAN JOB","THE GOLDEN COMPASS","THE MUMMY"],["THE WITCHER","WARRIOR NUN","INTO THE NIGHT","STRANGER THINGS"],["CALL OF DUTY","GRAND THEFT AUTO"]]
hard=[["POMEGRANATE","JACKFRUIT","DURIAN","FEIJOA"],["CASTLE ROCK","I","AXL","EL CHAPO"],["HEMLOCK GROVE","EL CHEMA"],["PLAYERUNKNOWN BATTLE GROUND"]]
words_dict={
0:"Fruits",
1:"Movies",
2:"Series",
3:"Games"
}

def difficulty():
    while True:
         try:
            difficult = str(input("Please Select Difficulty: Easy, Medium or Hard? ").strip().lower())
            if difficult == "easy":
                tries=12
                break
            elif difficult == "medium":
                tries=8
                break
            elif difficult == "hard":
                tries=4
                break
            else:
                print("Enter a Valid Difficulty")
    return tries

def rndm_word():
    words = []
    num = random.randint(0,len(words_dict)-1)
    if difficult == "easy":
        words.append(random.choice(easy[num]))
    if difficult == "medium":
        words.append(random.choice(medium[num]))
    if difficult == "hard":
        words.append(random.choice(hard[num]))
    words.append(words_dict[num])
    return words

tries = difficulty()
result = rndm_word()
word, topic = result[0], result[1]
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
