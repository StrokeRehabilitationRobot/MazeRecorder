from pygame.locals import *
import pygame
import mazeBank

# Colors for use throughout
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARK_BLUE = (0,0,128)
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (255,200,200)
PURPLE = (255,150,255)

# Map element sizes
BLOCKSIZE_X = 50
BLOCKSIZE_Y = 50
PLAYERSIZE_X = 20
PLAYERSIZE_Y = 20

# Translating arm motion to map
THRESHOLD = 0.05
Y_CUTOFF = 0.35

maze1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1,
         1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1,
         1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         ]

maze2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         ]

maze3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1,
         1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1,
         1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         ]

maze4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         ]

maze5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
         1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1,
         1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         ]

trainer1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            ]

class Player:
    # Initialize player to block in second row, second column
    x = BLOCKSIZE_X + 1
    y = BLOCKSIZE_Y + 1
    prev_x = x
    prev_y = y
    ## CHANGE PLAYER SPEED HERE
    speed = 1
    ########

    # Move right relative to current position, using speed modified by magnitude (mag)
    def moveRight(self, mag):
        self.prev_x = self.x
        self.x = self.x + (self.speed*mag)

    # Move left relative to current position, using speed modified by magnitude (mag)
    def moveLeft(self, mag):
        self.prev_x = self.x
        self.x = self.x - (self.speed*mag)

    # Move up relative to current position, using speed modified by magnitude (mag)
    def moveUp(self, mag):
        self.prev_y = self.y
        self.y = self.y - (self.speed*mag)

    # Move down relative to current position, using speed modified by magnitude (mag)
    def moveDown(self, mag):
        self.prev_y = self.y
        self.y = self.y + (self.speed*mag)

    # Move to a position, ideally representing the end effector position of the robot
    def goTo(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y

    # Draw the player inside the maze
    def draw(self, display_surf):
        #pygame.draw.rect(display_surf, BLACK,
        #                (self.prev_x, self.prev_y, PLAYERSIZE_X, PLAYERSIZE_Y), 0)
        pygame.draw.rect(display_surf, GREEN,
                         (self.x, self.y, PLAYERSIZE_X, PLAYERSIZE_Y), 0)

class Maze:
    def __init__(self):
        self.M = 15 # number of columns
        self.N = 12 # number of rows
        ## SELECT MAZE NUMBER
        self.my_mazeBank = mazeBank.mazeBank
        self.maze = self.my_mazeBank.getMaze(self.my_mazebank, "maze2")
        #####################

    # Check if a cell is a wall or the goal (1 = wall, 2 = goal, 0 = path)
    def checkCell(self, loc_x, loc_y):
        # If the cell in the maze array is a 1, the cell is a wall
        if self.maze[loc_x + (loc_y * self.M)] == 1:
            return 1
        # If the cell is not a wall, but is located in the last column, the cell is the goal
        elif loc_x == (self.M - 1):
            return 2
        else:
            return 0

    def draw(self, display_surf):
        # Initialize row and columns counters
        bx = 0
        by = 0
        # Iterate over maze array
        for i in range(0, self.M * self.N):
            # If an element is a '1', color it as a wall
            if self.maze[bx + (by * self.M)] == 1:
                pygame.draw.rect(display_surf, PURPLE,
                                 (bx*BLOCKSIZE_X, by*BLOCKSIZE_Y, BLOCKSIZE_X, BLOCKSIZE_Y), 0)
            # Update iterator, and if it reaches the end of the row, increase row counter and reset column counter to 0
            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1


class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.player = Player()
        self.maze = Maze()

    # Initialize game, window, maze
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self.maze.draw(self._display_surf)
        pygame.display.update()

    # Not used
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    # Empty loop function, called regularly during operation
    def on_loop(self):
        pass

    # Re-render maze (just draws new player position, since player path is preserved)
    def on_render(self):
        #self._display_surf.fill((0, 0, 0))
        #self.maze.draw(self._display_surf)
        self.player.draw(self._display_surf)
        pygame.display.update()

    # Exit sequence
    def on_cleanup(self):
        pygame.quit()

    # Execute a movement based on arm movement (velocity mode)
    # Check the coordinates of the end effector (y-value shifted)
    # Move arm at a speed proportional to the distance from the 0 point on the axis
    def arm_move(self, x_sign, y_sign):
        if ((y_sign - Y_CUTOFF) < (0 - THRESHOLD)):
            print('Y value is ' + str(y_sign - Y_CUTOFF) + ' and direction is up')
            self.player.moveUp(2*abs(y_sign - Y_CUTOFF))

        if ((y_sign - Y_CUTOFF) > (0 + THRESHOLD)):
            print('Y value is ' + str(y_sign - Y_CUTOFF) + ' and direction is down')
            self.player.moveDown(2*abs(y_sign - Y_CUTOFF))

        if (x_sign < (0 - THRESHOLD)):
            print('X value is ' + str(x_sign) + ' and direction is right')
            self.player.moveRight(abs(x_sign))

        if (x_sign > (0 + THRESHOLD)):
            print('X value is ' + str(x_sign) + ' and direction is left')
            self.player.moveLeft(abs(x_sign))

    # Execute a movement based on arm position
    def arm_pos(self, loc_x, loc_y):
        self.player.goTo(loc_x, loc_y)

    # When app is called from this file, this is the execution loop
    def on_execute(self):
        # Initialize maze
        if self.on_init() == False:
            self._running = False

        # Execution loop - use keys as input, ESC to quit
        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()


            if (keys[K_RIGHT]):
                self.player.moveRight(1)

            if (keys[K_LEFT]):
                self.player.moveLeft(1)

            if (keys[K_UP]):
                self.player.moveUp(1)

            if (keys[K_DOWN]):
                self.player.moveDown(1)

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()