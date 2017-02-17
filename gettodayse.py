# -*- coding: utf-8 -*- 
import earthbranch
import skytrunk
class todayse:
	def __init__(self, now):
		self.year = now[0:3]
		self.month = now[4:5]
		self.day = now[6:7]
		self.hour = now[8:]
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()
	def get_year(self):
		self.ystmpindex = int(self.year[-1])
		self.ystmpindex = self.ystmpindex -3
		if self.ystmpindex<0:
			self.ystmpindex = self.ystmpindex+10		
		self.yebtmpindex = int(self.year)
		self.yebtmpindex = (self.yebtmpindex-3)%12
		return self.st_instance.names[self.yebtmpindex]+self.eb_instance.names[self.yebtmpindex]			
	def get_month(self):
		self.mstmpindex = (self.ystmpindex*2+int(self.month))%10
		self.mebtmpindex = (int(self.month)+12-2)%12
		return self.st_instance.names[self.mstmpindex]+self.eb_instance.names[self.mebtmpindex]	
	def get_day(self):
		
