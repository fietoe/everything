import pygame
 
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
blue = (0, 195, 255)
 
PI = 3.141592653
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Drawing")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, blue, [0, 0, 700, 500])
    pygame.draw.line(screen, BLACK, [350, 200], [450, 155], 10) #top right
    pygame.draw.line(screen, BLACK, [450, 155], [400, 250], 10)
    
    pygame.draw.line(screen, BLACK, [400, 250], [500, 315], 10)#middle right
    pygame.draw.line(screen, BLACK, [500, 315], [390, 315], 10)    
    
    pygame.draw.line(screen, BLACK, [350, 200], [250, 155], 10)#top left
    pygame.draw.line(screen, BLACK, [250, 155], [300, 250], 10)
    
    pygame.draw.line(screen, BLACK, [300, 250], [200, 314], 10)#middle left
    pygame.draw.line(screen, BLACK, [200, 314], [310, 314], 10)   
    
    pygame.draw.line(screen, BLACK, [310, 314], [350, 414], 10)#bottom centre
    pygame.draw.line(screen, BLACK, [390, 315], [350, 414], 10)
 
    pygame.draw.arc(screen, BLACK, [300,150,100,50],  PI/2,     PI, 10)#centre top curve
    pygame.draw.arc(screen, BLACK, [300,150,100,50],     0,   PI/2, 10)
    
    pygame.draw.arc(screen, BLACK, [400,200,60,80],     0,   PI/2, 10)#centre middle right curve
    pygame.draw.arc(screen, BLACK, [400,200,60,70],3*PI/2,   2*PI, 10)
    
    pygame.draw.arc(screen, BLACK, [370,280,70,80],3*PI/2,   2*PI, 10)#centre bottom right curve
    #pygame.draw.arc(screen, BLACK, [385,280,65,80],    PI, 3*PI/2, 10)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()