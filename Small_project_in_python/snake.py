import pygame
import time
import random
import sys

#initialising pygame 
pygame.init()

clock = pygame.time.Clock()
pygame.font.init()

#declaration of the colors that i'll be using in game
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
pink = 	(255,20,147)

#declaring the pygame window
width = 700
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
# sysfont = pygame.font.get_default_font()
score_font = pygame.font.SysFont("comicsansms",35)

#defining the speed of the snake
snake_speed = 12

#displaying the snake everytime after eating the food
def snake_position(snake_list,snake):
    for i in snake_list:
        pygame.draw.rect(screen,white,(i[0],i[1],snake,snake))

#function for displaying your score at the end of the game
def your_score(score):
    val = score_font.render("Your Score :" + str(score), True,green)
    screen.blit(val,(width//3,height//2))

#displaying different messages on the screen  
def message(msg):
    mess = score_font.render(msg,True,blue)
    screen.blit(mess,(width//6,height//4))

def snakegame():
    snake = 10
    snake_list = []
    snake_x = width//2
    snake_y = height//2
    snake_x_change = 0
    snake_y_change = 0
    snake_length = 1
    left_right = 0
    up_down = 0

    #defining the position of the very first food
    x_food = random.randint(10,width-10)
    y_food = random.randint(10,height-10)
    game_loop = True
    game_end = True
    while game_loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
                # sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if up_down == 0:
                        snake_x_change = 0
                        snake_y_change = -snake
                        up_down = 1
                        left_right = 0
                if event.key == pygame.K_DOWN:
                    if up_down == 0:
                        snake_x_change = 0
                        snake_y_change = +snake
                        up_down = 1       
                        left_right = 0
                if event.key == pygame.K_LEFT:
                    if left_right == 0:
                        snake_y_change = 0
                        snake_x_change = -snake
                        up_down = 0
                        left_right = 1
                if event.key == pygame.K_RIGHT:
                    if left_right == 0:
                        snake_y_change = 0
                        snake_x_change = +snake
                        up_down = 0
                        left_right = 1
        if snake_x >= width-10 or snake_x < 10 or snake_y >= height-10 or snake_y < 10:
            game_end = False
        screen.fill(black)
        while game_end == False:
            screen.fill(pink)
         
            your_score(snake_length-1)
            message("Press c to continue otherwise q")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(pink)
                    pygame.display.update()
                    game_end = True
                    game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_end = True
                        game_loop = False   
                    if event.key == pygame.K_c:
                        snakegame()
                        game_end = True
                        game_loop = False
        if game_loop == False:
            break  
                    
        snake_x += snake_x_change
        snake_y += snake_y_change
        
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list)>snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = False
        snake_position(snake_list,snake)
        
        pygame.draw.rect(screen,red,(x_food,y_food,snake,snake))
        pygame.display.update() 
        if abs(snake_x - x_food) <= 10 and abs(snake_y - y_food) <= 10:
            
            x_food = random.randint(0,width-10)
            y_food = random.randint(0,height-10)
            snake_length += 1
            
            pygame.draw.rect(screen,red,(x_food,y_food,snake,snake))
            pygame.display.update()
        
        clock.tick(snake_speed)
    


snakegame()
pygame.quit()