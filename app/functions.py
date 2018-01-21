import json

def isNumberEven(iNumber: int):
    result = divmod(iNumber, 2)

    if result[1] == 0:
        return True
    else:
        return False

def isNumberOdd(iNumber: int):
    result = divmod(iNumber, 2)

    if result[1] != 0:
        return True
    else:
        return False

def convertSQLtoListDict(listSQL, listOfKeys):
    #
    # This function will take a SQL list result, add keys for each column and convert to JSON
    #
    objJSON = []
    dictItems = dict()
    for i_item in listSQL:
        counter_j_items = 0
        for j_item in i_item:
            if str.isdigit(j_item):
                j_item = int(j_item)
            dictItems[listOfKeys[counter_j_items]] = j_item
            counter_j_items += 1

        objJSON.append(dictItems.copy())
        print(objJSON)

    return objJSON

def sortListofDict(list, key):
        # This function will sort a list of dictionnary on a selected key
        return sorted(list, key=lambda y: y.get(key))

def convertSQLtoJSON(listSQL, listOfKeys):
    #
    # This function will take a SQL list result, add keys for each column and convert to JSON
    #
    objJSON = []
    dictItems = dict()
    for i_item in listSQL:
        counter_j_items = 0
        for j_item in i_item:
            if str.isdigit(j_item):
                j_item = int(j_item)
            dictItems[listOfKeys[counter_j_items]] = j_item
            counter_j_items += 1

        objJSON.append(dictItems.copy())
        # print(objJSON)

    return(json.dumps(objJSON))

testlist = [{'key1':'Baleine', 'key2':'4'},{'key1':'Astro', 'key2':'6'}]
print(testlist)
x = testlist[0]
print(sortListofDict(testlist,'key1'))

#print(sorted(testlist,key=lambda y: y.get('key2')))

