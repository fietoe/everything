"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (0,0,255)

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        pygame.draw.ellipse(self.image, BLUE, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        
class Player(pygame.sprite.Sprite):
    def __init__(self):     
        super().__init__()
        self.image = pygame.image.load("player.bmp").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width =  500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(BLACK, 15, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 

clock = pygame.time.Clock()
 
score = 0
font = pygame.font.Font(pygame.font.get_default_font(), 56)
ding_sound = pygame.mixer.Sound("Ding_Sound_Effect.ogg")

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # Set the player object to the mouse location
    
    player.rect.x = pos[0]
    player.rect.y = pos[1] 
    
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    for block in blocks_hit_list:
        score += 1
        #ding_sound.stop() 
        ding_sound.play()
        print(score)

    if(score >= 50):
        end = font.render("You Won!", 1, BLACK) 
        screen.blit(end, (125, 200))
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
