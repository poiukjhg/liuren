# -*- coding: utf-8 -*- 
import fiveelements
import earthbranch
import skytrunk

class trishift:
	def __init__(self, upperlist, bottomlist):		
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()
		self.fe_instance = fiveelements.fiveelements()
		self.upperlist = upperlist
		self.bottomlist = bottomlist
		self.up_bottom_overcome = [0]*4
		self.bottom_attri = ['']*4
		self.upper_attri = ['']*4
	def build_trishift(self):	
		self.upper_attri = list(map(lambda x: self.eb_instance.attribute[self.eb_instance.names.index(x)], self.upperlist))	
		self.bottom_attri[0] = self.st_instance.attribute[self.st_instance.names.index(self.bottomlist[0])]
		self.bottom_attri[1:] = list(map(lambda x: self.eb_instance.attribute[self.eb_instance.names.index(x)], self.bottomlist[1:]))		
		print '  '.join(self.upper_attri[::-1])
		print '  '.join(self.bottom_attri[::-1])
		for index in range(4):
			if self.fe_instance.is_overcoming(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 1
			if self.fe_instance.is_overcomed(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 2	
		print '  '.join(list(map(lambda x:['  ', '贼','克'][x], self.up_bottom_overcome[::-1])))
		




