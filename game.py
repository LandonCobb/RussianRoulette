import pygame as pg
import sys

class Game:
    def __init__(self, difficulty = 6):
        pg.init()
        self.screen_width = 800
        self.screen_height = 600
        self.window = None

        self.difficulty = difficulty
        print(self.difficulty)

    def start_game(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Russian Roulette")
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            self.window.fill((255, 255, 255))
            pg.display.update()
            
if __name__ == "__main__":
    Game().start_game()