# -*- coding:GBK -*-

import sys
import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
	# 初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
	
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	
	# 创建一个用于存储子弹的编组
	bullets = Group()
	
	# 创建一个外星人编组
	aliens = Group()
	
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# 创建存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)	# 调用检测响应事件的方法
		if stats.game_active:
			ship.update()  # 调用更新飞船的方法
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)	# 调用更新屏幕的方法
				

run_game()
