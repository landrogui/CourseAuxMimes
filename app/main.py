from app.database import *
from app.functions import *
import os

def getListWords(strLanguage):
    AppDatabase = SQLiteDatabase()
    list = AppDatabase.getListOfWords(strLanguage)

    list_keys = ["word", "difficulty", "hint"]
    result = convertSQLtoListDict(list, list_keys)
    result = sortListofDict(result, 'word')
    print(result)
    result = json.dumps(result)
    return result

print("Current Directory: " + os.curdir)
print("List Dir: ", str(os.listdir(os.curdir)))
print(str(os.path.isfile("database.db")))

# AppDatabase.regenerateDatabase()
# Create basic table for language list
# AppDatabase.createNewTable("tabLanguageList","lgName", "text", "lgTableName", "text", "lgAlphabet", "text")
# AppDatabase.addLanguage("Français","A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z")
