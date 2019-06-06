import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    print("Thanks for playing!")
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    #设置背景颜色
    bg_color = (230,230,230)

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用来存储子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏主循环
    while True:
        #检查玩家的输入
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            #更新飞船的位置
            ship.update()
            #更新子弹的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #更新外星人的位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #用更新后的位置来重新绘制屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
print("Bye Bye!")