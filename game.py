import os
import pygame
import random
# import time


def intro(): # приветствие
    pygame.init()
    size = width, height = 1100, 619
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                running = False
            screen.fill((255, 80, 80))
            font = pygame.font.Font(None, 50)
            text = font.render('Добро пожаловать в игру "Съешь яблочко"!', 1, (0, 0, 0))
            screen.blit(text, (200, 300))
            font0 = pygame.font.Font(None, 50)
            text0 = font0.render('(щёлкните, чтобы продолжить.)', 1, (0, 0, 0))
            screen.blit(text0, (200, 350))
            pygame.display.flip()
    pygame.quit()


def plot():
    pygame.init()  # о чём игра
    size = width, height = 1100, 619
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                running = False
            screen.fill((141, 255, 132))
            font1 = pygame.font.Font(None, 50)
            text1 = font1.render('Сюжет игры.', 1, (0, 0, 0))
            screen.blit(text1, (450, 10))
            font2 = pygame.font.Font(None, 50)
            text2 = font2.render('Однажды голодная ящерица по имени Боб вышла погулять', 1, (0, 0, 0))
            screen.blit(text2, (0, 80))
            font3 = pygame.font.Font(None, 50)
            text3 = font3.render('на Поле Чудес. Как раз в тот момент наступило время обеда:', 1, (0, 0, 0))
            screen.blit(text3, (0, 130))
            font4 = pygame.font.Font(None, 50)
            text4 = font4.render('стали появляться в воздухе яблоки. Но не тут то было!', 1, (0, 0, 0))
            screen.blit(text4, (0, 180))
            font5 = pygame.font.Font(None, 50)
            text5 = font5.render('Злой маг Шайнханд наложил заклятие на это поле! Теперь', 1, (0, 0, 0))
            screen.blit(text5, (0, 230))
            font6 = pygame.font.Font(None, 50)
            text6 = font6.render('там стали появляться магические бомбы! Помогите', 1, (0, 0, 0))
            screen.blit(text6, (0, 280))
            font7 = pygame.font.Font(None, 50)
            text7 = font7.render('Бобу скушать хотя бы 30 яблок (можно и больше) и не', 1, (0, 0, 0))
            screen.blit(text7, (0, 330))
            font8 = pygame.font.Font(None, 50)
            text8 = font8.render('напороться на бомбу.', 1, (0, 0, 0))
            screen.blit(text8, (0, 380))
            font9 = pygame.font.Font(None, 50)
            text9 = font9.render('Если ящерица утолит свой голод, то заклятие с поля исчезнет,', 1, (0, 0, 0))
            screen.blit(text9, (0, 430))
            font10 = pygame.font.Font(None, 50)
            text10 = font10.render('а Шайнханд перестанет его [поле] терроризировать.', 1, (0, 0, 0))
            screen.blit(text10, (0, 480))
            font11 = pygame.font.Font(None, 50)
            text11 = font11.render('(щёлкните, чтобы продолжить.)', 1, (0, 0, 0))
            screen.blit(text11, (0, 530))
            pygame.display.flip()
    pygame.quit()


def rules():
    pygame.init()  # правила игры
    size = width, height = 1100, 619
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                running = False
            screen.fill((124, 124, 247))
            font12 = pygame.font.Font(None, 50)
            text12 = font12.render('Правила игры.', 1, (0, 0, 0))
            screen.blit(text12, (450, 10))
            font13 = pygame.font.Font(None, 50)
            text13 = font13.render('Вы играете за ящерицу. Она двигается за курсором, т. е.', 1, (0, 0, 0))
            screen.blit(text13, (0, 80))
            font14 = pygame.font.Font(None, 50)
            text14 = font14.render('Вы управляете ей лишь движениями мышки. Нужно собирать', 1, (0, 0, 0))
            screen.blit(text14, (0, 130))
            font15 = pygame.font.Font(None, 50)
            text15 = font15.render('яблоки, щёлкая по ним. На месте собранного яблока', 1, (0, 0, 0))
            screen.blit(text15, (0, 180))
            font16 = pygame.font.Font(None, 50)
            text16 = font16.render('появляется огрызок, а за него [яблоко] даётся очко.', 1, (0, 0, 0))
            screen.blit(text16, (0, 230))
            font17 = pygame.font.Font(None, 50)
            text17 = font17.render('Всё казалось бы просто, если бы не бомбы, которые', 1, (0, 0, 0))
            screen.blit(text17, (0, 280))
            font18 = pygame.font.Font(None, 50)
            text18 = font18.render('появляюся при каждом щелчке! Будьте ПРЕДЕЛЬНО', 1, (0, 0, 0))
            screen.blit(text18, (0, 330))
            font19 = pygame.font.Font(None, 50)
            text19 = font19.render('внимательны, чтобы не напороться на бомбы: они могут', 1, (0, 0, 0))
            screen.blit(text19, (0, 380))
            font20 = pygame.font.Font(None, 50)
            text20 = font20.render('накладываться друг на друга, закрывая при этом яблоко!', 1, (0, 0, 0))
            screen.blit(text20, (0, 430))
            font21 = pygame.font.Font(None, 50)
            text21 = font21.render('У Боба есть всего 3 жизни.', 1, (0, 0, 0))
            screen.blit(text21, (0, 480))
            font21 = pygame.font.Font(None, 50)
            text21 = font21.render('При взрыве бомбы у ящерицы отнимается жизнь, а очки', 1, (0, 0, 0))
            screen.blit(text21, (0, 530))
            font21 = pygame.font.Font(None, 50)
            text21 = font21.render('обнуляются. А для победы нужно 30 и более очков.', 1, (0, 0, 0))
            screen.blit(text21, (0, 580))
            pygame.display.flip()
    pygame.quit()


def farewell():
    pygame.init()  # напутствие
    size = width, height = 1100, 619
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                running = False
            screen.fill((255, 255, 0))
            pygame.draw.line(screen, (255, 0, 255), (0, 0), (1100, 619), 5)
            pygame.draw.line(screen, (255, 0, 255), (1100, 0), (0, 619), 5)
            pygame.draw.line(screen, (0, 255, 255), (0, 309), (1100, 309), 5)
            pygame.draw.line(screen, (0, 255, 255), (550, 0), (550, 619), 5)
            font22 = pygame.font.Font(None, 50)
            text22 = font22.render('Напутствие.', 1, (0, 0, 0))
            screen.blit(text22, (450, 10))
            font23 = pygame.font.Font(None, 50)
            text23 = font23.render('Желаем удачи в игре! Выполните задание,', 1, (0, 0, 0))
            screen.blit(text23, (250, 245))
            font24 = pygame.font.Font(None, 50)
            text24 = font24.render('проучите злого Шайнханда!', 1, (0, 0, 0))
            screen.blit(text24, (250, 295))
            font25 = pygame.font.Font(None, 50)
            text25 = font25.render('(щёлкните, чтобы начать игру).', 1, (0, 0, 0))
            screen.blit(text25, (250, 345))
            pygame.display.flip()
    pygame.quit()


def game():
    pygame.init()
    size = width, height = 1100, 619
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        image = image.convert_alpha()

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image

    class Apple(pygame.sprite.Sprite):
        image = load_image("apple.png")
        image0 = load_image("hrum.png")

        def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно!!!
            super().__init__(group)
            self.image = Apple.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - 50)
            self.rect.y = random.randrange(height - 50)

        def update(self):
            self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)

        def get_event(self, event, q, w):
            if self.rect.collidepoint(event.pos):
                self.image = self.image0
                q += 1
                w = True
            else:
                w = False
            return q, w

    class Bomb(pygame.sprite.Sprite):
        image = load_image("bomb.png")
        image_boom = load_image("boom.png")

        def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно !!!
            super().__init__(group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - 50)
            self.rect.y = random.randrange(height - 51)

        # Поручим бомбочке получать событие и взрываться (поменяем картинку)
        def get_event(self, event, q, r):
            if self.rect.collidepoint(event.pos):
                self.image = self.image_boom
                q = 0
                r -= 1
            return q, r

    class Star_1(pygame.sprite.Sprite):
        image = load_image("star_1.png")

        def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно!!!
            super().__init__(group)
            self.image = Star_1.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - 50)
            self.rect.y = random.randrange(height - 50)

        def update(self):
            self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)

    class Star_2(pygame.sprite.Sprite):
        image = load_image("star_2.png")

        def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно!!!
            super().__init__(group)
            self.image = Star_2.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - 50)
            self.rect.y = random.randrange(height - 50)

        def update(self):
            self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)

    def draw():
        screen.fill((65, 242, 46), pygame.Rect(0, 588, 1100, 619))
        pygame.draw.circle(screen, (255, 204, 0), (1000, 24), 100)

    q = 0
    r = 3
    w = False
    apple0 = pygame.sprite.Group()
    for _ in range(1):
        Apple(apple0)
    bomb0 = pygame.sprite.Group()
    for _ in range(1):
        Bomb(bomb0)
    lizard0 = pygame.sprite.Group()
    lizard = pygame.sprite.Sprite()
    lizard.image = load_image("lizard.png")
    lizard.rect = lizard.image.get_rect()
    lizard.mask = pygame.mask.from_surface(lizard.image)
    lizard0.add(lizard)
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 100), 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or r == 0:
                running = False
            if event.type == pygame.MOUSEMOTION:
                lizard.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in apple0:
                    x.get_event(event, q, w)
                    q = x.get_event(event, q, w)[0]
                    w = x.get_event(event, q, w)[1]
                for y in bomb0:
                    y.get_event(event, q, r)
                    q = y.get_event(event, q, r)[0]
                    r = y.get_event(event, q, r)[1]
                if w:
                    Apple(apple0)
                Bomb(bomb0)
            screen.fill((126, 214, 246))
            draw()
            lizard0.draw(screen)
            apple0.draw(screen)
            bomb0.draw(screen)
            b = 'Очки: {}'.format(str(q))
            c = 'Жизни: {}'.format(str(r))
            font_score = pygame.font.Font(None, 50)
            text_score = font_score.render(b, 1, (0, 0, 0))
            screen.blit(text_score, (10, 10))
            font_life = pygame.font.Font(None, 50)
            text_life = font_life.render(c, 1, (0, 0, 0))
            screen.blit(text_life, (900, 10))
            pygame.display.flip()
    pygame.quit()

    if q >= 10:  # выйгрыш
        pygame.init()
        a = 'Вы набрали {} очков(-а, -о).'.format(str(q))
        size = width, height = 1100, 619
        screen = pygame.display.set_mode(size)
        running = True
        stars_1 = pygame.sprite.Group()
        stars_2 = pygame.sprite.Group()
        for _ in range(q):
            Star_1(stars_1)
        for _ in range(q):
            Star_2(stars_2)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                screen.fill((255, 255, 255))
                stars_1.draw(screen)
                stars_2.draw(screen)
                font01 = pygame.font.Font(None, 50)
                text01 = font01.render('Поздравляем с победой!', 1, (0, 0, 0))
                screen.blit(text01, (300, 200))
                font02 = pygame.font.Font(None, 50)
                text02 = font02.render(a, 1, (0, 0, 0))
                screen.blit(text02, (300, 300))
                pygame.display.flip()
        pygame.quit()

    if r == 0:  # пройгрыш
        pygame.init()
        size = width, height = 500, 500
        screen = pygame.display.set_mode(size)
        all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image("gameover_2.jpg")
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)
        running = True
        kek = -600
        v = 200
        fps = 10
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                while kek < 10:
                    sprite.rect.topleft = (kek, 0)
                    screen.fill((0, 0, 0))
                    all_sprites.draw(screen)
                    kek += v / fps
                    clock.tick(fps)
                    pygame.display.flip()
        pygame.quit()


def main():
    intro()
    plot()
    rules()
    farewell()
    game()


main()
