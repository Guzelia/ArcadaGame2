import pygame
import sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mrigth = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mrigth = False
            if event.key == pygame.K_LEFT:
                gun.mleft  = False

def update(bg_color, screen, stats, sc, gun, inos,  bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, inos, bullets):
    """обновление позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,inos, True, True)
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)





def gun_kill(stats, screen, gun, inos, bullets):
    """"""
    if stats.guns_left >0:
        stats.guns_left -= 1
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game =False
        sys.exit()

def update_inos(stats, screen, gun, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)
    inos_chek(stats, screen, gun, inos, bullets)


def inos_chek(stats, screen, gun, inos, bullets):
    """"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom > screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break

def create_army(screen, inos):

    """ создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = (700 - 2 * ino_width) // ino_width
    ino_heigth = ino.rect.height
    number_ino_y = (800 - 200 - 2 * ino_heigth) // ino_heigth

    for row in range(number_ino_y - 3):

        for t in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width * (1 + t)
            ino.y = ino_heigth * (1 + row)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row
            inos.add(ino)

