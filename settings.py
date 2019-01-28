# -*- coding:GBK -*-

class Settings():
	# 存储《外星人入侵》的所有设置 的类
	def __init__(self):
		'''初始化游戏的静态设置'''
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# 飞船设置
		self.ship_limit = 3
		
		# 子弹设置
		self.bullet_width = 1200
		self.bullet_height = 8
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10
		
		# 外星人设置
		self.fleet_drop_speed = 3
		
		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		
		# 外星人点数的提高速度
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()#初始化随游戏进行而变化的属性
		
	def initialize_dynamic_settings(self):
		'''初始化随游戏进行而变化的属性'''
		self.ship_speed_factor = 0.5
		self.bullet_speed_factor = 0.5
		self.alien_speed_factor = 0.5
		
		self.fleet_direction = 1	# 1表示向右, -1表示向左
		
		self.alien_points = 50	# 确保每次开始新游戏时, 这个值都会被重置
	
	def increase_speed(self):
		'''提高速度设置和外星人点数'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		#print(self.alien_points)	
		'''
		每当提高一个等级时,你都会在终端窗口看到一个外星人新的所值点数.
		确认点数在增不断加后,一定删除这条print语句,否则它可能会影响游戏性能以及分散玩家注意力
		
		
		
		
		
		
		# 初始化游戏外观设置, 屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		# 飞船的设置
		self.ship_speed_factor = 0.5
		self.ship_limit = 3
		# 子弹设置
		self.bullet_speed_factor = 0.5
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10	# 存储所允许的最大子弹数
		# 外星人设置
		self.alien_speed_factor = 0.5	# 设置外星人向右移动的速速
		self.fleet_drop_speed = 30	# 撞到屏幕边缘时向下移动的速度
		self.fleet_direction = 1	# fleet_direction为1表示向右移动，为-1表示向左移动
		'''
		
