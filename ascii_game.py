import sys, select

class Player(object):
   X_OFFSET = 60 
   Y_OFFSET = 20
    
   CMD_TO_MOVE = {
        'u': (0, -1),
        'd': (0, 1),
        'l': (-1, 0),
        'r': (1, 0)
    }

   def __init__(self):
        self.x = 1
        self.y = 1
        self.MY_MOVE = 'r'

   def move(self):
        i, _, _ = select.select( [sys.stdin], [], [], .1 )
        if i:
             command_str = sys.stdin.readline().strip()
             if command_str not in self.CMD_TO_MOVE:
             	command_str = self.MY_MOVE
        else:
             command_str = self.MY_MOVE
        self.MY_MOVE = command_str
        
        dx, dy = self.CMD_TO_MOVE[command_str]
        if (self.x + dx) > 0 and (self.y + dy) > 0 and (self.x + dx) < self.X_OFFSET and (self.y + dy) < self.Y_OFFSET:
             self.x += dx
             self.y += dy

   def render(self):
        for _ in range(self.y):
            print('.'* self.X_OFFSET)

        print('{} @ {}'
              .format('.' * (self.x - 1),
                      '.' * (self.X_OFFSET - 2 - self.x)))
        
        for _ in range(self.Y_OFFSET - self.y):
            print('.'* self.X_OFFSET)


class Game(object):
    def __init__(self):
        self.player = Player()

    def run(self):
        while True:
            self.player.render()
            self.player.move()

if __name__ == "__main__":
    Game().run()