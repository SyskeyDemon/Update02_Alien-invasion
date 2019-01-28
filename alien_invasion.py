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
	# ��ʼ��pygame�����ú���Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# ����Play��ť
	play_button = Button(ai_settings, screen, "Play")
	
	# ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	stats = GameStats(ai_settings)
	
	# ����һ�ҷɴ�
	ship = Ship(ai_settings, screen)
	
	# ����һ�����ڴ洢�ӵ��ı���
	bullets = Group()
	
	# ����һ�������˱���
	aliens = Group()
	
	# ����������Ⱥ
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# �����洢��Ϸͳ����Ϣ��ʵ��,�������Ƿ���
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)	# ���ü����Ӧ�¼��ķ���
		if stats.game_active:
			ship.update()  # ���ø��·ɴ��ķ���
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)	# ���ø�����Ļ�ķ���
				

run_game()
