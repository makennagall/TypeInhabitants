#!/usr/bin/env python3
import sys

def main():
    #Note: Term must be wrapped in quotes, no spaces
    #All types except for the final type must be wrapped in parentheses
    #Final type should only be one term (no arrows)
    #type variables cannot be numbers
    #VX.VY.(T1)->(T2)->FT
#Term Parsing:
    testFileName = sys.argv[1]
    testFile = open(testFileName, "r")
    for line in testFile:
        line = line[:-2]
        line = line[1:]
        #parse term, evaluate term
        print(line)
        typeDict, varList, firstTerm, finalType = parseType(line)
        #print("starting Type: " + firstTerm)
        #print("final type: " + finalType)
        lambdaTerm = makeLambdaTerm(varList, typeDict)
        print(lambdaTerm)
    #Check infinite:
        typeDict = genTerms(typeDict, varList)
        if not finalType in typeDict:
            typeDict[finalType] = ['']
        print(typeDict)
        termIsInfinite = False
        for type in typeDict:
            if checkInfinite(type, typeDict) == True:
                termIsInfinite = True
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
            print("Infinite Term")
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
    for var in term[:-1]:
        if var == termOutcome:
            #check to make sure the term isn't uninhabited:
            for variable in list(term):
                if not variable in typeDict:
                    print("Uninhabited")
                    return 'Uninhabited'
            return True
    else:
        return False
def substitute(typeDict, startTerm, finalList):
    for var in list(startTerm):
        newList = []
        if not var in typeDict:
            returnString = "Uninhabited Term"
            return returnString, False
        for term in finalList:
            for newTerm in typeDict[var]:
                newList.append(str(term) + str(newTerm))
        finalList = newList
    if finalList == []:
        returnString = "Uninhabited Term"
        return returnString, False
    else:
        return finalList, True
def genTerms(typeDict, varList):
    tryAgainList = []
    for var in varList:
        if not var in typeDict:
            newList, newTermMade = genTermsHelper(typeDict, var, tryAgainList)
            if newTermMade == False:
                tryAgainList = newList
            else:
                typeDict[var] = newList
    while tryAgainList != []:
        for var in tryAgainList:
            newList, newTermMade = genTermsHelper(typeDict, var, tryAgainList)
            if newTermMade == False:
                tryAgainList = newList
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
                if len(type[:-1]) > 1:
                    return tryAgainList, False
                else:
                    tryAgainList.append(var)
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
