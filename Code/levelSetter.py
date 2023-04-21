import pygame 
import pickle
from os import path
import os
from pygame import gfxdraw
pygame.init()

fps = 60
# gameWindow
screen_width= 1000     # default = 1100
screen_height=800      # default = 800
tile_Size=50          #default 100

screen = pygame.display.set_mode((screen_width,screen_height+150))
pygame.display.set_caption("Level Maker")

img_List=[]
#load images
bg_img=pygame.image.load('Images/bg_img.jpeg')
wall_idx=0
def loadImages():
    entries = os.listdir('./Images')
    # print(entries[1])
    for i in range(0,len(entries)):
        if entries[i]=='bg_img.jpeg' or entries[i] == '.DS_Store':
            continue 
        if entries[i] == 'SideWall.png':
            wall_idx=len(img_List)
        c_path='Images/'
        c_path+=entries[i]
        curr_img=pygame.image.load(c_path)
        # print(entries[i])
        img_List.append(curr_img)
    print("Number of images loaded:"+ str(len(img_List)))
loadImages()

#define game variables
clicked = False
level = 2

white = (255,255,255)
green = (144,201,120)

font = pygame.font.SysFont('Futura',24)

#create empty tile list
world_data= []
N_row= round(screen_height/tile_Size)
N_col= round(screen_width/tile_Size)

for row in range(N_row):
    r = [0] * N_col
    world_data.append(r)

#create Boundary
# row boundary
for x in range(N_col):
    world_data[0][x]= wall_idx #black boundary
    world_data[N_row-1][x]= 2 # grass boundary
for y in range(N_row):
    world_data[y][0] = wall_idx
    world_data[y][N_col-1] = wall_idx

def draw_text(text,font,col,x,y):
    img = font.render(text, True, col)
    screen.blit(img, (x,y))

def drawGridWithTileSize(tile_size):
    # draw vertical lines
    N_ver= round(screen_width/tile_size) - 1
    white=(255,255,255)
    for i in range(0,N_ver):
        start_pos=(tile_size*(i+1),0)
        end_pos=(tile_size*(i+1),screen_height)
        pygame.draw.line(screen,white,start_pos,end_pos,1)
    N_hor= round(screen_height/tile_size) - 1
    # draw horizontal lines
    for i in range(0,N_hor):
        start_pos=(0,tile_size*(i+1))
        end_pos=(screen_width,tile_size*(i+1))
        pygame.draw.line(screen,white,start_pos,end_pos,1)
        DDA_DrawLine(0,tile_size*(i+1),screen_width,tile_size*(i+1))
        


def draw_world():
    for row in range(N_row):
        for col in range(N_col):
                # traverse over all the images and see if it matches any image
                for i in range(len(img_List)):
                    if world_data[row][col] == i+1:
                        img = pygame.transform.scale(img_List[i],(tile_Size,tile_Size))
                        screen.blit(img,(col*tile_Size,row*tile_Size)) 
def Brehsens(x1,y1,x2, y2):  
  
    m_new = 2 * (y2 - y1)  
    slope_error_new = m_new - (x2 - x1) 
  
    y=y1 
    for x in range(x1,x2+1):  
      
        # gfxdraw.pixel(win,round(x),round(y),white)
  
  
        # Add slope to increment angle formed  
        slope_error_new =slope_error_new + m_new  
  
        # Slope error reached limit, time to  
        # increment y and update slope error.  
        if (slope_error_new >= 0):  
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)  
          

def DDA_DrawLine(x1,y1,x2,y2):
	dx=x2-x1
	dy=y2-y1
	abs_dx=abs(dx)
	abs_dy=abs(dy)
	steps=10
	if abs_dx>abs_dy:
		steps=abs_dx
	else:
		steps=abs_dy

	x_inc = dx/float(steps)
	y_inc = dy/float(steps)
	# gfxdraw.pixel(win,round(x1),round(y1),white)
	x=x1
	y=y1
	for i in range(steps):
		x+= x_inc
		y+= y_inc
		# gfxdraw.pixel(win,round(x),round(y),white)
	     
  
class Button():
    def __init__(self, x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft= (x,y)
        self.clicked = False

    def draw(self):
        action = False # ?
        # get mouse position 
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # checking if mouse position is on the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False
        
        #draw button
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

loadBtn = pygame.image.load('Buttons/loadBtn.png')
saveBtn = pygame.image.load('Buttons/saveBtn.png')

# create load and save buttons
save_button = Button(screen_width // 2 - 150, screen_height+40,saveBtn)
load_button = Button(screen_width // 2 + 50, screen_height+40, loadBtn)

run = True

while run:
    # clock.tick(fps) # ?

    #draw background
    screen.fill(green)
    screen.blit(bg_img,(0,0))

    #load and save level
    if save_button.draw(): # returns if the button was clicked by determining the mouse postion coordinates
        pickle_out = open(f'level{level}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    
    if load_button.draw():
        #load in level data
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)

    draw_world()
    # drawGridWithTileSize(tile_Size)

    #text showing current level
    draw_text(f'Level: {level}', font, white, tile_Size, screen_height+70 )
    draw_text('Press UP or DOWN to change level', font, white, tile_Size, screen_height+110)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        
        #mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked= True
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_Size
            y = pos[1] // tile_Size
            # check that the coordinates are within the tile area
            print('Clicked mouse button')
            print(str(x)+" , "+str(y))
            if x < N_col and y < N_row :
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] = (world_data[y][x]+1)%(len(img_List)+1) # will cycle over all the images
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if(world_data[y][x]<0):
                        world_data[y][x]=len(img_List)
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
		#up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 2:
                level -= 1
    #update game display window
    pygame.display.update()

pygame.quit()          
