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

def evalTerm(currTerm, typeDict, varList, outcomeSet, startTerm):
    for type in typeDict:
        print(type)
        print("typeDict[type]: " + ', '.join(typeDict[type]))
        print(currTerm)
        if typeDict[type] in currTerm:
            newString = currTerm.replace(typeDict[type], str(type))
            print("newString: " + newString)
            outcomeSet.add(str(startTerm) + newString)
    return outcomeSet

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
    for var in varList:
        if not var in typeDict:
            typeDict = genTermHelper(typeDict, [], var)


def genTermHelper(typeDict, newTermList, var):
    print(typeDict)
    print(var)
    for type in typeDict:
        if var == type[-1]:
            print("type: " + type)
            for newTermVar in list(type[:-1]):
                if not newTermVar in typeDict:
                    print("calling genTermHelper to find " + newTermVar)
                    typeDict = genTermHelper(typeDict, [], newTermVar)
            if len(newTermList) == 0:
                print(typeDict)
                for num in typeDict[type]:
                    print("appending")
                    newTermList.append(num)
                print(newTermList)
            else:
                for string in newTermList:
                    updatedList = []
                    for string in newTermList:
                        print("typeDict[type]: " + typeDict[type])
                        for num in typeDict[type]:
                            newString = string + str(num)
                            updateList.append(newString)
                newTermList = updateList
            if len(type[:-1]) == 0:
                print("base case")
                if len(newTermList) != 0:
                    typeDict[var] = newTermList
                    return typeDict
                return typeDict
    return typeDict




#Execute Main:
if __name__ == '__main__':
    main()
