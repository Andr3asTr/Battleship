#Andreas Triantafyllopoulos, A.M.:4504
def mapa(z):
    x=0
    print('   P1     P2')
    for i in range(0,6):
         for i in range(0,7):
                print(board1[x][i], end='')
         for y in range(0,7):
                if y==6:
                    print(board2[x][y])
                    x+=1
                else:
                    print(board2[x][y], end='')
    
def cpupos(lstcpu):#domh 8eshs cpu
    g=False
    cpux=(chr(randint(97,101))+str(randint(1,5)))  
    while g != True:
            if cpux in lstcpu:
                  cpux=(chr(randint(97,101))+str(randint(1,5)))
            else:
                g=True
    lstcpu.append(cpux)



def playerpos(P, lst):#domh 8eshs paixth
    g = False
    lstapodekta = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']#apodektoi xarakthres
    while g != True :
          if P not in lstapodekta:
                P =( str(input('Invalid position ,or position already taken. Try again: ')))
          elif P in lst:
                P = (str(input('Invalid position ,or position already taken. Try again: ')))
          else:
                g = True
    lst.append(P)  


    
    
def pos_check(pos, lista):#8esh pou rixnei kai lista pou koitaei an exei 3anari3ei
    g = False
    lstapodekta = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']
    while g != True:
        if pos not in lstapodekta:
            pos = (str(input('Invalid position, or missile already thrown there. Try again: ')))
        elif pos in lista:
            pos = (str(input('Invalid position, or missile already thrown there. Try again: ')))
        else:
            lista.append(pos)
            g = True
    print('Missile thrown at ' + pos)
    return pos
               
            



def hit_check(pos, lista, board):#8esh pou rixnei kai lista pou koitaei an petyxe stoxo
     if pos in lista:
        print ('Target hit!')
        cor1=(ord(pos[0])-96)#koitaw to gramma
        cor2=int(pos[1])+1#koitaw to noumero
        board[cor1][cor2]='O'
        mapa(1)
        lista.remove(pos)
     else:
        print ('Target missed!')               
        cor1=(ord(pos[0])-96)#koitaw to gramma
        cor2=int(pos[1])+1#koitaw to noumero
        board[cor1][cor2]='X'               
        mapa(1)

def cpuhit_check_and_pos_check(pos, lista, lst, board):
    x=0
    g = False
    while g != True:
        if pos in lista:#koitaw an exei ri3ei ekei k an exei ri3ei to allazw
            pos=chr(randint(97,101))+str(randint(1,5))
        else:
            lista.append(pos)
            g = True
            x+=1
        if x==1:
            if pos in lst:#koitaw an petyxe tpt
                print('Missile thrown at ' + pos)
                print ('Target hit!')
                cor1=(ord(pos[0])-96)#koitaw to gramma
                cor2=int(pos[1])+1#koitaw to noumero
                board[cor1][cor2]='O'
                mapa(1)
                lst.remove(pos)
            else:
                print('Missile thrown at ' + pos)
                print('Target missed!')
                cor1=(ord(pos[0])-96)#koitaw to gramma
                cor2=int(pos[1])+1#koitaw to noumero
                board[cor1][cor2]='X'
                mapa(1)

def main(first, mode):
    g = False
    if mode==1:
        if first==1:
           while g != True: 
                pos1=input('Player 1 please enter the position to throw your missile: ')
                pos1=pos_check(pos1, p1rix)
                hit_check(pos1, lstcpu, board2)
                if len(lstcpu)==0:
                    g = True
                    print('Game OVER. Player wins')
                else:
                    pos2=chr(randint(97,101))+str(randint(1,5))      
                    cpuhit_check_and_pos_check(pos2, cpurix, lstop, board1)
                    if len(lstop)==0:
                        print('Game OVER. CPU wins')
                        g = True
        elif first==2:
            while g != True:
                pos1=chr(randint(97,101))+str(randint(1,5))
                cpuhit_check_and_pos_check(pos1, cpurix, lstop, board1)
                if len(lstop)==0:
                        print('Game OVER. CPU wins')
                        g = True    
                else:
                    pos2=input('Player 1 please enter the position to throw your missile: ')
                    pos2=pos_check(pos2, p1rix)
                    hit_check(pos2, lstcpu, board2)
                    if len(lstcpu)==0:
                        g = True
                        print('Game OVER. Player wins')

    elif mode==2:
        if first==1:
            while g != True:
                pos1=input('Player 1 please enter the position to throw your missile: ')
                pos1=pos_check(pos1, p1rix)
                hit_check(pos1, lst2, board2)
                if len(lst2)==0:
                    g = True
                    print('Game OVER. Player 1 wins.')
                else:
                    pos2=input('Player 2 please enter the position to throw your missile: ')
                    pos2=pos_check(pos2, p2rix)
                    hit_check(pos2, lst1, board1)
                    if len(lst1)==0:
                        g = True
                        print('Game OVER. Player 2 wins.')
        elif first==2:
            while g != True:
                pos1=input('Player 2 please enter the position to throw your missile: ')
                pos1=pos_check(pos1, p2rix)
                hit_check(pos1, lst1, board1)
                if len(lst1)==0:
                    g = True
                    print('Game OVER. Player 2 wins.')
                else:
                    pos2=input('Player 1 please enter the position to throw your missile: ')
                    pos2=pos_check(pos2, p1rix)
                    hit_check(pos2, lst2, board2)
                    if len(lst2)==0:
                        g = True
                        print('Game OVER. Player 1 wins.')

def gamemode(x):#zhtaw syntetagmenes
     if x == 1:
        #an bei player vs cpu
        P1 = input("Player enter the position of your ship no 1: ")
        playerpos(P1, lstop)
        P2 = input("Player enter the position of your ship no 2: ")
        playerpos(P2, lstop)
        P3 = input("Player enter the position of your ship no 3: ")
        playerpos(P3, lstop)
        P4 = input("Player enter the position of your ship no 4: ")
        playerpos(P4, lstop)
        P5 = input("Player enter the position of your ship no 5: ")
        playerpos(P5, lstop)

        #elegxw ti random petaei o cpu
        cpupos(lstcpu)
        cpupos(lstcpu)
        cpupos(lstcpu)
        cpupos(lstcpu)
        cpupos(lstcpu)

     elif x==2 :     
        #player1
        P6=input("Player 1 enter the position of your ship no 1: ")
        playerpos(P6, lst1)
        P7=input("Player 1 enter the position of your ship no 2: ")
        playerpos(P7, lst1)
        P8=input("Player 1 enter the position of your ship no 3: ")
        playerpos(P8, lst1)
        P9=input("Player 1 enter the position of your ship no 4: ")
        playerpos(P9, lst1)
        P10=input("Player 1 enter the position of your ship no 5: ")
        playerpos(P10, lst1)
        print('\n'*60)

        #player 2
        P11=input("Player 2 enter the position of your ship no 1: ")
        playerpos(P11, lst2)
        P12=input("Player 2 enter the position of your ship no 2: ")
        playerpos(P12, lst2)
        P13=input("Player 2 enter the position of your ship no 3: ")
        playerpos(P13, lst2)
        P14=input("Player 2 enter the position of your ship no 4: ")
        playerpos(P14, lst2)
        P15=input("Player 2 enter the position of your ship no 5: ")
        playerpos(P15, lst2)
        print('\n'*60)

print('BATTLESHIP GAME')
print('The objective is to sink the opponent\'s ships before the opponent sinks yours.')
from random import randint
listaaa=['1','2']
board1=[[' ',' ','1','2','3','4','5'],
       ['a',' ',' ',' ',' ',' ',' '],
       ['b',' ',' ',' ',' ',' ',' '],
       ['c',' ',' ',' ',' ',' ',' '],
       ['d',' ',' ',' ',' ',' ',' '],
       ['e',' ',' ',' ',' ',' ',' ']]

board2=[[' ',' ','1','2','3','4','5'],
        ['a',' ',' ',' ',' ',' ',' '],
        ['b',' ',' ',' ',' ',' ',' '],
        ['c',' ',' ',' ',' ',' ',' '],
        ['d',' ',' ',' ',' ',' ',' '],
        ['e',' ',' ',' ',' ',' ',' ']]
mode=input('Input 1 for 1-player game or 2 for 2-player game: ')
while mode not in listaaa:
        mode=input('Please re-enter the prefered Game-Mode: ')
mode=int(mode)
if mode==1:
    lstop=[] 
    p1rix=[]#edw exw ri3ei
    lstcpu=[] 
    cpurix=[]#k edw
elif mode==2:
    lst1=[] 
    p1rix=[]
    lst2=[] 
    p2rix=[]
gamemode(mode)
first=randint(1,2)
if first == 1 and mode==1:
     print('Player 1 starts first')
     mapa(1)   
     main(1,1)
elif first==1 and mode==2:
     print('Player 1 starts first')
     mapa(1)   
     main(1,2)   
elif first==2 and mode==1:
     print('Player 2 starts first')
     mapa(1)
     main(2,1)
elif first==2 and mode==2:
     print('Player 2 starts first')
     mapa(1)
     main(2,2)     
