puzzle=[
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
    ]
import sys
count=0
def solver(nameOfArray):
    """if(isLegal(nameOfArray)==False):
        return"""
    if (isLegal(nameOfArray)==True and hasNoZeros(nameOfArray)==False):
        for list in possibleLists(nameOfArray):
            solver(list)
    elif (isLegal(nameOfArray)==True and hasNoZeros(nameOfArray)==True):
        for listName in nameOfArray:
            print(listName)
        print(count)
        sys.exit()
def hasNoZeros(name):
    for index1 in range(0,9):
        for index2 in range(0,9):
            if(name[index1][index2]==0):
                return False
    return True
def possibleLists(name):
    global count
    possibilities=[]
    for index in range(0,9):
        for secondIndex in range(0,9):
            if (name[index][secondIndex]==0):
                for x in range(1,10,1):
                    f=[]
                    for list in name:
                       g=list.copy()
                       f.append(g)
                    f[index][secondIndex]=x
                    count+=1
                    possibilities.append(f)
                return possibilities
    return None
def isLegal(puzzleName):
    #check rows and makes sure values are legal
    for index in range(0,9):
        listOfNums=[]
        for num in puzzleName[index]:
            if(num>9 or num<0):
                return False
            if(num!=0 and num in listOfNums):
                return False
            if(num!=0 and num not in listOfNums):
                listOfNums.append(num)
    #check the columns
    for index in range(0,9):   
        listOfNums=[]
        for num in range(0,9):
            if(puzzleName[num][index]!=0 and puzzleName[num][index] in listOfNums):
                return False
            if(puzzleName[num][index]!=0 and puzzleName[num][index] not in listOfNums):
                listOfNums.append(puzzleName[num][index])
    #check boxes to make sure values are legal
    listOfNums=[]
    for index in range(0,3):
        for num in range(0,3):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(0,3):
        for num in range(3,6):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(0,3):
        for num in range(6,9):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(3,6):
        for num in range(0,3):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(3,6):
        for num in range(3,6):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(3,6):
        for num in range(6,9):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(6,9):
        for num in range(0,3):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(6,9):
        for num in range(3,6):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num])
    listOfNums=[]
    for index in range(6,9):
        for num in range(6,9):
            if(puzzleName[index][num]!=0 and puzzleName[index][num] in listOfNums):
                return False
            if(puzzleName[index][num]!=0 and puzzleName[index][num] not in listOfNums):
                listOfNums.append(puzzleName[index][num]) 
    return True

#call the solver    
print(solver(puzzle))
