import Words
import random
import re

def rndm_word():
    word = []
    num = random.randint(0,len(Words.words_dict)-1)
    word.append(random.choice(Words.words_list[num]))
    word.append(Words.words_dict[num])
    return word
    
result = rndm_word()
word, topic = result[0], result[1]
tries = 6
solved = False
ans = re.sub('[a-z]','*', word)
print(word, topic)
while tries > 0:
    print("____________________________________________________")
    print("Topic: " + topic)
    print("Lives:", tries)
    print("____________________________________________________")
    print("Word: "+ ans)
    a = input("Enter a character: ").lower()
    if len(a)==1 and a.isalpha():
        if a in word:
            to_list = list(ans)
            for i in range(len(word)):
                if a == word[i]:
                    to_list[i] = a
            ans = "".join(to_list)
        else:
            tries-=1
        if '*' not in ans:
            solved = True
            break
    else:
        print("Invalid input!")
        continue
if solved:
    print("Congrats you won!!!\n:D")
else:
    print("Sorry you are hanged\n:(")