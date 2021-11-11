#An Unbeatable TicTacToe using the minimax algorithm
#It is a 2-player game where one is the user and the other is the computer
#The game board is a 2D array
#During the computers turn, it call the minimax algorithm to increase its chance of winning
#by checking the possible future states of the game and choosing the most beneficial
import pygame 
import math
import random

#Defining colors used
greyBlack = (23, 23, 23)
background_colour = (234, 212, 252)
white = (255, 255, 255)
red = (194, 24, 7)
green = (119, 198, 110)

xB = 0 
yB = 0
w = 0
h = 0

user_key = ''
comp_key = ''
board = [ ['', '', '' ],
          ['', '', '' ],
          ['', '', '' ] ] 
empty_spaces = 9 

#Method checks the winner after each move
def check_winner(letter, board):
        if(board[0][0] == board[0][1] == board[0][1] == board[0][2]  != ''): 
            return letter
        elif(board[1][0] == board[1][1] == board[1][2] != ''): 
            return letter
        elif(board[2][0] == board[2][1] == board[2][2] != ''): 
            return letter
        elif(board[0][0] == board[1][0] == board[2][0] != ''):
            return letter
        elif(board[0][1] == board[1][1] == board[2][1] != ''): 
            return letter
        elif(board[0][2] == board[1][2] == board[2][2] != ''):
            return letter
        elif(board[0][0] == board[1][1] == board[2][2] != ''): 
            return letter
        elif(board[0][2] == board[1][1] == board[2][0] != ''): 
            return letter
        elif(empty_spaces == 0):
            return "tie"
        else:
            return ''

#Method to draw the final red stroke when someone wins
def draw_line(board, screen, color):
    if(board[0][0] == board[0][1] == board[0][1] == board[0][2]):
        pygame.draw.line(screen, color, (xB + (200 / 3), (yB+ 200/3)), (xB + (1000 / 3), (yB+ 200/3)), 5)
    elif(board[1][0] == board[1][1] == board[1][2]):
        pygame.draw.line(screen, color, (xB + (200 / 3), (yB+ 200)), (xB + (1000 / 3), (yB+ 200)), 5)
    elif(board[2][0] == board[2][1] == board[2][2]):
        pygame.draw.line(screen, color, (xB + (200 / 3), (yB+ 1000/3)), (xB + (1000 / 3), (yB+ 1000/3)), 5)
    elif(board[0][0] == board[1][0] == board[2][0]):
        pygame.draw.line(screen, color, (xB + (200 / 3), (yB+ 200/3)), (xB + (200 / 3), (yB+ 1000/3)), 5)
    elif(board[0][1] == board[1][1] == board[2][1]):
        pygame.draw.line(screen, color, (xB + 200, (yB+ 200/3)), (xB + 200, (yB+ 1000/3)), 5)
    elif(board[0][2] == board[1][2] == board[2][2]):
        pygame.draw.line(screen, color, (xB + (1000 / 3), (yB+ 200/3)), (xB + (1000 / 3), (yB+ 1000/3)), 5)
    elif(board[0][0] == board[1][1] == board[2][2]):
        pygame.draw.line(screen, color, (xB + (200 / 3), (yB+ 200/3)), (xB + (1000 / 3), (yB+ 1000/3)), 5) 
    elif(board[0][2] == board[1][1] == board[2][0]):
        pygame.draw.line(screen, color, (xB + (1000 / 3), (yB+ 200/3)), (xB + (200 / 3), (yB+ 1000/3)), 5)

class Smart_Computer:

    def __init__(self, X_O, screenDim): 
        self.letter = X_O
        self.present = self.letter
        if(self.letter == 'x'):
            self.opposition = 'o'
        else:
            self.opposition = 'x'
        self.screen = screenDim
        self.first_turn = True 

    #The algorithm which makes the computer 'smart'
    def minimax(self, game_board, isMaximizing: bool): 
        global empty_spaces 
        result = check_winner(self.present, game_board) 
        if(result != ''):
            if(result == self.letter):
                return 1*(empty_spaces+1)
            elif(result == self.opposition): 
                return -1*(empty_spaces+1)
            else:
                return 0
        if(isMaximizing):
            best_score = -math.inf
        else:
            best_score = math.inf

        for i in range(0, 3):
            for j in range(0, 3):
                if(game_board[i][j] == ''):
                    if(isMaximizing):
                        self.present = self.letter
                    else:
                        self.present = self.opposition
                    game_board[i][j] = self.present
                    empty_spaces = empty_spaces-1
                    if(isMaximizing): 
                        check_score = self.minimax(game_board, False)
                        if(check_score>best_score):
                            best_score = check_score
                    else:
                        check_score = self.minimax(game_board, True)
                        if(check_score<best_score):
                            best_score = check_score
                    game_board[i][j] = ''
                    empty_spaces = empty_spaces+1  
        return best_score
        
    def best_move(self, game_board):
        self.present = self.letter
        global empty_spaces
        turn = None
        if self.first_turn != True:
            best_score = -math.inf
            for i in range(0, 3):
                for j in range(0, 3):
                    if(game_board[i][j]==''):
                        self.present = self.letter
                        game_board[i][j] = self.present    
                        empty_spaces = empty_spaces-1
                        score = self.minimax(game_board, False) 
                        game_board[i][j] = ''
                        empty_spaces = empty_spaces+1
                        if(score>best_score):
                            best_score = score 
                            turn = [i, j]
            self.present = self.letter 
            game_board[turn[0]][turn[1]] = self.present  #the final best turn after minimax is assigned to computer
        #The first move of the computer is random
        else:
            assigned = False
            while(assigned == False):
                i = random.randrange(0, 3)
                j = random.randrange(0, 3)
                if game_board[i][j] == '':
                    game_board[i][j] = self.present
                    turn = [i, j]
                    assigned = True
            self.first_turn = False
        return turn

class Game_Window:

    def print_board(screen):
        pygame.draw.line(screen, greyBlack, (xB + (400 / 3), yB), (xB + (400 / 3), yB+400), 5)
        pygame.draw.line(screen, greyBlack, (xB + (2*400 / 3), yB), (xB + (2*400 / 3), yB+400), 5)
        pygame.draw.line(screen, greyBlack, (xB, yB+ (400 / 3)), (xB + 400, yB+ (400 / 3)), 5)
        pygame.draw.line(screen, greyBlack, (xB, yB+ (2*400 / 3)), (xB + 400, yB+ (2*400 / 3)), 5)

    #converts user cilck to defined location in the 2D array
    def user_click():
        x, y = pygame.mouse.get_pos()
        if(xB < x < (xB+400/3)):
            column = 0
        elif((xB+400/3) < x < (xB+800/3)):
            column = 1
        elif((xB+800/3) < x < (xB+400)):
            column = 2
        else:
            column = None
        if(yB < y < (yB+400/3)):
            row = 0
        elif((yB+400/3) < y < (yB+800/3)):
            row = 1
        elif((yB+800/3) < y < (yB+400)):
            row = 2
        else:
            row = None
        return row, column 

    def print_winner(self, letter, screen):
        pygame.draw.rect(screen, greyBlack, pygame.Rect(xB, yB+375, 400, 50))
        font_style_win = pygame.font.Font("EvilEmpire.ttf", 24) 
        if(self.user_letter == letter):
            #incase the user wins, so never executed :)
            string = "You Won"
            mesg = font_style_win.render(string, True, green)
            screen.blit(mesg, [xB+50, yB+376])
            return
        elif(letter == 'tie'):
            string = "It's a tie"
        else:
            string = "You Lost"
        mesg = font_style_win.render(string, True, red)
        screen.blit(mesg, [xB+50, yB+376])
        replay_string = "r: Replay"
        mesg_replay = font_style_win.render(replay_string, True, white)
        screen.blit(mesg_replay, [xB+250, yB+376])

    def print_letter(x_point, y_point, screen, letter):
        global board
        font_style_XO = pygame.font.Font("EvilEmpire.ttf", 65) 
        mesg = font_style_XO.render(letter, True, greyBlack)
        screen.blit(mesg, [x_point-15, y_point-25])

    #Depending on its location in 2D board, prints letter on screen
    def find_location(self, row, column, screen, letter):  
        if(row == column == 0):
            x_coord = xB + 200/3
            y_coord = yB + 200/3 
        elif(row == 0 and column == 1):
            x_coord = xB + 200
            y_coord = yB + 200/3
        elif(row == 0 and column == 2):
            x_coord = xB + 1000/3
            y_coord = yB + 200/3
        elif(row == 1 and column == 0):
            x_coord = xB + 200/3
            y_coord = yB + 200
        elif(row == column == 1):
            x_coord = xB + 200
            y_coord = yB + 200
        elif(row == 1 and column == 2):
            x_coord = xB + 1000/3
            y_coord = yB + 200
        elif(row == 2 and column == 0):
            x_coord = xB + 200/3
            y_coord = yB + 1000/3
        elif(row == 2 and column == 1):
            x_coord = xB + 200
            y_coord = yB + 1000/3
        elif(row == column == 2):
            x_coord = xB + 1000/3
            y_coord = yB + 1000/3
        else:
            return
        Game_Window.print_letter(x_coord, y_coord, screen, letter)    #printing user_letter in that block

    def running_game(self, comp: Smart_Computer): 
        end = False
        global board
        winner = ''
        global empty_spaces
        screenDim = self.screen
        global xB, yB 
        pygame.display.set_caption('Tic-Tac-Toe using PyGame') 
        pygame.draw.rect(screenDim, background_colour, pygame.Rect(xB, yB, 400, 400))
        pygame.draw.rect(screenDim, greyBlack, pygame.Rect(xB, yB, 400, 400), 3)
        Game_Window.print_board(screenDim) 

        while(self.running):
            if(self.current_player == comp.letter):
                position = comp.best_move(board) 
                empty_spaces = empty_spaces - 1
                for i in range(0, 3):
                    for j in range(0, 3):
                        if(board[i][j] != ''):
                            self.find_location(i, j, screenDim, board[i][j])
                winner = check_winner(self.current_player, board)
                #If someone wins or is a tie 
                if(winner != ''):
                    draw_line(board, screenDim, red)
                    self.print_winner(winner, screenDim)
                    self.running = False
                self.current_player = self.user_letter

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    end = True
                if event.type == pygame.VIDEORESIZE:
                    screenDim = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    screenDim.fill(greyBlack)
                    w, h = pygame.display.get_surface().get_size() 
                    if w!=400:
                        xB = (w-400)/2
                        yB = (h-400)/2  
                    else:
                        xB = 0
                        yB = 0
                    pygame.draw.rect(screenDim, background_colour, pygame.Rect(xB, yB, 400, 400))
                    pygame.draw.rect(screenDim, greyBlack, pygame.Rect(xB, yB, 400, 400), 3) 
                    Game_Window.print_board(screenDim)
                    for i in range(0, 3):
                        for j in range(0, 3):
                            if(board[i][j] != ''):
                                self.find_location(i, j, screenDim, board[i][j]) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = Game_Window.user_click()
                    if board[row][col]=='':
                        board[row][col] = self.current_player     #that particular block is utilized by the user
                        empty_spaces = empty_spaces - 1 
                        for i in range(0, 3):
                            for j in range(0, 3):
                                if(board[i][j] != ''):
                                    self.find_location(i, j, screenDim, board[i][j]) 
                        winner = check_winner(self.current_player, board)
                        #If someone wins or is a tie
                        if(winner != ''):
                            draw_line(board, screenDim, red)
                            self.print_winner(winner, screenDim)
                            self.running = False
                        self.current_player = comp.letter      #sets current_player as computer  
            pygame.display.update() 

        while(end == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                if event.type == pygame.VIDEORESIZE:
                    screenDim = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    screenDim.fill(greyBlack)
                    w, h = pygame.display.get_surface().get_size()
                    if w!=400:
                        xB = (w-400)/2
                        yB = (h-400)/2  
                    else:
                        xB = 0
                        yB = 0
                    pygame.draw.rect(screenDim, background_colour, pygame.Rect(xB, yB, 400, 400))
                    pygame.draw.rect(screenDim, greyBlack, pygame.Rect(xB, yB, 400, 400), 3) 
                    Game_Window.print_board(screenDim)
                    for i in range(0, 3):
                        for j in range(0, 3):
                            if(board[i][j] != ''):
                                self.find_location(i, j, screenDim, board[i][j])
                    draw_line(board, screenDim, red)
                    self.print_winner(winner, screenDim)
                    pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: 
                        end = True
                        board = [ ['', '', '' ],
                                  ['', '', '' ],
                                  ['', '', '' ] ] 
                        empty_spaces = 9
                        Game_Window(screenDim, user_key) 

    def __init__(self, screen, user_key): 
        if(user_key == 'x'):
            comp: Smart_Computer = Smart_Computer('o', screen)
        else:
            comp: Smart_Computer = Smart_Computer('x', screen)
        self.running = True 
        self.screen = screen
        self.user_letter = user_key 
        self.current_player = user_key     
        self.running_game(comp)


def print_option(screen, color, xB, yB):
    font_style = pygame.font.Font("EvilEmpire.ttf", 35)
    font_style_sub = pygame.font.Font("EvilEmpire.ttf", 25)
    msg = "Choose your letter:"
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [xB+70, yB+150])

    msgX = "Press X: X_Player"
    msgY = "Press O: O_Player"
    mesgX = font_style_sub.render(msgX, True, color)
    mesgY = font_style_sub.render(msgY, True, color)
    screen.blit(mesgX, [xB+115, yB+190])
    screen.blit(mesgY, [xB+115, yB+220])

def user_screen():
    global xB, yB, user_key, comp_key
    running = True
    screenDim = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Tic-Tac-Toe using PyGame') 

    while(running): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screenDim = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                screenDim.fill(greyBlack) 
                w, h = pygame.display.get_surface().get_size() 
                if w!=400:
                     xB = (w-400)/2
                     yB = (h-400)/2  
                else:
                    xB = 0
                    yB = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    user_key = 'x'
                    comp_key = 'o'
                elif event.key == pygame.K_o:
                    user_key = 'o'
                    comp_key = 'x'
                else:
                    break
                Game_Window(screenDim, user_key)
                running = False
                
        if(running == True):
            screenDim.fill(greyBlack)
            print_option(screenDim, white, xB, yB) 
            pygame.display.update()

pygame.init()
user_screen()
pygame.quit()
quit()