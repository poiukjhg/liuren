# -*- coding: utf-8 -*- 
import fiveelements
import earthbranch
import skytrunk

class trishift:
	def __init__(self, upperlist, bottomlist, skyplate, skygeneral):		
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()
		self.fe_instance = fiveelements.fiveelements()
		self.skyplate = skyplate
		self.skygeneral = skygeneral
		self.upperlist = upperlist
		self.bottomlist = bottomlist
		self.up_bottom_overcome = [0]*4
		self.bottom_attri = ['']*4
		self.upper_attri = ['']*4
		self.ninefunc = ''
		self.tri = ['']*3
	def build_trishift(self):	
		self.upper_attri = list(map(lambda x: self.eb_instance.attribute[self.eb_instance.names.index(x)], self.upperlist))	
		self.bottom_attri[0] = self.st_instance.attribute[self.st_instance.names.index(self.bottomlist[0])]
		self.bottom_attri[1:] = list(map(lambda x: self.eb_instance.attribute[self.eb_instance.names.index(x)], self.bottomlist[1:]))		
		#print '  '.join(self.upper_attri[::-1])
		#print '  '.join(self.bottom_attri[::-1])
		full_four = (len(self.upperlist)==len(set(self.upperlist)))
		if full_four == False:
			#别责
			if len(set(self.upperlist)) == 3:
				self.ninefunc = "别责"
				self.bieze()
				return self.tri
			#八专
			today_stoeb = self.st_instance.stoeb[self.st_instance.names.index(self.bottomlist[0])]	
			if self.bottomlist[2] == today_stoeb:
				self.ninefunc = "八专"
				self.bazhuan()
				return self.tri							
			#伏吟
			if self.upperlist[0] == self.eb_instance.names.index(today_stoeb): 
				self.ninefunc = "伏吟"
				self.fuyin()
				return self.tri			
			#反吟
			if self.upperlist[0] == self.eb_instance.opposited[self.eb_instance.names.index(today_stoeb)]:
				self.ninefunc = "反吟"
				self.fanyin()
				return self.tri			
		for index in range(4):
			#贼
			if self.fe_instance.is_overcoming(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 1
			#克	
			if self.fe_instance.is_overcomed(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 2	
			
		print '  '.join(list(map(lambda x:['  ', '贼','克'][x], self.up_bottom_overcome[::-1])))
		#重审
		if self.up_bottom_overcome.count(1) == 1 :
			self.ninefunc = "重审"
			self.haske(self.up_bottom_overcome.index(1))
			return self.tri	
		if 	self.up_bottom_overcome.count(1) > 1:
			stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome[index] == 1:					
					tmpyinyang = self.eb_instance.yinyang[self.eb_instance.names.index(self.upperlist[index])]
					print stattr +tmpyinyang
					if tmpyinyang == stattr:
						same_attr[index] = 1
			#比用			
			if same_attr.count(1) == 1:
				self.ninefunc = "比用"		
				self.haske(same_attr.index(1))	
			else:
			#涉害	
			#直接使用孟仲季的取法
				self.ninefunc = "涉害"	
				sehai = ['']*4
				tmpindex = -1
				for index in range(4):
					if self.up_bottom_overcome[index]  == 1:
						tmpstr = self.upperlist[index]
						ltmpindex = self.eb_instance.names.index(tmpstr)												
						ltmpindex = self.eb_instance.tricoop[ltmpindex].index(tmpstr)
						sehai[index] = ['孟', '仲', '季'][ltmpindex]
						print tmpstr+' 涉害 '+sehai[index]
				if sehai.count('孟') == 1:
					tmpindex = sehai.index('孟')
				elif sehai.count('仲') == 1:
					tmpindex = sehai.index('仲')
				elif sehai.count('季') == 1:
					tmpindex = sehai.index('季')										
				if 	tmpindex == -1:
					print '涉害 error'
					return None
				self.haske(tmpindex)		
			return self.tri
		#元首
		if self.up_bottom_overcome.count(2) == 1:
			self.ninefunc = "元首"
			self.haske(self.up_bottom_overcome.index(2))
			return self.tri			
		if self.up_bottom_overcome.count(2) >1:
			stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome[index] == 2:
					tmpyinyang = self.eb_instance.yinyang[self.eb_instance.names.index(self.upperlist[index])]
					print stattr +tmpyinyang
					if tmpyinyang == stattr:
						same_attr[index] = 1
			#比用			
			if same_attr.count(1) == 1:
				self.ninefunc = "比用"		
				self.haske(same_attr.index(1))	
			else:
			#涉害	
			#直接使用孟仲季的取法
				self.ninefunc = "涉害"
				sehai = ['']*4
				tmpindex = -1
				for index in range(4):
					if self.up_bottom_overcome[index]  == 2:
						tmpstr = self.upperlist[index]
						ltmpindex = self.eb_instance.names.index(tmpstr)												
						ltmpindex = self.eb_instance.tricoop[ltmpindex].index(tmpstr)
						sehai[index] = ['孟', '仲', '季'][ltmpindex]
						print tmpstr+' 涉害 '+sehai[index]
				if sehai.count('孟') == 1:
					tmpindex = sehai.index('孟')
				elif sehai.count('仲') == 1:
					tmpindex = sehai.index('仲')
				elif sehai.count('季') == 1:
					tmpindex = sehai.index('季')										
				if 	tmpindex == -1:
					print '涉害 error'
					return None
				self.haske(tmpindex)										
			return self.tri
		#遥克
		for index in range(4):
			#弹
			if self.fe_instance.is_overcoming(self.bottom_attri[0], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 3
			#蒿	
			if self.fe_instance.is_overcomed(self.bottom_attri[0], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 4
		print '  '.join(list(map(lambda x:['  ', '贼','克', '弹', '矢'][x], self.up_bottom_overcome[::-1])))				
		#弹射
		if self.up_bottom_overcome.count(3)==1:
			self.ninefunc = "遥克"
			self.yaoke(self.up_bottom_overcome.index(3))
			return self.tri	
		if self.up_bottom_overcome.count(3)>1:
			self.ninefunc = "遥克"
			stattr = self.bottom_attri[0]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome[index] == 3:
					if self.upper_attri[index] == stattr:
						same_attr[index] = 1		
			if same_attr.count(1) == 1:	
				self.yaoke(same_attr.index(1))			
			return self.tri	
		#蒿矢	
		if self.up_bottom_overcome.count(4) == 1:	
			self.ninefunc = "遥克"
			self.yaoke(self.up_bottom_overcome.index(4))
			return self.tri	
		if self.up_bottom_overcome.count(4)>1:
			self.ninefunc = "遥克"
			stattr = self.bottom_attri[0]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome[index] == 4:
					if self.upper_attri[index] == stattr:
						same_attr[index] = 1		
			if same_attr.count(1) == 1:	
				self.yaoke(same_attr.index(1))				
			return self.tri	
		#昴星
		self.angxing()
		return self.tri
	def out_res(self):
		print self.ninefunc
		print ' '.join(self.tri)

	def haske(self, index):		
		self.tri[0] = self.upperlist[index]
		self.tri[1] = self.skyplate[self.eb_instance.names.index(self.tri[0])]
		self.tri[2] = self.skyplate[self.eb_instance.names.index(self.tri[1])]
		self.out_res()
	def yaoke(self, index):
		self.out_res()
	def angxing(self):
		self.out_res()	
	def bazhuan(self):
		self.out_res()
	def bieze(self,):
		self.out_res()		
	def fuyin(self):
		self.out_res()
	def fanyin(self,):
		self.out_res()
	
