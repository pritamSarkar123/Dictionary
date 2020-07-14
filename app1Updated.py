import mysql.connector
from difflib import get_close_matches

class MyDict:
    def __init__(self):
        self.searchedFor=[]
        self.myconnector=mysql.connector.connect(
            user = "ardit700_student",
            password = "ardit700_student",
            host = "108.167.140.122",
            database = "ardit700_pm1database"
        )
        self.mycursor=self.myconnector.cursor()
        self.mycursor.execute("SELECT Expression FROM Dictionary")
        dbkeys=self.mycursor.fetchall()
        self.keys=[]
        for result in dbkeys:
            self.keys.append(result[0])
    def getSearched(self):
        if len(self.searchedFor)==0:
            return None
        return ', '.join(self.searchedFor)
    def getMeaning(self,word):
        meanings=[]
        if word not in self.searchedFor:
                self.searchedFor.append(word)
        self.mycursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'"%word)
        results=self.mycursor.fetchall()
        for result in results:
            meanings.append(result[1])
        return '\n'.join(meanings)
    def translate(self,word):
        word=word.lower()
        closeMatches=get_close_matches(word,self.keys)
        if word in self.keys:
            return self.getMeaning(word)
        elif len(closeMatches) > 0:
            yn=input("Did you mean %s instead? enter Y/N: "%closeMatches[0])
            if yn.lower()=="y" or yn.lower()=="yes":
                if closeMatches[0] not in self.searchedFor:
                    self.searchedFor.append(closeMatches[0])
                return self.getMeaning(closeMatches[0]) 
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

            
