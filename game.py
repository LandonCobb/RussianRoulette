import pygame as pg
import sys
import random
import webbrowser

class Game:
    def __init__(self, difficulty = 7):
        pg.init()
        self.screen_width = 800
        self.screen_height = 600
        self.window = None

        self.difficulty = difficulty
        
        self.cylinder = [False for i in range(difficulty)]
        self.cylinder[random.randint(0, self.difficulty - 1)] = True
        print(self.cylinder)
        
        self.cylinder_position = 0

        self.fire_rect = pg.Rect(0, 0, 600, 100)
        self.fire_rect.center = (self.screen_width // 2, 500)

        self.dead = False
        
        self.dog = pg.image.load("./assets/dogewiththegat.png")
        self.gru = pg.image.load("./assets/gruwiththegat.jpg")
        self.revolver = pg.image.load("./assets/normalrevolver.jpg")
        self.suicide = pg.image.load("./assets/suicide.jpg")
        self.cat = pg.image.load("./assets/thecatwiththegat.jpg")
        
        if self.difficulty == 10:
            self.background_image = self.revolver
        elif self.difficulty == 7:
            self.background_image = self.dog
        elif self.difficulty == 4:
            self.background_image = self.gru
        elif self.difficulty == 2:
            self.background_image = self.cat
        elif self.difficulty == 1:
            self.background_image = self.suicide
        else:
            self.background_image = self.suicide

    def draw_objects(self):
        self.window.fill((255, 255, 255))

        self.window.blit(pg.transform.scale(self.background_image, (self.screen_width, self.screen_height)), (0, 0))
        
        pg.draw.rect(self.window, (255, 0, 0), self.fire_rect, 5, 10)
        fire_text = pg.font.Font(None, 100).render("PULL TRIGGER", True, (255, 0, 0))
        self.window.blit(fire_text, fire_text.get_rect(center = self.fire_rect.center))

    def start_game(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Russian Roulette")
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    # code to easily save mouse positions for testing
                    # with open("cords.txt", "a") as cords:
                    #     cords.write(", ".join(map(str, event.pos)))
                    #     cords.write("\n")
                    if self.fire_rect.collidepoint(event.pos[0], event.pos[1]) and not self.dead:
                        if self.cylinder[self.cylinder_position]:
                            print("you died")
                            self.dead = True
                            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
                        else:
                            print("you live")
                            self.cylinder_position += 1
                    
            self.draw_objects()
            pg.display.update()
            
if __name__ == "__main__":
    Game().start_game()