# -*- coding:GBK -*-

import pygame.font	# Scoreboard����Ļ����ʾ�ı�
from pygame.sprite import Group	# ����Ҫ����һ���ɴ����飬���ǵ���Group���Ship��

from ship import Ship


'''��ʾ�÷���Ϣ����'''
class Scoreboard():
	def __init__(self, ai_settings, screen, stats):
		'''��ʼ����ʾ�÷��漰������'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		# ��ʾ�÷���Ϣʱʹ�õ���������
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)	# ʵ����һ���������
		
		# ׼��������ߵ÷ֺ͵�ǰ�÷ֵ�ͼ��
		self.prep_score()			# ��Ҫ��ʾ���ı�ת��Ϊͼ��
		self.prep_high_score()		# ����ߵ÷��뵱ǰ�÷ַֿ���ʾ
		self.prep_level()
		self.prep_ships()
		
	def prep_ships(self):
		# ��ʾ�����¶��ٷɴ�
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def prep_level(self):
		# ���ȼ�ת��Ϊ��Ⱦ��ͼ��
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
		# ���ȼ����ڵ÷��·�
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_high_score(self):
		# ����ߵ÷�ת��Ϊ��Ⱦͼ��
		high_score = round(self.stats.high_score, -1)	# ����ߵ÷�Բ���������10������
		high_score_str = "{:,}".format(high_score)
		self.high_score_image  = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)	# ������ߵ÷�����һ��ͼ��
		# ����ߵ÷ַ�����Ļ��������
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx	# �÷�ͼ��ˮƽ����
		self.high_score_rect.top = self.score_rect.top	# �� ����ߵ÷�ͼ�� ��top��������Ϊ ����ǰ�÷�ͼ�� ��top����
		
	def prep_score(self):
		'''���÷�ת��Ϊһ����Ⱦ��ͼ��'''
		rounded_score = int(round(self.stats.score, -1))# ע�ͼ���
		score_str = "{:,}".format(rounded_score)# �˴���ʹ����һ���ַ�����ʽ����ָ�����Python����ֵת��Ϊ�ַ���ʱ,��ǧ��λ�����붺��
		
		'''
		����round()ͨ����С����ȷ��С��������λ������λ�����ɵڶ������������ģ�
		Ȼ��������ָ��Ϊ��������˼�ǽ�Բ���������10��100��1000�����������˴���
		-1��ʾԲ����10������������洢��rounded_score ��
		PS��
			��Python2.7�У�round()���Ƿ���һ��С��ֵ���������ʹ��int()��ȷ��
			�÷�Ϊ�����������ʹ�õ���Python3������ʡ�Զ�int()�ĵ���
		'''
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)	# �ٽ�����ַ������ݸ�����ͼ���render(),��������Ļ����ɫ�Լ��ı���ɫ,��������Ļ��������ʾ�÷�
		
		# ���÷ַ�����Ļ���Ͻ�
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20	# �õ÷��ұ�Ե����Ļ�ұ�Ե���20����
		self.score_rect.top = 20	#  �õ÷��ϱ�Ե����Ļ�ϱ�ԵҲ���20����
		
	
		
	def show_score(self):
		'''����Ļ����ʾ�ȼ��͵÷�'''
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# ���Ʒɴ�
		self.ships.draw(self.screen)

