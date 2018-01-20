from app.database import *
from functions import *
import os

def getList():
    AppDatabase = SQLiteDatabase()
    list = AppDatabase.getListOfWords("Francais")
    print(list)
    print("")

    list_keys = ["word", "difficulty", "hint"]
    result = convertSQLtoJSON(list, list_keys)
    print(result)
    return result

print("Current Directory: " + os.curdir)
print("List Dir: ", str(os.listdir(os.curdir)))
print(str(os.path.isfile("database.db")))

# AppDatabase.regenerateDatabase()
# Create basic table for language list
# AppDatabase.createNewTable("tabLanguageList","lgName", "text", "lgTableName", "text", "lgAlphabet", "text")
# AppDatabase.addLanguage("Français","A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z")
