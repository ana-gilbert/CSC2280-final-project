import pygame


#intialize the font and mixer modules
pygame.font.init()
pygame.mixer.init()

############################################
##             GAME CONSTANTS             ##
############################################

#set width and height of the game window
WIDTH  = 900
HEIGHT = 500

#creates a display with the width and height defined before
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#sets a caption at top of game window w/ game name
pygame.display.set_caption("BUBBLE BLASTER!")

#constants for colors the text and border
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (250, 107, 207)
GREEN = (113, 250, 110)
#creates the border to divide the 2 sides of the screen
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# all the fonts and sizes to be used when i draw in text
HEALTH_FONT = pygame.font.SysFont('Impact', 40)
WINNER_FONT = pygame.font.SysFont('Impact', 100)
PAUSE_FONT = pygame.font.SysFont('Impact', 60)
SCORE_FONT = pygame.font.SysFont('Impact', 80)
MENU_FONT =  pygame.font.SysFont('Impact', 90)
OPTION_FONT = pygame.font.SysFont('Impact', 50)
OPTION2_FONT = pygame.font.SysFont('Impact', 35)

#frames per second for the clock
FPS = 60

#velocities for the players and the bubbles
VEL = 7
BUBBLE_VEL = 15

#max amount of bubbles that can be shot at once
MAX_BUBBLES = 3

# width and height of the fish images
FISH_WIDTH = 108
FISH_HEIGHT = 130

# custom user events for when a bubble collides with a character
PINK_HIT = pygame.USEREVENT + 1
GREEN_HIT = pygame.USEREVENT + 2

#load on images for the fish, bubbles, and background and scale to the correct sizes
PINK_FISH_IMAGE = pygame.image.load("pinkfish.png")
PINK_FISH = pygame.transform.scale(PINK_FISH_IMAGE, (FISH_WIDTH, FISH_HEIGHT))

GREEN_FISH_IMAGE = pygame.image.load("greenfish.png")
GREEN_FISH = pygame.transform.scale(GREEN_FISH_IMAGE, (FISH_WIDTH, FISH_HEIGHT))

BUBBLE_IMAGE = pygame.image.load("bubble.png")
BUBBLE = pygame.transform.scale(BUBBLE_IMAGE, (35, 35))

BACKGROUND = pygame.transform.scale(pygame.image.load("ocean_bg.jpeg"), (WIDTH, HEIGHT))

#load in background music and popping sound, start playing background music ( the (-1) parameter loops the music)
pygame.mixer.music.load("game_music.mp3")
pop = pygame.mixer.Sound("pop.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

############################################
##             GAME FUNCTIONS             ##
############################################

# draws in the pause screen when ESCAPE is pressed
def pause_screen():
        
    WINDOW.blit(BACKGROUND, (0, 0)) #draw in blank version of the background

    # define text
    menu_text = PAUSE_FONT. render("PAUSED" , 1, PINK)
    start_text = PAUSE_FONT.render("-press ESCAPE to start-", 1, WHITE)

    #draw in text
    WINDOW.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, 150))
    WINDOW.blit(start_text, (WIDTH// 2 - start_text.get_width() // 2, 250))
        
    pygame.display.update()  # update screen display to show new background and text

# draws in the main menu screen sonce the game opens    
def main_menu():
    WINDOW.blit(BACKGROUND, (0, 0)) #draw in blank version of the background

    # define and draw in title
    menu_text = MENU_FONT.render("BUBBLE BLASTER!", 1, PINK)
    WINDOW.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 - menu_text.get_height()))
    
    #define and draw in start instruction
    start_text = OPTION_FONT.render("-press SPACE to begin-", 1, WHITE)
    WINDOW.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + menu_text.get_height() + start_text.get_height() - 170))

    instruct_text = OPTION_FONT.render("-press ENTER for instructions-", 1, WHITE)
    WINDOW.blit(instruct_text, (WIDTH // 2 - instruct_text.get_width() // 2, HEIGHT // 2 + menu_text.get_height() + start_text.get_height() + instruct_text.get_height() - 170))

    pygame.display.update()  # update screen display to show new background and text

# draws in the instructions screen when enter is pressed and if the start screen is open 
def instruct():
    WINDOW.blit(BACKGROUND, (0, 0)) #draw in blank version of the background

    #define and draw in all instructions to be written on instruction menu
    instruct1 = OPTION_FONT.render("PINK FISH:", 1, PINK) 
    WINDOW.blit(instruct1, (WIDTH // 3 - instruct1.get_width(), 60))

    instruct2 = OPTION2_FONT.render("ASWD to move", 1, WHITE)
    WINDOW.blit(instruct2, (WIDTH // 3 - instruct1.get_width(), instruct1.get_height() + 60))

    instruct3 = OPTION2_FONT.render("L SHIFT to fire", 1, WHITE)
    WINDOW.blit(instruct3, (WIDTH // 3 - instruct1.get_width(), instruct1.get_height() + instruct2.get_height() + 60))

    instruct4 = OPTION_FONT.render("GREEN FISH:", 1, GREEN)
    WINDOW.blit(instruct4, (WIDTH // 3 + instruct4.get_width(), 60))

    instruct5 = OPTION2_FONT.render("ARROW KEYS to move", 1, WHITE)
    WINDOW.blit(instruct5, (WIDTH // 3 + instruct4.get_width(), instruct4.get_height() + 60))

    instruct6 = OPTION2_FONT.render("R SHIFT  to fire", 1, WHITE)
    WINDOW.blit(instruct6, (WIDTH // 3 + instruct4.get_width(), instruct4.get_height() + instruct5.get_height() + 60))

    instruct7 = OPTION_FONT.render("Shoot Bubbles at the Opposing Fish", 1, WHITE)
    WINDOW.blit(instruct7, (WIDTH // 2 - instruct7.get_width() // 2, instruct4.get_height() + instruct5.get_height() + instruct6.get_height() + 90))

    instruct8 = OPTION_FONT.render("First Hit Opponent 10 Times WINS ", 1, WHITE)
    WINDOW.blit(instruct8, (WIDTH // 2 - instruct8.get_width() // 2, instruct4.get_height() + instruct5.get_height() + instruct6.get_height() + instruct7.get_height() + 90))
    
    instruct9 = OPTION_FONT.render("ESCAPE to pause", 1, WHITE)
    WINDOW.blit(instruct9, (WIDTH // 2 - instruct9.get_width() // 2, instruct4.get_height() + instruct5.get_height() + instruct6.get_height() + instruct7.get_height() + instruct8.get_height() + 90))

    instruct10 = OPTION2_FONT.render("-TAB to return to main menu-", 1, BLACK)
    WINDOW.blit(instruct10, (WIDTH // 2 - instruct10.get_width() // 2, 440))
    
    pygame.display.update() # update screen display to show new background and text

# draw in main game screen with fish, bubbles, health bars and the divider
def draw_window(green, pink, green_bubbles, pink_bubbles, green_health, pink_health):

    # draw in a blank version of the background and a blacl rectangle in the middle to divide the screen
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    #define and draw in the two health bars for the top of each side of the screen
    # add the health variables to the new text variable to ensure the health updates as players take damage
    green_health_text = HEALTH_FONT.render(
        "Health: " + str(green_health), 1, WHITE)
    pink_health_text = HEALTH_FONT.render(
        "Health: " + str(pink_health), 1, WHITE)
    WINDOW.blit(green_health_text, (WIDTH - green_health_text.get_width() - 10, 10))
    WINDOW.blit(pink_health_text, (10, 10))
    
    # draw in the fish characters at the location defined in main()
    WINDOW.blit(PINK_FISH, (pink.x, pink.y))
    WINDOW.blit(GREEN_FISH, (green.x, green.y))

    # cycles throgh the bubble lists, if there is a bubble in the list, draw it and move it across the screen from where it was shot
    for bubbles in green_bubbles:
        WINDOW.blit(BUBBLE, bubbles)

    for bubbles in pink_bubbles:
        WINDOW.blit(BUBBLE, bubbles)

    pygame.display.update() # update the screen

#function thats handles the pink fish's movement around the screen
def pink_handle_movement(keys_pressed, pink):
    # when A is pressed, pink moves left IF the x coordinate - the velocity is greater than 0
    if keys_pressed[pygame.K_a] and pink.x - VEL > 0:  
        pink.x -= VEL

    # when D is pressed, pink moves right IF the x coordinate + the velocity + the width of the pink fish is LESS than the BORDER'S  x coordinate
    if keys_pressed[pygame.K_d] and pink.x + VEL + pink.width < BORDER.x:
        pink.x += VEL

    # when W is pressed, pink moves up IF the y coordinate - the velocity is greater than 0
    if keys_pressed[pygame.K_w] and pink.y - VEL > 0:
        pink.y -= VEL

    # when S is pressed, pink moves down IF the y coordinate + the velocity + the height of teh pink fish is LESS than than the HEIGHT of the screen - 15 
    if keys_pressed[pygame.K_s] and pink.y + VEL + pink.height < HEIGHT - 15:  
        pink.y += VEL

#function thats handles the green fish's movement around the screen
def green_handle_movement(keys_pressed, green):
    # when left arrow is pressed, green moves left IF the x coordinate - the velocity is greater than the BORDER's x coordinate + the BORDER'S width
    if keys_pressed[pygame.K_LEFT] and green.x - VEL > BORDER.x + BORDER.width:  
        green.x -= VEL

    # when right arrow is pressed, green moves right IF the x coordinate + the velocity + the width of the green fish is LESS than the width of the screen
    if keys_pressed[pygame.K_RIGHT] and green.x + VEL + green.width < WIDTH:  # green moves right using right arrow key
        green.x += VEL
    
    # when up arrow is pressed, green moves up IF the y coordinate - the velocity is greater than 0
    if keys_pressed[pygame.K_UP] and green.y - VEL > 0:  # green moves up using up arrow key
        green.y -= VEL

    # when down arrow is pressed, green moves down IF the y coordinate + the velocity + the height of the green fish is LESS than than the HEIGHT of the screen - 15    
    if keys_pressed[pygame.K_DOWN] and green.y + VEL + green.height < HEIGHT - 15:  # green moves down using down arrow key
        green.y += VEL

# function that handles when and how the bubbles move across the screen
def handle_bubbles(pink_bubbles, green_bubbles, pink, green):
    #cycles through bubbles shot by the pink fish
    for bubbles in pink_bubbles:
        #increases the x coordinate of the pink bubble by the bubbles velocity (15)
        bubbles.x += BUBBLE_VEL
        # if the green fish hits a bubble, remove that bubbles from the pink list and the screen, and use our custom user event GREEN_HIT
        if green.colliderect(bubbles):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            pink_bubbles.remove(bubbles)
        # when the bubble hits the other end of the screen remove it from the pink list    
        elif bubbles.x > WIDTH:
            pink_bubbles.remove(bubbles)
        

    for bubbles in green_bubbles:
        #decreases the x coordinate of the green bubble by the bubbles velocity (15)
        bubbles.x -= BUBBLE_VEL
        # if the pink fish hits a bubble, remove that bubble from the green list and the screen, and use our custom user event PINK_HIT
        if pink.colliderect(bubbles):
            pygame.event.post(pygame.event.Event(PINK_HIT))
            green_bubbles.remove(bubbles)
        # when the bubble hits the other end of the screen remove it from the green list    
        elif bubbles.x < 0:
            green_bubbles.remove(bubbles)

    
#function to draw the winner screen, uses the green or pink text sent at the call
def draw_winner(text):
    #define the text and draw it onto the screen
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    
    #update the screen and wait about 4 seconds to switch screens
    pygame.display.update()
    pygame.time.delay(4000)


#function that display the score screen after each round    
def draw_score(green_score, pink_score):  
    #draw in a blank background and the border
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    
    #define the scores text using the updating scores sent over at the call
    green_score_text= SCORE_FONT.render(
        "Score: " + str(green_score), 1, WHITE)
    pink_score_text= SCORE_FONT.render(
        "Score: " + str(pink_score), 1, WHITE)
    
    # draw in the score texts on either side of the border
    WINDOW.blit(green_score_text, (WIDTH//4 - 150, 175))
    WINDOW.blit(pink_score_text, (WIDTH//4 + green_score_text.get_width() + 75, 175))

    # update the screen and wait 3 seconds
    pygame.display.update()
    pygame.time.delay(3000)

# main game function where everything runs
def main():

    # the green and pink fish hit boxes
    green = pygame.Rect(700, 300, FISH_WIDTH, FISH_HEIGHT)
    pink = pygame.Rect(100, 300, FISH_WIDTH, FISH_HEIGHT)

    # intialize the scores to 0
    green_score = 0
    pink_score = 0
    # set the start screen variable to True so we start on that screen, paused to False , and instructions to False
    start = True
    paused = False
    instructions = False

    # intialize the clock
    clock = pygame.time.Clock()
    
    #first game loop
    while True:
        #set both healths to their max 10
        green_health = 10
        pink_health = 10

        # set winner text to nothing 
        winner_text = ""

        #reset paused to False
        paused = False

        #set the bubbles lists to empty
        green_bubbles = []
        pink_bubbles = []
        
        # make sure user can still exit on the start screen
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

        #subsequest rounds loop
        while True:
            # clock ticks at 60 frames per second
            clock.tick(FPS)
            keys_pressed = pygame.key.get_pressed() #
            
            # if the start variable is True, draw in the start screen
            if start == True:
                main_menu()

            # if the instructions variable is True, draw in the instructions screen
            if instructions == True:
                instruct()

            #if the pause variable is True, draw in the pause screen    
            if paused == True:
                pause_screen()

            #start checking for events
            for event in pygame.event.get():
                # if the X button is clicked, quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                # if a key is held down...   
                if event.type == pygame.KEYDOWN:
                    # if the escape key is pressed...
                    if event.key == pygame.K_ESCAPE:
                        #if both the instructions and start menu are off then the pause menu can turn on
                        if instructions == False and start == False:
                            # if the pause menu is already on switch it off
                            if paused == True:
                                paused = False
                            else:
                                paused = True
                    
                    # if the space key is pressed...
                    if event.key == pygame.K_SPACE:    
                        # turn off the main menu and start the game
                        if start == True:
                            start = False

                    # if the enter key is pressed...
                    if event.key == pygame.K_RETURN:          
                        # only turn on the instructions menu if we are on the menu screen
                        if start == True:
                            instructions = True

                    # if tab key is pressed...           
                    if event.key == pygame.K_TAB:          
                        # if we are on the instructions menu (aka we aren't on the start menu or the main game screen)
                        if start == False:
                            # if we are on the instructions menu, turn instructions off and go back to start menu
                            if instructions == True:
                                instructions = False
                                start = True
                            
                    # if the left shift key is pressed, AND the length of the pink bubbles list is less than the max bubbles allowed (3), AND the start, instructions, and paused, menus are all turned off...        
                    if event.key == pygame.K_LSHIFT and len(pink_bubbles) < MAX_BUBBLES and not paused and not start and not instructions:
                         # set the bubbles variable to a rectangle that start at the green fish's location, this will be used to move the image across the screen
                        bubbles = pygame.Rect(
                            pink.x + pink.width, pink.y + pink.height // 2 - 2, 10, 5)
                        # add a bubble to the pink_bubbles list
                        pink_bubbles.append(bubbles)
                        # play the pop sound!
                        pygame.mixer.Sound.play(pop)
                        
                    # if the right shift key is pressed, AND the length of the pink bubbles list is less than the max bubbles allowed (3), AND the start, instructions, and paused, menus are all turned off...        
                    if event.key == pygame.K_RSHIFT and len(green_bubbles) < MAX_BUBBLES and not paused and not start and not instructions:
                        # set the bubbles variable to a rectangle that start at the green fish's location, this will be used to move the image across the screen
                        bubbles = pygame.Rect(
                            green.x, green.y + green.height // 2 - 2, 10, 5)
                        # add a bubble to the green_bubbles list
                        green_bubbles.append(bubbles)
                        # play the pop sound!
                        pygame.mixer.Sound.play(pop)

                # if the green fish gets hit AND the pause, start, and instructions screens are off
                if event.type == GREEN_HIT and not paused and not start and not instructions:
                    green_health -= 1
                    
                # if the pink fish gets hit AND the pause, start, and instructions screens are off
                if event.type == PINK_HIT and not paused and not start and not instructions:
                    pink_health -= 1
                    
            # set the winner text to nothing 
            winner_text = ""

            # if the green health drops to 0, set the winner text to Pink Fish Wins!, and increase the pink score
            if green_health < 1:
                winner_text = "Pink Fish Wins!"
                pink_score += 1

            # if the pink health drops to 0, set the winner text to Green Fish Wins!, and increase the green score
            if pink_health < 1:
                winner_text = "Green Fish Wins!"
                green_score += 1

            # if the winner text is NOT nothing, draw in the winner screen the n the score screen, then break and go back to the first game loop to reset certain variables
            if winner_text != "":
                draw_winner(winner_text)
                draw_score(pink_score, green_score)
                break

            # if the pause, start , and instructions menus are turned off...
            if not paused and not start and not instructions:

                # call the main window drawing function, the pink and green fish movement functions, and the bubble movement functions
                draw_window(green, pink, green_bubbles, pink_bubbles, green_health, pink_health)
                
                pink_handle_movement(keys_pressed, pink)
                green_handle_movement(keys_pressed, green)

                handle_bubbles(pink_bubbles, green_bubbles, pink, green)


# call the main game function!!
main()