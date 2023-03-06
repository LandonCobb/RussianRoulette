import pygame as pg
import pygame_menu as pm
from game import Game

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.update()

def run_game(difficulty):
    Game(difficulty).start_game()

theme = pm.themes.THEME_DEFAULT.copy()

background_image = pm.baseimage.BaseImage(
    image_path="./assets/BFbackground.jpg",
    drawing_mode=pm.baseimage.IMAGE_MODE_FILL,
)

theme.background_color = background_image

main_menu = pm.Menu("Ball Roulette", 800, 600, theme=theme)
main_menu.add.button("Easy", run_game, 10)
main_menu.add.button("Normal", run_game, 7)
main_menu.add.button("Hard", run_game, 4)
main_menu.add.button("EXTREME", run_game, 2)
main_menu.add.button("SUICIDE", run_game, 1)

def start():
    main_menu.mainloop(screen)