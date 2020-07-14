import json
from difflib import get_close_matches

class MyDict:
    def __init__(self):
        self.data=json.load(open("data.json"))
        self.searchedFor=[]
    def getSearched(self):
        if len(self.searchedFor)==0:
            return None
        return ', '.join(self.searchedFor)
    def translate(self,word):
        word=word.lower()
        closeMatches=get_close_matches(word,self.data.keys())
        if word in self.data:
            if word not in self.searchedFor:
                self.searchedFor.append(word)
            return '\n'.join(self.data[word])
        elif len(closeMatches) > 0:
            yn=input("Did you mean %s instead? enter Y/N: "%closeMatches[0])
            if yn.lower()=="y" or yn.lower()=="yes":
                if closeMatches[0] not in self.searchedFor:
                    self.searchedFor.append(closeMatches[0])
                return '\n'.join(self.data[closeMatches[0]])
            elif yn.lower()=="n" or yn.lower()=="no":
                return "Wrong word, please do double check!"
            else:
                return "Could not understand the query!"
        else:
            return "Wrong word, please do double check!"

if __name__=="__main__":
    print("Welcome user!")
    mydict=MyDict()
    while True:
        ip=input("1.Search\n2.Return\n   : ")
        if ip=="1":
            word=input("Enter the word: ")
            print(mydict.translate(word))
        elif ip=="2":
            print('Thanks for using our dictionary')
            print(f'You searched for : {mydict.getSearched()}')
            break
        else:
            print("Could not understand input")
            continue
