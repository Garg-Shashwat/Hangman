import Words
import random

def rndm_word():
    word = []
    num = random.randint(0,len(Words.words_dict)-1)
    word.append(random.choice(Words.words_list[num]))
    word.append(Words.words_dict[num])
    return word
    
i = rndm_word()
print(i)