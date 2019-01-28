# -*- coding:GBK -*-

import pygame.font	# Scoreboard在屏幕上显示文本
from pygame.sprite import Group	# 鉴于要创建一个飞船编组，我们导入Group类和Ship类

from ship import Ship


'''显示得分信息的类'''
class Scoreboard():
	def __init__(self, ai_settings, screen, stats):
		'''初始化显示得分涉及的属性'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)	# 实例化一个字体对象
		
		# 准备包含最高得分和当前得分的图像
		self.prep_score()			# 将要显示的文本转换为图像
		self.prep_high_score()		# 将最高得分与当前得分分开显示
		self.prep_level()
		self.prep_ships()
		
	def prep_ships(self):
		# 显示还余下多少飞船
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def prep_level(self):
		# 将等级转换为渲染的图像
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
		# 将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_high_score(self):
		# 将最高得分转换为渲染图像
		high_score = round(self.stats.high_score, -1)	# 将最高得分圆整到最近的10整数倍
		high_score_str = "{:,}".format(high_score)
		self.high_score_image  = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)	# 根据最高得分生成一幅图像
		# 将最高得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx	# 得分图像水平居中
		self.high_score_rect.top = self.score_rect.top	# 将 “最高得分图像” 的top属性设置为 “当前得分图像” 的top属性
		
	def prep_score(self):
		'''将得分转换为一副渲染的图像'''
		rounded_score = int(round(self.stats.score, -1))# 注释见下
		score_str = "{:,}".format(rounded_score)# 此处，使用了一个字符串格式设置指令，它让Python将数值转换为字符串时,在千分位处插入逗号
		
		'''
		函数round()通常让小数精确到小数点后多少位，其中位数是由第二个参数决定的，
		然而，这里指定为负数，意思是将圆整到最近的10、100、1000等整数倍，此处的
		-1表示圆整到10倍，并将结果存储到rounded_score 中
		PS：
			在Python2.7中，round()总是返回一个小数值，因此我们使用int()来确保
			得分为整数，如果你使用的是Python3，可以省略对int()的调用
		'''
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)	# 再将这个字符串传递给创建图像的render(),并传递屏幕背景色以及文本颜色,可以在屏幕上清晰显示得分
		
		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20	# 让得分右边缘与屏幕右边缘相距20像素
		self.score_rect.top = 20	#  让得分上边缘与屏幕上边缘也相距20像素
		
	
		
	def show_score(self):
		'''在屏幕上显示等级和得分'''
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# 绘制飞船
		self.ships.draw(self.screen)

