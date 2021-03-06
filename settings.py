from time import sleep
from os import listdir, remove
from random import choice, randint
from datetime import datetime
from paths import *

pg.display.set_caption(NAME_OF_THE_GAME)
DISPLAY_DEFAULT = 747
MAIN_SCREEN = pg.display.set_mode((DISPLAY_DEFAULT, 1050), pg.SCALED | pg.RESIZABLE)

VERSION = '2.0'
LOG = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

FRAMES = pg.time.Clock()
MAX_FRAMES = 30

FONT_SETTINGS = pg.font.SysFont('arial', 25, True)
LIMBO = -1080

MAX_RECORDS = 9
MIN_CHARACTERS_NAME, MAX_CHARACTERS_NAME = 3, 20

soundtrack = [SONGS['orpheus']]
click_sound = SOUNDS['click']


class Obj(pg.sprite.Sprite):
    """
    Primary class to add any object

    image = (str) -- folder/imagename/type(.png or .jpg)
    rect_x = (int) -- horizontal position
    rect_y = (int) -- vertical position
    width and height -- get the width and height of the current image

    This class has methods inherited from pygame's Sprite class.
    So any object must be assigned to a group of "pygame.sprite.Group()"
    example:

    #################################################################################
    screen = pygame.display.set_mode((500, 500), pygame.SCALED | pygame.FULLSCREEN)
    group_1 = pygame.sprite.Group()

    x = Obj(img='folder/imagename.png', x=0, y=100, group_1)

    Method to design group sprites:

    while main_loop:
        group_1.draw(screen)
    """

    def __init__(self, img, x, y, *groups):

        super().__init__(*groups)

        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()


def save_log():

    with open('codes/log', 'a') as up_log:

        up_log.write(LOG + ' < // > ' + date_time() + '\n')

    click_sound.play()
    sleep(1), pg.quit(), quit()


def date_time():

    return datetime.today().strftime('%d/%m/%Y %H:%M:%S')


def draw_texts(screen, TXT: str, X: int, Y: int, font='arial', size=15, color=(255, 255, 255)):

    txt = pg.font.SysFont(font, size, True)
    t = txt.render(f'{TXT}', True, color)

    screen.blit(t, (X, Y))


def check_records(FOLDER_: str):
    """
    CHECKS AND TREAT THE FILES IN THE SAVED FOLDER
    :type FOLDER_: SAVE FOLDER NAME -> STR
    :return: RETURNS LIST WITH VALID SAVED
    """
    list_records = [x for x in listdir(FOLDER_)]
    records = []

    for save in list_records:

        if not open(FOLDER_ + save, mode='r+', encoding='utf-8').readlines():
            remove(FOLDER_ + save)

        with open(FOLDER_ + save, mode='r+', encoding='utf-8') as file:
            records.append(file.read().strip().split('\n'))

    return records
