import random
import pygame
##################################################################
#must do for setting

pygame.init() #un-checked-python> linting: Enable from Setting

#setting screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#screen title 
pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()

#####################################################################
#1. background, game image, font, speed...

#background
background = pygame.image.load("/Users/yejiahn/Desktop/projects/basic_game/game/background.png")

#character-sprite 
character = pygame.image.load("/Users/yejiahn/Desktop/projects/basic_game/game/character.png")
character_size = character.get_rect().size #image size
character_width = character_size[0] #size of width
character_height = character_size[1] #size of height
character_x_pos = screen_width / 2 - (character_width / 2) #half size of width position
character_y_pos = screen_height - character_height # bottom of the screen

to_x = 0
to_y = 0

#speed
character_speed = 0.6

#enemy character
enemy = pygame.image.load("/Users/yejiahn/Desktop/projects/basic_game/game/enemy.png")
enemy_size = enemy.get_rect().size #image size
enemy_width = enemy_size[0]  #size of width
enemy_height = enemy_size[1]#size of height
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

#font
game_font = pygame.font.Font(None, 40) #font size

#total time
total_time = 30

#start time
start_ticks = pygame.time.get_ticks()

##################################################################

# event loop
running = True 
while running:
    dt = clock.tick(30) #frame number per second
    # print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if close
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: #if not press 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    character_x_pos += to_x * dt


    # width boarderline
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # #collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # #check collision
    if character_rect.colliderect(enemy_rect):
        print("collision")
        running = False

    screen.blit(background,(0,0)) #draw background
    screen.blit(character,(character_x_pos, character_y_pos)) #draw character
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos)) #draw enemy 

    #timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000 #change to second from ms

    # text, True, font color
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    #if time is under 0:
    if total_time - elapsed_time <= 0:
        running = False

    # pygame.timer.delay(2000) #wait 2s to close the game

    pygame.display.update() 

#end game
pygame.quit()