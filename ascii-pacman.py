import sys, select

class Player:
    X_LIM = 60 
    Y_LIM = 20
    shape = u'\U0001F344' #@
    COMMANDS = {
        'w': (0, -1), #up
        's': (0, 1), #down
        'a': (-1, 0), #left
        'd': (1, 0) #right
    }

    def __init__(self, x_start = 1, y_start = 1, default_move = 'd'):
        self.x = x_start
        self.y = y_start
        self.MY_MOVE = default_move

    def move(self):
        i, _, _ = select.select( [sys.stdin], [], [], .1 ) #check for user input every so often
        if i: #an input is detected!
            if sys.stdin.readline().strip() in self.COMMANDS: #if its valid...
                cmd = sys.stdin.readline().strip() #read the new command from the user
        else:
            cmd = self.MY_MOVE #otherwise keep moving in same direction as before
        self.MY_MOVE = cmd
        dx, dy = self.COMMANDS[cmd]
        if self.valid_space(dx, dy): 
             self.x += dx
             self.y += dy

    def valid_space(self, dx, dy):
        if (self.x + dx) > 0 and (self.y + dy) > 0 and (self.x + dx) < self.X_LIM and (self.y + dy) < self.Y_LIM:  #if within limits of board
            return True
        else:
            return False

    def render(self):
        for _ in range(self.y): print('.'* self.X_LIM)  #rows above player
        print('{}{}{}'.format('.' * (self.x - 1), self.shape ,'.' * (self.X_LIM - 2 - self.x))) #row player is on
        for _ in range(self.Y_LIM - self.y): print('.'* self.X_LIM) #rows below player

class Game(object):
    def __init__(self):
        self.pacman = Player()
        #self.pinky = Ghost()
        #etc...

    def run(self):
        while True:
            self.pacman.render()
            self.pacman.move()

if __name__ == "__main__":
    Game().run()
