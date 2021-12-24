import random
global r1
global r2
global r3
global r4

global R1
global R2
global R3
global R4


# making a class in order to handke the different rows and related data. will help with the 
class row():
    def __init__(self) -> None:
        self.rowList= [0,0,0,0]
        self.c = [True, True ,True , True]
        self.empty = 4
    
    def __str__(self) -> str:
        return "[ {} , {} , {} , {} ]".format(self.rowList[0], self.rowList[1], self.rowList[2], self.rowList[3])

    def emptySpaceList(self,k):
        self.splst = []
        for i in range(0,4) :
            if self.rowList[i] == 0:
                self.splst.append(4*k + i)
                self.c[i] = True
            else:
                self.c[i]= False
        self.empty = len(self.splst)
        return self.splst


#defining the printing function
def printBoard():
    print ("\n{}\n{}\n{}\n{}\n".format(r1.rowList,r2.rowList,r3.rowList,r4.rowList))

#defining a function to generate 2 at random places in the board
def generateNum():
    lst = []
    lst.extend(r1.emptySpaceList(0))
    lst.extend(r2.emptySpaceList(1))
    lst.extend(r3.emptySpaceList(2))
    lst.extend(r4.emptySpaceList(3))
    
    if len(lst) == 0:
        return False

    choice = random.choice(lst)

    if choice >= 0 and choice <=3 : 
        r1.rowList[choice%4] = 2
         
    elif choice >= 4 and choice <=7 :
        r2.rowList[choice%4] = 2
         
    elif choice >= 8 and choice <=11:
        r3.rowList[choice%4] = 2

    else :
        r4.rowList[choice%4] = 2
         
    return True

def moveChoice():

    print("\nEnter the value W,A,S,D to move all tiles up, left, down, right respectively")
    while True:
        move_choice = input("Enter your choice : ").upper()

        if move_choice == 'W' or move_choice == 'A' or move_choice == 'S' or move_choice == 'D':
            print("Input recieved is : {}\n".format(move_choice))
            break
            # while True:
            #     try:
            #         a = int(input(
            #             "Do you wish to continue with the selected move?\n1 for yes, 0 for no:  ")) % 2
            #     except:
            #         print("please enter a number only.")
            #     else:
            #         print("choice recieved!")
            #         break
            # if a == 1:
            #     break
            # else:
            #     print("changing the move.")
        else:
            print("please provide proper input. Only w,a,s,d allowed")

    return move_choice

def instructions():
    print("\n\nWelcome to 2048, a number game.")
    printBoard()
    print("As you can see, this is how the board looks like.")
    print("the number 2 is generated each time an iteration occurs.\nIt occurs randomly at one of the empty tiles.")
    print("You will have to move all the tiles using\n\nW for up,\nA for left\nD for right and\nS for down\n\n")
    print("when two equal number will be clubbed next to each other, they will be added and \nthe result will be displayed according to the move provided by you")
    
#defining different functions to handle the upwards and sideways movements

def moveUp():

    
    R1.rowList[0]= r1.rowList[0] 
    R1.rowList[1]= r2.rowList[0]
    R1.rowList[2]= r3.rowList[0]
    R1.rowList[3]= r4.rowList[0]
    R2.rowList[0]= r1.rowList[1] 
    R2.rowList[1]= r2.rowList[1]
    R2.rowList[2]= r3.rowList[1]
    R2.rowList[3]= r4.rowList[1]
    R3.rowList[0]= r1.rowList[2] 
    R3.rowList[1]= r2.rowList[2]
    R3.rowList[2]= r3.rowList[2]
    R3.rowList[3]= r4.rowList[2]
    R4.rowList[0]= r1.rowList[3] 
    R4.rowList[1]= r2.rowList[3]
    R4.rowList[2]= r3.rowList[3]
    R4.rowList[3]= r4.rowList[3]

    random_var = R1.emptySpaceList(0)
    random_var = R2.emptySpaceList(1)
    random_var = R3.emptySpaceList(2)
    random_var = R4.emptySpaceList(3)

    random.shuffle(random_var)

#this is move up func

    for i in range(0, R1.empty):
        R1.rowList.append(R1.rowList.pop(R1.rowList.index(0)))
    for i in range(0, R2.empty):
         R2.rowList.append( R2.rowList.pop( R2.rowList.index(0)))
    for i in range(0, R3.empty):
         R3.rowList.append( R3.rowList.pop( R3.rowList.index(0)))
    for i in range(0, R4.empty):
         R4.rowList.append( R4.rowList.pop( R4.rowList.index(0)))

        
    for i in range(0,3):
        if R1.rowList[i] == 0:
            break
        elif R1.rowList[i] == R1.rowList[i+1]:
            R1.rowList[i] *= 2
            R1.rowList[i+1] = 0
            R1.empty += 1
            R1.rowList.append(R1.rowList.pop(R1.rowList.index(0)))

    for i in range(0, 3):
        if R2.rowList[i] == 0:
            break
        elif R2.rowList[i] == R2.rowList[i+1]:
            R2.rowList[i] *= 2
            R2.rowList[i+1] = 0
            R2.empty += 1
            R2.rowList.append(R2.rowList.pop(R2.rowList.index(0)))

    for i in range(0, 3):
        if R3.rowList[i] == 0:
            break
        elif R3.rowList[i] == R3.rowList[i+1]:
            R3.rowList[i] *= 2
            R3.rowList[i+1] = 0
            R3.empty += 1
            R3.rowList.append(R3.rowList.pop(R3.rowList.index(0)))
    
    for i in range(0, 3):
        if R4.rowList[i] == 0:
            break
        elif R4.rowList[i] == R4.rowList[i+1]:
            R4.rowList[i] *= 2
            R4.rowList[i+1] = 0
            R4.empty += 1
            R4.rowList.append(R4.rowList.pop(R4.rowList.index(0)))

    r1.rowList[0] = R1.rowList[0]
    r2.rowList[0] = R1.rowList[1]
    r3.rowList[0] = R1.rowList[2]
    r4.rowList[0] = R1.rowList[3]
    r1.rowList[1] = R2.rowList[0]
    r2.rowList[1] = R2.rowList[1]
    r3.rowList[1] = R2.rowList[2]
    r4.rowList[1] = R2.rowList[3]
    r1.rowList[2] = R3.rowList[0]
    r2.rowList[2] = R3.rowList[1]
    r3.rowList[2] = R3.rowList[2]
    r4.rowList[2] = R3.rowList[3]
    r1.rowList[3] = R4.rowList[0]
    r2.rowList[3] = R4.rowList[1]
    r3.rowList[3] = R4.rowList[2]
    r4.rowList[3] = R4.rowList[3]


def moveLeft():

    for i in range(0, r1.empty):
        r1.rowList.append(r1.rowList.pop(r1.rowList.index(0)))
    for i in range(0, r2.empty):
         r2.rowList.append( r2.rowList.pop( r2.rowList.index(0)))
    for i in range(0, r3.empty):
         r3.rowList.append( r3.rowList.pop( r3.rowList.index(0)))
    for i in range(0, r4.empty):
         r4.rowList.append( r4.rowList.pop( r4.rowList.index(0)))

        
    for i in range(0,3):
        if r1.rowList[i] == 0:
            break
        elif r1.rowList[i] == r1.rowList[i+1]:
            r1.rowList[i] *= 2
            r1.rowList[i+1] = 0
            r1.empty += 1
            r1.rowList.append(r1.rowList.pop(r1.rowList.index(0)))

    for i in range(0, 3):
        if r2.rowList[i] == 0:
            break
        elif r2.rowList[i] == r2.rowList[i+1]:
            r2.rowList[i] *= 2
            r2.rowList[i+1] = 0
            r2.empty += 1
            r2.rowList.append(r2.rowList.pop(r2.rowList.index(0)))

    for i in range(0, 3):
        if r3.rowList[i] == 0:
            break
        elif r3.rowList[i] == r3.rowList[i+1]:
            r3.rowList[i] *= 2
            r3.rowList[i+1] = 0
            r3.empty += 1
            r3.rowList.append(r3.rowList.pop(r3.rowList.index(0)))
    
    for i in range(0, 3):
        if r4.rowList[i] == 0:
            break
        elif r4.rowList[i] == r4.rowList[i+1]:
            r4.rowList[i] *= 2
            r4.rowList[i+1] = 0
            r4.empty += 1
            r4.rowList.append(r4.rowList.pop(r4.rowList.index(0)))
        



def moveRight():
    
    for i in range(0,r1.empty):
        r1.rowList.insert(0, r1.rowList.pop(r1.rowList.index(0,i)))

    for i in range(0, r2.empty):
        r2.rowList.insert(0, r2.rowList.pop(r2.rowList.index(0,i)))

    for i in range(0, r3.empty):
        r3.rowList.insert(0, r3.rowList.pop(r3.rowList.index(0,i)))

    for i in range(0, r4.empty):
        r4.rowList.insert(0, r4.rowList.pop(r4.rowList.index(0,i)))

    for i in range(3,1,-1):
        if r1.rowList[i] == 0:
            break
        elif r1.rowList[i] == r1.rowList[i-1]:
            r1.rowList[i] *= 2
            r1.rowList[i-1] = 0
            r1.empty += 1
            r1.rowList.insert(0, r1.rowList.pop(r1.rowList.index(0, i-1)))

    for i in range(3, 1, -1):
        if r2.rowList[i] == 0:
            break
        elif r2.rowList[i] == r2.rowList[i-1]:
            r2.rowList[i] *= 2
            r2.rowList[i-1] = 0
            r2.empty += 1
            r2.rowList.insert(0, r2.rowList.pop(r2.rowList.index(0, i-1)))
    
    for i in range(3, 1, -1):
        if r3.rowList[i] == 0:
            break
        elif r3.rowList[i] == r3.rowList[i-1]:
            r3.rowList[i] *= 2
            r3.rowList[i-1] = 0
            r3.empty += 1
            r3.rowList.insert(0, r3.rowList.pop(r3.rowList.index(0, i-1)))

    for i in range(3, 1, -1):
        if r4.rowList[i] == 0:
            break
        elif r4.rowList[i] == r4.rowList[i-1]:
            r4.rowList[i] *= 2
            r4.rowList[i-1] = 0
            r4.empty += 1
            r4.rowList.insert(0, r4.rowList.pop(r4.rowList.index(0, i-1)))
        

def moveDown():
    
    R1.rowList[0] = r1.rowList[0]
    R1.rowList[1] = r2.rowList[0]
    R1.rowList[2] = r3.rowList[0]
    R1.rowList[3] = r4.rowList[0]
    R2.rowList[0] = r1.rowList[1]
    R2.rowList[1] = r2.rowList[1]
    R2.rowList[2] = r3.rowList[1]
    R2.rowList[3] = r4.rowList[1]
    R3.rowList[0] = r1.rowList[2]
    R3.rowList[1] = r2.rowList[2]
    R3.rowList[2] = r3.rowList[2]
    R3.rowList[3] = r4.rowList[2]
    R4.rowList[0] = r1.rowList[3]
    R4.rowList[1] = r2.rowList[3]
    R4.rowList[2] = r3.rowList[3]
    R4.rowList[3] = r4.rowList[3]

    random_var = R1.emptySpaceList(0)
    random_var = R2.emptySpaceList(1)
    random_var = R3.emptySpaceList(2)
    random_var = R4.emptySpaceList(3)

    random.shuffle(random_var)


#this is the move down function
    for i in range(0, R1.empty):
        R1.rowList.insert(0, R1.rowList.pop(R1.rowList.index(0, i)))

    for i in range(0, R2.empty):
        R2.rowList.insert(0, R2.rowList.pop(R2.rowList.index(0,i)))

    for i in range(0, R3.empty):
        R3.rowList.insert(0, R3.rowList.pop(R3.rowList.index(0,i)))

    for i in range(0, R4.empty):
        R4.rowList.insert(0, R4.rowList.pop(R4.rowList.index(0,i)))

    for i in range(3,1,-1):
        if R1.rowList[i] == 0:
            break
        elif R1.rowList[i] == R1.rowList[i-1]:
            R1.rowList[i] *= 2
            R1.rowList[i-1] = 0
            R1.empty += 1
            R1.rowList.insert(0, R1.rowList.pop(R1.rowList.index(0, i-1)))

    for i in range(3, 1, -1):
        if R2.rowList[i] == 0:
            break
        elif R2.rowList[i] == R2.rowList[i-1]:
            R2.rowList[i] *= 2
            R2.rowList[i-1] = 0
            R2.empty += 1
            R2.rowList.insert(0, R2.rowList.pop(R2.rowList.index(0, i-1)))
    
    for i in range(3, 1, -1):
        if R3.rowList[i] == 0:
            break
        elif R3.rowList[i] == R3.rowList[i-1]:
            R3.rowList[i] *= 2
            R3.rowList[i-1] = 0
            R3.empty += 1
            R3.rowList.insert(0, R3.rowList.pop(R3.rowList.index(0, i-1)))

    for i in range(3, 1, -1):
        if R4.rowList[i] == 0:
            break
        elif R4.rowList[i] == R4.rowList[i-1]:
            R4.rowList[i] *= 2
            R4.rowList[i-1] = 0
            R4.empty += 1
            R4.rowList.insert(0, R4.rowList.pop(R4.rowList.index(0, i-1)))

    r1.rowList[0] = R1.rowList[0]
    r2.rowList[0] = R1.rowList[1]
    r3.rowList[0] = R1.rowList[2]
    r4.rowList[0] = R1.rowList[3]
    r1.rowList[1] = R2.rowList[0]
    r2.rowList[1] = R2.rowList[1]
    r3.rowList[1] = R2.rowList[2]
    r4.rowList[1] = R2.rowList[3]
    r1.rowList[2] = R3.rowList[0]
    r2.rowList[2] = R3.rowList[1]
    r3.rowList[2] = R3.rowList[2]
    r4.rowList[2] = R3.rowList[3]
    r1.rowList[3] = R4.rowList[0]
    r2.rowList[3] = R4.rowList[1]
    r3.rowList[3] = R4.rowList[2]
    r4.rowList[3] = R4.rowList[3]


# the primary code begins here

r1 = row()
r2 = row()
r3 = row()
r4 = row()
R1 = row()
R2 = row()
R3 = row()
R4 = row()

gameOn = True
b = True


while gameOn:

    if b:
        instructions()
        b = False
    else:
        print("\n"*100)

    gameOn = generateNum()
    printBoard()

    move_choice = moveChoice()

    random_variable = r1.emptySpaceList(0)
    random_variable = r2.emptySpaceList(1)
    random_variable = r3.emptySpaceList(2)
    random_variable = r4.emptySpaceList(3)

    if move_choice == 'W':
        moveUp()

    elif move_choice == 'A':
        moveLeft()

    elif move_choice == 'S':
        moveDown()
    
    elif move_choice == 'D':
        moveRight()
    

            



