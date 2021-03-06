from settings import *

soundtrack[0].play()


class Menu:

    class_menu = True
    BLOCK = False
    check = ''

    def __init__(self, *groups):

        self._background = Obj(IMG_MENU['bg'], 0, 0, *groups)

        self._guides = []

        self._objects = {
            'select': Obj(IMG_MENU['select'], 0, LIMBO, *groups),
            'info_credit': Obj(IMG_MENU['info_c'], 0, LIMBO, *groups),
            'return': Obj(IMG_MENU['return'], 206, LIMBO, *groups)
        }
        self._draw_guides()

    def _draw_guides(self):

        pos_x, pos_y = 195, 317

        for __item__ in list_guides_menu:

            draw_texts(MAIN_SCREEN, f'{__item__:^45}'.title().replace('_', ' '), pos_x, pos_y + 15, size=25)

            self._guides.append(pg.rect.Rect(pos_x, pos_y, 356, 65))

            pos_y += 90

    def _guide_new_game(self, pos_mouse):

        if self._guides[0].collidepoint(pos_mouse):

            self.check = 'new'
            self.class_menu = False
            click_sound.play()

    def _guide_load(self, pos_mouse):

        if self._guides[1].collidepoint(pos_mouse):

            self.check = 'load'
            self.class_menu = False
            click_sound.play()

    def _guide_options(self, pos_mouse):

        if self._guides[3].collidepoint(pos_mouse):

            self.check = 'options'
            self.class_menu = False
            click_sound.play()

    def _guide_credit(self, pos_mouse):

        if self._guides[2].collidepoint(pos_mouse):

            y, y_ = 0, 942
            self.BLOCK = True

        elif self._objects['return'].rect.collidepoint(pos_mouse):

            y, y_ = LIMBO, LIMBO
            self.BLOCK = False

        else:
            return 0

        self._objects['info_credit'].rect.y = y
        self._objects['return'].rect.y = y_
        click_sound.play()

    def _guide_quit(self, pos_mouse):

        if self._guides[4].collidepoint(pos_mouse):

            save_log()

    def _get_mouse_events_to_show_interactive(self, pos_mouse):

        __img_return__ = 'return'

        if self._objects['return'].rect.collidepoint(pos_mouse):
            __img_return__ = 'select_return'

        self._objects['return'].image = pg.image.load(IMG_MENU[__img_return__])

    def _select_guides(self, pos_mouse):

        __topleft__ = -1080, - 1080

        for __object__ in self._guides:

            if __object__.collidepoint(pos_mouse):

                __topleft__ = __object__.topleft

        self._objects['select'].rect.topleft = __topleft__

    def events_menu(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:

            self._guide_credit(pos_mouse)

            if not self.BLOCK:

                self._guide_new_game(pos_mouse)
                self._guide_load(pos_mouse)
                self._guide_options(pos_mouse)
                self._guide_quit(pos_mouse)

        if not self.BLOCK:

            self._select_guides(pos_mouse)

        self._get_mouse_events_to_show_interactive(pos_mouse)

    def update(self) -> None:

        draw_texts(MAIN_SCREEN, NAME_OF_THE_GAME, MAIN_SCREEN.get_width() / 2 - len(NAME_OF_THE_GAME) * 6.5, 100, size=25)
        draw_texts(MAIN_SCREEN, VERSION, MAIN_SCREEN.get_width() / 2 - len(VERSION), 980)

        if not self.BLOCK:

            self._draw_guides()
