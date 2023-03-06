import pygame as pg
import sys
import random
import webbrowser
import keyboard
import os
import start_main

class Game:
    def __init__(self, difficulty = 7):
        pg.init()
        self.screen_width = 800
        self.screen_height = 600
        self.window = None

        self.difficulty = difficulty
        
        self.cylinder = [False for i in range(difficulty)]
        self.cylinder[random.randint(0, self.difficulty - 1)] = True
        
        self.cylinder_position = 0

        self.fire_rect = pg.Rect(0, 0, 600, 100)
        self.fire_rect.center = (self.screen_width // 2, 500)

        self.back_rect = pg.Rect(0, 0, 50, 50)

        self.dead = False
        
        self.dog = pg.image.load("./assets/dogewiththegat.png")
        self.gru = pg.image.load("./assets/gruwiththegat.jpg")
        self.revolver = pg.image.load("./assets/normalrevolver.jpg")
        self.suicide = pg.image.load("./assets/suicide.jpg")
        self.cat = pg.image.load("./assets/thecatwiththegat.jpg")
        self.chad_image = pg.image.load("./assets/gigachad.jpg")
        self.death_image = pg.image.load("./assets/RRbang.png")

        self.boom = pg.mixer.Sound("./assets/vine-boom.mp3")
        self.chad_sound = pg.mixer.Sound("./assets/gigachadmusic.mp3")        
        self.hitmarker_sound = pg.mixer.Sound("./assets/hitmarker_2.mp3")        
        self.rust_sound = pg.mixer.Sound("./assets/rustheadshot.mp3")        
        
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

        self.chad_animation_time = 0
        self.death_animation_time = 0
        self.deez_nuts = 10
        self.playing_chad = False
        self.playing_death = False

    def punishment(self):
        if self.difficulty == 1:
            # os.system("shutdown /s /t 1")
            print("shutdown")
        else:
            match random.randint(1, 3):
                case 1:
                    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
                case 2:
                    keyboard.on_press(lambda key : self.boom.play())
                case 3:
                    keyboard.block_key("capslock")
                    keyboard.press_and_release("capslock")

    def draw_objects(self):
        self.window.fill((255, 255, 255))

        self.window.blit(pg.transform.scale(self.background_image, (self.screen_width, self.screen_height)), (0, 0))

        self.animation()

        pg.draw.rect(self.window, (255, 0, 0), self.fire_rect, 5, 10)
        fire_text = pg.font.Font(None, 100).render("PULL TRIGGER", True, (255, 0, 0))
        self.window.blit(fire_text, fire_text.get_rect(center = self.fire_rect.center))

        back_text = pg.font.Font(None, 40).render("<", True, (0, 0, 0))
        self.window.blit(back_text, back_text.get_rect(center = self.back_rect.center))

    def animation(self):
        if self.playing_chad:
            self.window.blit(pg.transform.scale(self.chad_image, (self.screen_width, self.screen_height)), (0, 0))
            if self.chad_animation_time == 0:
                self.chad_sound.play()
                self.chad_animation_time += 1
            elif self.chad_animation_time == 400:
                self.chad_sound.stop()
                self.playing_chad = False
                self.chad_animation_time = 0
            else:
                self.chad_animation_time += 1
                
        if self.playing_death:
            self.window.blit(self.death_image, self.death_image.get_rect(center = (self.screen_width // 2, self.screen_height // 2)))
            if self.death_animation_time == 0:
                self.death_animation_time += 1
            elif self.death_animation_time % 10 == 0 and self.death_animation_time != 100:
                self.hitmarker_sound.play()
                self.death_animation_time += 1
            elif self.death_animation_time == 100:
                self.playing_death = False
                self.death_animation_time = 0
                self.punishment()
            else:
                self.death_animation_time += 1
        
    def start_game(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Russian Roulette")
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.fire_rect.collidepoint(event.pos[0], event.pos[1]) and not self.dead and not self.playing_chad and not self.playing_death:
                        if self.cylinder[self.cylinder_position]:
                            print("you died")
                            self.dead = True 
                            self.playing_death = True
                        else:
                            print("you live")
                            self.playing_chad = True
                            self.cylinder_position += 1
                    
                    if self.back_rect.collidepoint(event.pos[0], event.pos[1]) and not self.playing_chad and not self.playing_death:
                        start_main.start()
            
            self.draw_objects()
            pg.display.update()
            
if __name__ == "__main__":
    Game().start_game()