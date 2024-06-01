import random

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'Z']
markShip = 'S'
markHit = 'X'
markMissed = 'M'
emptyMark ='0'

myCount=1
AICount=0





val = input("Hi. Nice to meet you. Enter your name: ") 
print("Hi", val, "Lets play!") 

boardSize=input("Please tell me how big board you want to use: ")
boardSize=int(boardSize)
shipNumber=round(boardSize/4+1)


print("Here it is your board!")

def makeBoard(boardSize):
 board=[]

 for i in range(boardSize):
    row=[]
    for j in range(boardSize):
     row.append([emptyMark])

    board.append(row)

 return board


myBoard=makeBoard(boardSize)

def get_display_board(size, board):
    rows = '  '
    
    for i in range(size):
        rows += f'{abc[i]} '
    rows += '\n'
    
   

    for i in range(size):
        row_elements = []
        for item in board[i]:
            
                row_elements.extend(item)
           
        rows += f'{i + 1} {" ".join(map(str, row_elements))} \n'
    
    return rows

print(get_display_board(boardSize, myBoard))


def placingShips(board):
    print(f'Hi, you can place {shipNumber} ship!')
    inputP=input("Please give me a place where you want to place your ship: ").upper()
    letter=inputP[0]
    letterIndex=abc.index(letter)
    exactInput=[int(inputP[1])-1, letterIndex]
    board[exactInput[0]][exactInput[1]]=markShip

    print(get_display_board(boardSize, board))
    

    return board


for i in range(shipNumber):
    placingShips(myBoard)


print('You are ready! Lets play!')

def placingShipsAI(board):
    input0=random.randrange(0,boardSize)
    input1=random.randrange(0, boardSize)
    
    if board[input0][input1]==emptyMark:
     board[input0][input1]=markShip

    else:
     input0N=random.randrange(0,boardSize)
     input1N=random.randrange(0, boardSize) 
     board[input0N][input1N]=markShip


    print('AI')
    print(get_display_board(boardSize, AIboard))
    

    return board


AIboard=makeBoard(boardSize)

for i in range(shipNumber):
    placingShipsAI(AIboard)

playingBoard=makeBoard(boardSize)

def guessing(myCount):
    
    
    inputH=input("Please give me a place where you want to hit: ").upper()
    letter=inputH[0]
    letterIndex=abc.index(letter)
    exactInput=[int(inputH[1])-1, letterIndex]
    if AIboard[exactInput[0]][exactInput[1]]==markShip:
       print ('You found a ship')
       AIboard[exactInput[0]][exactInput[1]]=markHit
       playingBoard[exactInput[0]][exactInput[1]]=markHit
       myCount=myCount+1
  


    else:
       print ('You  missed!')
       AIboard[exactInput[0]][exactInput[1]]=markMissed
       playingBoard[exactInput[0]][exactInput[1]]=markMissed


    print(get_display_board(boardSize, playingBoard))
    

    return myCount

def guessingAI():

    input0=random.randrange(0,boardSize)
    input1=random.randrange(0, boardSize)
    
    if AIboard[input0][input1]==markShip:
     myBoard[input0][input1]=markHit

    else: 
     myBoard[input0][input1]=markMissed


    print('Myboard')
    print(get_display_board(boardSize, myBoard))

    
    return myBoard
    



myCountNew=guessing(myCount)

while myCountNew<=shipNumber or AICount<=shipNumber:
   guessing(myCount)
   guessingAI()
   print(myCountNew)
   if myCountNew==2:
      break
  
   
   

print('the game is over')



