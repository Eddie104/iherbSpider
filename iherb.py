#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helper
import re
import json

result = []

class User(object):
	"""docstring for User"""
	def __init__(self, name, numTopic, numPost, numPoint, title):
		super(User, self).__init__()
		self.name = name
		self.numTopic = numTopic
		self.numPost = numPost
		self.numPoint = numPoint
		self.title = title

	def toCSV(self):
		return '%s,%s,%s,%s,%s' % (self.name, self.numTopic, self.numPost, self.numPoint, self.title)

def hasUser(name):
	global result
	for u in result:
		if u.name == name:
			return True
	return False

def fetchPage(url, curPage = 1, totalPage = None):
	global result
	pq = helper.get(url + '&page=' + str(curPage))
	aArr = pq('.xg2>table>th>p>a')
	bArr = pq('.xg2>table>td>p>a')
	cArr = pq('p>em>a')
	nameArr = pq('.authi>a.xw1')
	index = 0
	for name in nameArr:
		name = name.text
		if not hasUser(name):
			numTopic = aArr[index * 2].text
			numPost = aArr[index * 2 + 1].text
			if numPost == None:
				numPost = aArr[index * 2 + 1].find('span').text
			numPoint = bArr[index].text
			if numPoint == None:
				numPoint = bArr[index].find('span').text
			title = cArr[index].text
			print(numTopic, numPost, numPoint)
			result.append(User(name, numTopic, numPost, numPoint, title))
		index += 1

	if not totalPage:
		try:
			totalPage = int(pq('.pgt label span').text().split(' ')[1])	
		except Exception as e:
			totalPage = 1

	if curPage < totalPage:
		fetchPage(url, curPage + 1, totalPage)

if __name__ == '__main__':
	csv = helper.readFile('iherb.csv')
	if csv != '':
		rowArr = csv.split('\n')
		for row in xrange(1, len(rowArr)):
			a = row.split(',')
			result.append(User(a[0], a[1], a[2], a[3], a[4]))

	for page in xrange(1, 36):
		url = 'https://bbs.iherb.com/forum.php?mod=forumdisplay&fid=61&filter=author&orderby=dateline&page=' + str(page)
		pq = helper.get(url)
		topicAArr = pq('.xst')
		for topic in topicAArr:
			fetchPage(topic.get('href'))
			csv = 'name,numTopic,numPost,numPoint,title\n'
			for u in result:
				csv += u.toCSV() + '\n'
			helper.writeFile(csv.encode('utf-8'), 'iherb.csv')