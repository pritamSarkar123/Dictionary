import mysql.connector #import mysql <-leads to error
myconnector=mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
mycursor=myconnector.cursor()

word=input('Input the word: ')

mycursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'"%word)
#mycursor.execute("SELECT Expression FROM Dictionary")
results=mycursor.fetchall()
#keys=[]
# for result in results:
#     print(result[1])
print(results)

