# -*- coding: utf-8 -*- 
class output_results():
	def __init__(self, skytrunk, earthbranch, monthgeneral, fortell_hour, skyplate, skygeneral, fourclass_buttom, fourclass_upper):
		self.skytrunk = skytrunk
		self.earthbranch = earthbranch
		self.fortell_hour = fortell_hour
		self.monthgeneral = monthgeneral
		self.skyplate = skyplate
		self.skygeneral = skygeneral
		self.fourclass_upper = fourclass_upper
		self.fourclass_buttom = fourclass_buttom

	#	self.trisshift = trisshift
	def output(self):
		print self.skytrunk+self.earthbranch+'日'+self.fortell_hour+'时'+self.monthgeneral+'将'
		print '    '+self.skygeneral[5]+'  '+self.skygeneral[6]+'  '+self.skygeneral[7]+'  '+self.skygeneral[8]+'  '	
		print '    '+self.skyplate[5]+'  '+self.skyplate[6]+'  '+self.skyplate[7]+'  '+self.skyplate[8]+' '	
		print '  '+self.skygeneral[4]+self.skyplate[4]+'          '+self.skyplate[9]+self.skygeneral[9]
		print '  '+self.skygeneral[3]+self.skyplate[3]+'          '+self.skyplate[10]+self.skygeneral[10]
		print '    '+self.skyplate[2]+'  '+self.skyplate[1]+'  '+self.skyplate[0]+'  '+self.skyplate[11]+' '			
		print '    '+self.skygeneral[2]+'  '+self.skygeneral[1]+'  '+self.skygeneral[0]+'  '+self.skygeneral[11]+'  '	
		print ''
		print '四课：'
		tmpgeneral = ['','','','']
		for index in range(4):
			tmpgeneral[index] = self.skygeneral[self.skyplate.index(self.fourclass_upper[3-index])]
		print tmpgeneral[0]+'  '+tmpgeneral[1]+'  '+tmpgeneral[2]+'  '+tmpgeneral[3]+'  '
		print self.fourclass_upper[3]+'  '+self.fourclass_upper[2]+'  '+self.fourclass_upper[1]+'  '+self.fourclass_upper[0]+'  '
		print self.fourclass_buttom[3]+'  '+self.fourclass_buttom[2]+'  '+self.fourclass_buttom[1]+'  '+self.fourclass_buttom[0]+'  '
