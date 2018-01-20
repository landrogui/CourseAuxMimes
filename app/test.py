from app.database import *
from functions import *

AppDatabase = SQLiteDatabase()
list = AppDatabase.getListOfWords("Francais")
print(list)
print("")

list_keys = ["word", "difficulty", "hint"]
result = convertSQLtoJSON(list, list_keys)
print(result)
