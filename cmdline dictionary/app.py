import json
from difflib import SequenceMatcher, get_close_matches

dictionaryObj = json.load(open("data.json",'r'))

word = input("enter word: ").lower()


def get_word(word):
    if word in dictionaryObj:
        for w in dictionaryObj[word]:
            print(w)
    elif word.title() in dictionaryObj:
        print(dictionaryObj[word.title()])
    elif word.capitalize() in dictionaryObj:
        print(dictionaryObj[word.upper()])
    else:
        print("The word you typed doesn't exist, please double check your spelling.")
       
    #print(dictionaryObj[word])
  

try:
    get_word(word)
except KeyError:
    try:
        prob= get_close_matches( word , dictionaryObj.keys())[0] 
        correctWord = input("did you mean "+prob+" type y or n: \n").lower()
        if correctWord == "y":
            get_word(prob)
        elif correctWord == "n":
            print("The word you typed doesn't exsist, please try again")
        else:
            newWord = input("What word would you like to look up : \n")
            get_word(newWord)
    except IndexError:
        print("The word you typed doesn't exist, please try a different word")

            
        
        
    
    
