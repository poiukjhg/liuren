# -*- coding: utf-8 -*- 
import earthbranch
import skytrunk
from xingli import SolarTerm as xingli
from datetime import datetime, timedelta
class todayse:
	def __init__(self, curtime = datetime.now()):
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()	
		self.nowtime = curtime.strftime('%Y-%m-%d %H:%M:%S')			
		self.year = self.nowtime[0:4]
		self.month = self.nowtime[5:6]
		self.day = self.nowtime[8:9]
		self.hour = self.nowtime[11:]
		self.jieqi = xingli().mytest(int(self.year))
		cday = curtime
		year_start = datetime.strptime(self.jieqi[0], '%Y-%m-%d %H:%M:%S') 		
		if cday < year_start:
			self.year = str(int(self.year)-1)
			self.jieqi = xingli().mytest(int(self.year)	)
		print self.nowtime	
		print ' '.join(self.jieqi)
	def get_year(self):
		self.ystmpindex = int(self.year[-1])
		self.ystmpindex = self.ystmpindex -3
		if self.ystmpindex<0:
			self.ystmpindex = self.ystmpindex+10		
		self.yebtmpindex = int(self.year)
		self.yebtmpindex = (self.yebtmpindex-3)%12
		return self.st_instance.names[self.ystmpindex-1]+self.eb_instance.names[self.yebtmpindex-1]			
	def get_month(self):
		self.mstmpindex = (self.ystmpindex*2+int(self.month))%10
		lasttmptime = datetime.strptime(self.year+'-01-01 01:01:59', '%Y-%m-%d %H:%M:%S')
		nowtt = datetime.strptime(self.nowtime, '%Y-%m-%d %H:%M:%S')

		for index in range(12):
			tmptime = datetime.strptime(self.jieqi[index*2], '%Y-%m-%d %H:%M:%S')
			#print lasttmptime.strftime('%Y-%m-%d %H:%M:%S')+" "+self.nowtime+" "+tmptime.strftime('%Y-%m-%d %H:%M:%S')
			if nowtt > lasttmptime and nowtt<tmptime:
				print index
				break
			lasttmptime = tmptime 
		self.mebtmpindex = (index+2)%12
		return self.st_instance.names[self.mstmpindex]+self.eb_instance.names[self.mebtmpindex-1]	
	def get_day(self):
		pass

if __name__ == "__main__":
    test = todayse(datetime.strptime('2017-01-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
    print "年"+test.get_year()
    print "月"+test.get_month()
    test = todayse()
    print "年"+test.get_year()
    print "月"+test.get_month()


