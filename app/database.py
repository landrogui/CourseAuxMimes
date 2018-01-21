import sqlite3
import os
from functions import *

class SQLiteDatabase:

    global dbPath
    dbPath = "database.db"

    def __init__(self):
        global dummyvar

    def connectDatabase(self):
        global conn, curs
        conn = sqlite3.connect(dbPath)
        curs = conn.cursor()

    def disconnectionDatabase(self):
        conn.close()

    def regenerateDatabase(self):
        if os.path.isfile(dbPath):
            if "conn" in globals():
                self.disconnectionDatabase()
            self.deleteDatabaseFile()
        self.createDatabaseFile()
        self.connectDatabase()

    def deleteDatabaseFile(self):
        os.remove(dbPath)

    def createDatabaseFile(self):
        print(os.curdir)
        file = os.open(dbPath, os.O_CREAT)
        os.close(file)

    def executeSQLCommand(self,strType,strCommand):

        print("in executeSQLCommand: " + strType + " " + strCommand)
        self.connectDatabase()

        curs.execute(strCommand)

        if strType == "push":
            conn.commit()
        elif strType == "get":
            result = curs.fetchall()

        return result

        self.disconnectionDatabase()

    def createNewTable(self,strTableName: str, *strFields):

        strListOfFields = ""
        for i in range(len(strFields)):
            if isNumberEven(i):
                strListOfFields = strListOfFields + strFields[i] + " "
            else:
                strListOfFields = strListOfFields + strFields[i] + ","

        # Removing last character
        strListOfFields = strListOfFields[:len(strListOfFields)-1]

        strSQLCommand = "CREATE TABLE " + strTableName + " (" + strListOfFields + ")"

        self.executeSQLCommand("push", strSQLCommand)

    def insertNewRowAllFields(self,strTableName,*values):

        strSQLCommand = "INSERT INTO " + strTableName + " VALUES ("

    def getListOfWords(self,strLanguage):

        # Query database to find the table for that language
        strSQLCommand = "SELECT lgTableName FROM tabLanguageList WHERE lgName = " + "'" + strLanguage + "'"

        result = self.executeSQLCommand("get", strSQLCommand)

        # If only one result is returned, get the list of all the words
        if len(result) == 1:
            result = result[0]
            strTableName = result[0]

            strSQLCommand = "SELECT * from " + strTableName
            result = self.executeSQLCommand("get", strSQLCommand)
            return result
        else:
            return "ERROR: Too many results"

