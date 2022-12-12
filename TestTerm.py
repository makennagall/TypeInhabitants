#!/usr/bin/env python3
import sys

def main():
    #Note: Term must be wrapped in quotes, no spaces
    #All types except for the final type must be wrapped in parentheses
    #Final type should only be one term (no arrows)
    #type variables cannot be numbers
    #VX.VY.(T1)->(T2)->FT
#Term Parsing:
    testType = sys.argv[1]
    parenSplit = testType.split("(")
    vars = parenSplit[0]
    types = '('.join(parenSplit[1:])
    print(types)
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
    '''
    if list(firstTerm)[-1] == finalType:
        firstTerm = firstTerm[:-1]
    '''
    print("starting Type: " + firstTerm)
    print("final type: " + finalType)
    print(typeDict)
#Check infinite:
    typeDict = genTerms(typeDict, varList)
    print(typeDict)
    for type in typeDict:
        if checkInfinite(type, typeDict) == True:
            sys.exit("Infinite Term")
#Function Call:
    #outcomeSet = set()
    #outcomeSet = evalTerm(firstTerm, typeDict, varList, outcomeSet, 0)
    #print(outcomeSet)
#def varifyTypes(typelist, varList):

def checkInfinite(term, typeDict):
    termOutcome = term[-1]
    print("term outcome: " + termOutcome)
    for var in term[:-1]:
        print(var)
        if var == termOutcome:
            #check to make sure the term isn't uninhabited:
            for variable in list(term):
                print()
                if not variable in typeDict:
                    print("Impossible to make any terms")
                    sys.exit("Uninhabited")
            return True
    else:
        return False

def genTerms(typeDict, varList):
    tryAgainList = []
    for var in varList:
        print(var)
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
            if type[:-1] in typeDict:
                for num in typeDict[type]:
                    for num2 in typeDict[type[:-1]]:
                        newList.append(str(num) + str(num2))
                print(newList)
                return newList, True
            if len(type[:-1]) > 1:
                return tryAgainList, False
            else:
                print("another unknown variable encountered: " + type[:-1])
                tryAgainList.append(var)
                return tryAgainList, False
    return tryAgainList, False

#Execute Main:
if __name__ == '__main__':
    main()
