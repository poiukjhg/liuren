# -*- coding: utf-8 -*- 
import fiveelements
import earthbranch
import skytrunk

class trishift:
	def __init__(self, upperlist, bottomlist, skyplate, skygeneral, skyplate_st):		
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()
		self.fe_instance = fiveelements.fiveelements()
		self.skyplate = skyplate
		self.skyplate_st = skyplate_st
		self.skygeneral = skygeneral
		self.upperlist = upperlist
		self.bottomlist = bottomlist
		self.up_bottom_overcome = [0]*4
		self.up_bottom_overcome_yao = [0]*4
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
		for index in range(4):
			#贼
			if self.fe_instance.is_overcoming(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 1
			#克	
			if self.fe_instance.is_overcomed(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 2	
			
		#print '  '.join(list(map(lambda x:['  ', '贼','克'][x], self.up_bottom_overcome[::-1])))
		today_stoeb = self.st_instance.stoeb[self.st_instance.names.index(self.bottomlist[0])]	
		#print '日干寄宫'+today_stoeb		
		full_four = (len(self.upperlist)==len(set(self.upperlist)))		
		if full_four == False:
			#print '不备'						
			#伏吟
			if self.upperlist[0] == today_stoeb: 
				self.ninefunc = "伏吟"
				self.fuyin()
				return self.tri					
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
					#print stattr +tmpyinyang
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
						if index == 0:
							tmpstr = today_stoeb
						else:
							tmpstr = self.bottomlist[index]						
						ltmpindex = self.eb_instance.names.index(tmpstr)												
						ltmpindex = self.eb_instance.tricoop[ltmpindex].index(tmpstr)
						sehai[index] = ['孟', '仲', '季'][ltmpindex]
						#print self.bottomlist[index]+' 涉害 '+sehai[index]
				if sehai.count('孟') >= 1:
					tmpindex = sehai.index('孟')
				elif sehai.count('仲') >= 1:
					tmpindex = sehai.index('仲')
				elif sehai.count('季') >= 1:
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
					#print stattr +tmpyinyang
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
						if index == 0:
							tmpstr = today_stoeb
						else:
							tmpstr = self.bottomlist[index]	
						ltmpindex = self.eb_instance.names.index(tmpstr)												
						ltmpindex = self.eb_instance.tricoop[ltmpindex].index(tmpstr)
						sehai[index] = ['孟', '仲', '季'][ltmpindex]
						#print self.upperlist[index]+' 涉害 '+sehai[index]
				if sehai.count('孟') >= 1:
					tmpindex = sehai.index('孟')
				elif sehai.count('仲') >= 1:
					tmpindex = sehai.index('仲')
				elif sehai.count('季') >= 1:
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
				self.up_bottom_overcome_yao[index] = 3
			#蒿	
			if self.fe_instance.is_overcomed(self.bottom_attri[0], self.upper_attri[index]):
				self.up_bottom_overcome_yao[index] = 4
		#print '  '.join(list(map(lambda x:['  ', '贼','克', '弹', '矢'][x], self.up_bottom_overcome_yao[::-1])))
		#蒿矢	
		if self.up_bottom_overcome_yao.count(4) == 1:	
			self.ninefunc = "遥克"
			self.haske(self.up_bottom_overcome_yao.index(4))
			return self.tri	
		if self.up_bottom_overcome_yao.count(4)>1:
			self.ninefunc = "遥克"
			stattr = self.bottom_attri[0]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome_yao[index] == 4:
					if self.upper_attri[index] == stattr:
						same_attr[index] = 1		
			if same_attr.count(1) == 1:	
				self.haske(same_attr.index(1))				
			return self.tri	
		#弹射
		if self.up_bottom_overcome_yao.count(3)==1:
			self.ninefunc = "遥克"
			self.haske(self.up_bottom_overcome_yao.index(3))
			return self.tri	
		if self.up_bottom_overcome_yao.count(3)>1:
			self.ninefunc = "遥克"
			stattr = self.bottom_attri[0]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome_yao[index] == 3:
					if self.upper_attri[index] == stattr:
						same_attr[index] = 1		
			if same_attr.count(1) == 1:	
				self.haske(same_attr.index(1))			
			return self.tri	
		if full_four == False:
			#别责
			if len(set(self.upperlist)) == 3:
				self.ninefunc = "别责"
				self.bieze()
				return self.tri
			#八专						
			if self.bottomlist[2] == today_stoeb:
				self.ninefunc = "八专"
				self.bazhuan()
				return self.tri	
			#反吟
			if self.upperlist[0] == self.eb_instance.opposited[self.eb_instance.names.index(today_stoeb)]:
				self.ninefunc = "反吟"
				self.fanyin()
				return self.tri	
		#昴星
		else:			
			self.angxing()
		return self.tri
	def out_res(self):
		#print self.ninefunc
		#print ' '.join(self.tri)
		#map(lambda x: self.skyplate_st[self.skyplate.index(x)]+x , self.tri)
		#tmpl = list(map(lambda x: self.skyplate_st[self.skyplate.index(x)]+x+"  "+ self.skygeneral[self.skyplate.index(x)], self.tri))
		tmpl = list(map(lambda x: self.skyplate_st[self.skyplate.index(x)]+x+"  "+ self.skygeneral[self.skyplate.index(x)], self.tri))
		relation = ['']*3
		for index  in range(3):
			tmpattri = self.eb_instance.attribute[self.eb_instance.names.index(self.tri[index])]		
			if self.fe_instance.is_overcoming(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '财'
			elif self.fe_instance.is_overcomed(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '官'				
			elif self.fe_instance.is_child(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '子'				
			elif self.fe_instance.is_parent(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '父'				
			else:
				relation[index] = '比'

		print "\n\r三传"
		print relation[0]+"  "+tmpl[0]
		print relation[1]+"  "+tmpl[1]
		print relation[2]+"  "+tmpl[2]
		print "\n\r详解"
		file_name = "./output/"+self.bottomlist[0]+self.bottomlist[2]+"日干上"+self.upperlist[0]+".ini"
		#print file_name
		try:
			f = open(file_name, "r")	
		except IOError:
			print "Error: open  %s file error!" % file_name
		else:  
			tmpline = f.read()
			print tmpline
			f.close()
				
	def haske(self, index):		
		self.tri[0] = self.upperlist[index]
		self.tri[1] = self.skyplate[self.eb_instance.names.index(self.tri[0])]
		self.tri[2] = self.skyplate[self.eb_instance.names.index(self.tri[1])]
		self.out_res()
	def angxing(self):
		stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
		#虎视转蓬
		if stattr == '阳':
			self.tri[0] = self.skyplate[9]
			self.tri[1] = self.upperlist[2]
			self.tri[2] = self.upperlist[0]
		#冬蛇掩目	
		else:	
			self.tri[0] = self.eb_instance.names[self.upperlist.index('酉')]
			self.tri[1] = self.upperlist[0]
			self.tri[2] = self.upperlist[2]			
		self.out_res()	
	def bieze(self):
		stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
		if stattr == '阳':
			st_coop = self.st_instance.cooperation[self.st_instance.names.index(self.bottomlist[0])]
			self.tri[0] = self.skyplate[self.skyplate_st.index(st_coop)]
		else:
			co_l = self.eb_instance.tricoop[self.eb_instance.names.index(self.bottomlist[2])]
			self.tri[0] = co_l[(co_l.index(self.bottomlist[2])+1)%3]
		self.tri[1] = self.upperlist[0]
		self.tri[2] = self.upperlist[0]			
		self.out_res()		
	def fuyin(self):
		#不虞
		if self.up_bottom_overcome[0] != 0:
			self.tri[0] = self.upperlist[0]
			self.tri[1] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[0])]
			self.tri[2] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[1])]
		else:
			stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]				
			if stattr == '阳':	
				tmpstr = self.upperlist[0]		
			else:
				tmpstr = self.upperlist[2]
			if tmpstr != self.eb_instance.xing[self.eb_instance.names.index(tmpstr)]:	
			#自任				
			#自信
				self.tri[0] = tmpstr
				self.tri[1] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[0])]
				self.tri[2] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[1])]	
			#杜传
			else:
				self.tri[0] = tmpstr
				if stattr == '阳':	
					self.tri[1] = self.upperlist[2]		
				else:
					self.tri[1] = self.upperlist[0]	
				if 	self.tri[1] == self.eb_instance.xing[self.eb_instance.names.index(self.tri[1])]:
					self.tri[2] = self.eb_instance.opposited[self.eb_instance.names.index(self.tri[1])]
				else:	
					self.tri[2] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[1])]

		self.out_res()
	def fanyin(self):
		#无亲
		self.tri[0] = self.eb_instance.tricoop[self.eb_instance.names.index(self.upperlist[2])][0]
		self.tri[1] = self.upperlist[0]
		self.tri[2] = self.upperlist[2]			
		self.out_res()
	def bazhuan(self):
		if stattr == '阳':
			self.tri[0] = self.skyplate[(self.skyplate.index(self.upperlist[0])+3)%12]
		else:
			self.tri[0] = self.skyplate[(self.skyplate.index(self.upperlist[0])-3+12)%12]	
		self.tri[1] = self.upperlist[0]
		self.tri[2] = self.upperlist[0]			
		self.out_res()		
	
