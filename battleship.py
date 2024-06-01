abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'Z']
markShip = 'S'
markHit = 'X'
markMissed = 'M'
emptyMark ='0'


val = input("Hi. Nice to meet you. Enter your name: ") 
print("Hi", val, "Lets play!") 

boardSize=input("Please tell me how big board you want to use: ")
boardSize=int(boardSize)
shipNumber=round(boardSize/4+1)


print("Here it is your board!")

board=[]

for i in range(boardSize):
    row=[]
    for j in range(boardSize):
     row.append([emptyMark])

    board.append(row)



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

print(get_display_board(boardSize, board))


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
    placingShips(board)


print('You are ready! Lets play!')
 
