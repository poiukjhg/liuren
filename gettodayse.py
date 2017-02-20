# -*- coding: utf-8 -*- 
import earthbranch
import skytrunk
from xingli import SolarTerm as xingli
from datetime import datetime, timedelta
class todayse:
	def __init__(self, curtime = datetime.now()):
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()	
		nowtime = curtime.strftime('%Y-%m-%d %H:%M:%S')	
		print nowtime				
		self.year = nowtime[0:4]
		self.month = nowtime[4:5]
		self.day = nowtime[6:7]
		self.hour = nowtime[8:]
		print self.year
		self.jieqi = xingli().mytest(int(self.year))
		cday = curtime
		print self.jieqi[0]
		year_start = datetime.strptime(self.jieqi[0], '%Y-%m-%d %H:%M:%S') 		
		if cday < year_start:
			self.year = self.year-1		
			self.jieqi = xingli().mytest(int(self.year)	)
		print ' '.join(self.jieqi)	

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
		pass

if __name__ == "__main__":
    test = todayse()


