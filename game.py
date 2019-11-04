#!/usr/bin/env python
# coding: utf-8

# In[2]:


# displaying the board


# In[3]:


def disp(var):
    print(var[7]+' | '+var[8]+' | '+var[9]+'\n')
    print(var[4]+' | '+var[5]+' | '+var[6]+'\n')
    print(var[1]+' | '+var[2]+' | '+var[3]+'\n')


# In[4]:


disp(['#','x','0','x','0','x','0','x','0','x'])


# In[5]:


# defining initial position


# In[6]:


def init():
    pos=input('Welcome to TIC - TAC - TOE \n\nPlayer 1: Do you want to be x or o?')
    while pos !=  'x' and pos != 'o':
            pos=input('\nInvalid Input !!! Please choose x or o')
    else:
        print('\nPlayer 1 chooses '+pos + '\n\nPlayer 1, here you go !!! \n\nthe positions on the board are like:\n')
        disp(['#','1','2','3','4','5','6','7','8','9'])
        return pos


# In[7]:


x=init()


# In[8]:


# defining a function to enter x or o to the board


# In[9]:


def marker(board,pos,tog):
    p=pos
    while board[p] != '-':
        p=int(input('\nthis position is already filled, try another one between 1-9\n'))
    else:
        board[p]=tog
    disp(board)
    return board


# In[10]:


marker(['#','-','-','-','-','-','-','-','-','-'],1,'x')


# In[11]:


#defining a function to take user- input


# In[12]:


def pos(player,marker):
    pos=int(input(player+', on which position do you want to assign '+marker+' ? \n'))
    while pos not in range(1,10):
            pos=input('\nInvalid Input !!! Please choose any number between 1-9')
    else:
        return pos


# In[13]:


x=pos('player1','x')


# In[14]:


x


# In[15]:


#function to check if game is won,tied, lost, or ongoing.


# In[16]:


def check(board):
    if board[1]==board[4]==board[7]!='-':
        return True
    elif board[2]==board[5]==board[8]!='-':
        return True
    elif board[3]==board[6]==board[9]!='-':
        return True
    elif board[1]==board[2]==board[3]!='-':
        return True
    elif board[4]==board[5]==board[6]!='-':
        return True
    elif board[7]==board[8]==board[9]!='-':
        return True
    elif board[1]==board[5]==board[9]!='-':
        return True
    elif board[3]==board[5]==board[7]!='-':
        return True
    else:
        return False


# In[17]:


# to check if game is a tie


# In[18]:


def tie(board):
    return('-' not in board)


# In[19]:


import random
def game():
    play='y'
    while(play=='y'):
        player='player1'
        mkr=init() # mkr takes either x or o
        board=['-' for i in range(0,10)]
        board[0]='#'
        cont =True # cont checks if game has to be contiued or not
        while cont:
            psn = pos(player,mkr) #psn is the position on the grid
            board = marker(board,psn,mkr)
            cont=check(board)
            if cont:
                print(player+' wins !!!!')
                cont=False
            elif tie(board):
                print('game tied !!!!')
                cont=False
            else:
                if mkr=='x':
                    mkr='o'
                else:
                    mkr='x'
                if player == 'player1':
                    player='player2'
                else:
                    player='player1'
                #print(mkr,player)
                cont=True
        else:
            play=input('Do you want to continue, enter y to continue or any other key to stop.')
    else:
        print('thanks for playing this game')


# In[20]:


game()


# In[ ]:




