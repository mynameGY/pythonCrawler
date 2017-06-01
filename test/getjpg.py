#coding=utf-8


import urllib
import re
import os

def  getHtml(url):
	page  = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(http://imgsrc.*?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	filepath=os.getcwd()+'\pythonimg' 
	for imgurl in imglist:
		temp= filepath+'\%s.jpg' % x 
		print "imgurl:"+imgurl + "    temp:" + temp
		urllib.urlretrieve(imgurl,temp) 
		
		x+=1
	return imglist

html = getHtml("http://tieba.baidu.com/p/5142218697")	
getImg(html)