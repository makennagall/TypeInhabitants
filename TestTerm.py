#!/usr/bin/env python3
import sys

def main():
    #Note: Term must be wrapped in quotes, no spaces
    #All types except for the final type must be wrapped in parentheses
    #Final type should only be one term (no arrows)
    #VX.VY.(T1)->(T2)->FT
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
    typeList = []
    for type in types.split(')')[:-1]:
        type = type.replace("->(", '')
        print("type: " + type)
        typeList.append(type)
    finalType = types.split(')')[-1]
    finalType = finalType.split('>')[1]
    finalType = finalType.replace("->(", '')
    print("final type: " + finalType)
    print(typeList)
    print(varList)



#Execute Main:
if __name__ == '__main__':
    main()
