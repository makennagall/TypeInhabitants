#!/usr/bin/env python3
import sys

def main():
#Term Parsing:
    testFileName = sys.argv[1]
    testFile = open(testFileName, "r")
    count = 1
    for line in testFile:
        line = line[:-2]
        line = line[1:]
        #parse term, evaluate term
        print(str(count) + ": " + line)
        count += 1
        typeDict, varList, firstTerm, finalType = parseType(line)
        #print("starting Type: " + firstTerm)
        #print("final type: " + finalType)
        lambdaTerm = makeLambdaTerm(varList, typeDict)
        print("Lambda Term: " + lambdaTerm)
    #Check infinite and Uninhabited:
        typeDict = genTerms(typeDict, varList)
        if not finalType in typeDict:
            typeDict[finalType] = ['']
        termIsInfinite = False
        Uninhabited = False
        if finalType != firstTerm[-1]:
            Uninhabited = True
        for type in typeDict:
            check = checkInfinite(type, typeDict)
            if check == True:
                termIsInfinite = True
            if check == 'Uninhabited':
                Uninhabited = True
        if not Uninhabited:
            if not termIsInfinite:
                finalList, nonZero = substitute(typeDict, firstTerm, [''])
                #guarantee unique values using set:
                if nonZero == True:
                    finalSet = set()
                    for term in finalList:
                        finalSet.add(term)
                    print("Number of inhabitants: ", end='')
                    print(len(finalSet))
                    print("List of inhabitants: ")
                    for term in finalSet:
                        print(term)
                else:
                    print(finalList)
            else:
                print("Infinite Type")
        else:
            print("Uninhabited Type")
        print()
def parseType(testType):
        parenSplit = testType.split("(")
        vars = parenSplit[0]
        types = '('.join(parenSplit[1:])
        varList = []
        for var in vars.split('V'):
            if var != '':
                var = var.replace(".", '')
                varList.append(var)
                #Dictionaries are ordered.
        typeDict = {}
        count = 0
        for type in types.split(')')[:-1]:
            type = type.replace("->(", '')
            type = type.replace("->", '')
            if count == 0:
                firstTerm = type
            if not (type in typeDict):
                typeDict[type] = []
            typeDict[type].append(count)
            count+=1
        finalType = types.split(')')[-1]
        finalType = finalType.split('>')[1]
        finalType = finalType.replace("->(", '')
        #typeDict[finalType] = ['']
        return typeDict, varList, firstTerm, finalType
def checkInfinite(term, typeDict):
    termOutcome = term[-1]
    for var in list(term[:-1]):
        if var == termOutcome:
            #check to make sure the term isn't uninhabited:
            for variable in list(term):
                if typeDict[variable] == ['']:
                    #print("Uninhabited")
                    return 'Uninhabited'
            return True
    else:
        return False
def substitute(typeDict, startTerm, finalList):
    for var in list(startTerm):
        newList = []
        if not var in typeDict:
            returnString = "Uninhabited Type"
            return returnString, False
        for term in finalList:
            for newTerm in typeDict[var]:
                newList.append(str(term) + str(newTerm))
        finalList = newList
    if finalList == []:
        returnString = "Uninhabited Type"
        return returnString, False
    else:
        return finalList, True
def genTerms(typeDict, varList):
    tryAgainList = []
    for var in varList:
        newList, newTermMade = genTermsHelper(typeDict, var, tryAgainList)
        if newTermMade == False:
            tryAgainList = newList
        else:
            if var in typeDict:
                typeDict[var] = typeDict[var] + newList
            else:
                typeDict[var] = newList
    while tryAgainList != []:
        for var in tryAgainList:
            newList, newTermMade = genTermsHelper(typeDict, var, tryAgainList)
            if newTermMade == False:
                tryAgainList = newList
            else:
                if var in typeDict:
                    typeDict[var].append(newList)
                else:
                    typeDict[var] = newList
                tryAgainList.remove(var)
    return typeDict
def genTermsHelper(typeDict, var, tryAgainList):
    newList = []
    for type in typeDict:
        if type[-1] == var:
            if not var in type[:-1]:
                if type[:-1] in typeDict:
                    for num in typeDict[type]:
                        for num2 in typeDict[type[:-1]]:
                            newList.append(str(num) + str(num2))
                    return newList, True
                else:
                    if len(type[:-1]) > 1:
                        return tryAgainList, False
                    elif len(type[:-1]) == 1:
                        if not var in tryAgainList:
                            tryAgainList.append(var)
                        return tryAgainList, False
                    else:
                        return tryAgainList, False
    #make sure it doesn't run infinitely:
    if var in tryAgainList:
        tryAgainList.remove(var)
    return tryAgainList, False

def makeLambdaTerm(varList, typeDict):
    lambdaTerm = ''
    for var in varList:
        lambdaTerm = lambdaTerm + 'V' + var + '.'
    for type in typeDict:
        if typeDict[type] != ['']:
            for num in typeDict[type]:
                lambdaTerm = lambdaTerm + "\\" + str(num) + ":(" + '->'.join(list(type)) + ")."

    return lambdaTerm

#Execute Main:
if __name__ == '__main__':
    main()
