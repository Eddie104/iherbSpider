#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helper
import re
import json

if __name__ == '__main__':
	# https://www.kaola.com/category/2893/2896.html?key=&pageSize=60&pageNo=2&sortfield=0&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&#topTab
	# https://www.kaola.com/category/2893/2896.html?key=&pageSize=60&pageNo=1&sortfield=0&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&#topTab
	# https://www.kaola.com/category/2893/2899.html?key=&pageSize=60&pageNo=2&sortfield=0&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&#topTab
	
	categoryCfg = {
		'weiShengSu': [2893, 2896, 1],
		'yuYou': [2893, 2899, 3],
		'jiaoSu': [2893, 2901, 6],
		'danbaiFen': [2893, 2900, 9],
		'puTaoZi': [2893, 2904, 2],
		'manYueMei': [2893, 2906, 1],
		'yeSuan': [2893, 2907, 2],
		'fengMiFengJiao': [2893, 2908, 4],
		'tie': [2893, 6621, 2],
		'gai': [2893, 6623, 4],
		'danbaiFenAnJiSuan': [2893, 6627, 9],
		'daDouYiHuangTong': [2893, 6629, 1],
		'daSuanTiQuWu': [2893, 6631, 1],
		'jiaoYuanDanBai': [2893, 6633, 2],
		'senLei': [2893, 6635, 3],
		'fengMi': [2893, 6637, 4],
		'naiJianCao': [2893, 6639, 1],
		'yueJianCao': [2893, 6643, 1],
		'fanQieHongSu': [2893, 6645, 1],
		'luHui': [2893, 6647, 1],
		'luanLingZhi': [2893, 6649, 1],
		'yinXing': [2893, 6655, 1],
		'yeHuangLanMei': [2893, 6657, 2],
		'DHA': [2893, 6962, 4],
		'weiGuLi': [2893, 6966, 4],
		'nanXingGongNeng': [2916, 3468, 3],
		'meiRongMeiyan': [2916, 3052, 5],
		'tiaoJieSanGao': [2916, 3061, 3],
		'guanJieYangHu': [2916, 3067, 2],
		'ganShengYangHu': [2916, 3094, 1],
		'jianFeiShouShen': [2916, 6600, 6],
		'tiaoJieMianYi': [2916, 3095, 11],
		'xinNaoBaoJian': [2916, 4479, 3],
		'ziBuYangSheng': [2916, 4485, 3],
		'guGeJianKang': [2916, 6606, 14],
		'baoHuShiLi': [2916, 6613, 2],
		'gaiShanShuiMian': [2916, 6616, 3],
		'gaiShanPinXue': [2916, 6698, 2],
		'huFaYangFa': [2916, 6749, 3],
		'jianFeiShouShen': [3401, 4489, 3],
		'shuHuanSuiYue': [3401, 3402, 3],
		'jiaoYuanDanBai': [3401, 3406, 1],
		'neiFenMi': [3401, 3408, 2],
		'nvXingJiaoSu': [3401, 3492, 4],
		'buQiYangXue': [3401, 4470, 1],
		'laoNianZiBuYangSheng': [3446, 3447, 3],
		'laoNianXinNaoBaoJian': [3446, 3452, 2],
		'laoNianTiaoJieSanGao': [3446, 3462, 2],
		'laoNianTiaoJieMainYi': [3446, 6690, 21],
		'laoNianGanShengHuYang': [3446, 6696, 1],
		'laoNianGuGeGuanJie': [3446, 6723, 5],
		'huGan': [3438, 3442, 1],
		'buGai': [3438, 6659, 3],
		'buGai': [3438, 6659, 3],
		'shengXian': [3438, 6665, 2],
		'maKa': [3438, 6675, 2]
	}

	result = helper.readFile('result.text')
	result = json.loads(result)
	# print(result)
	for category in categoryCfg.items():
		itemArr = []
		for page in xrange(1, category[1][2] + 1):
			url = 'https://www.kaola.com/category/%d/%d.html?key=&pageSize=60&pageNo=%d&sortfield=0&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&#topTab' % (category[1][0], category[1][1], page)
			pq = helper.get(url)
			# print(pq.html())
			html = pq.html()
			pattern = re.compile(r'>\d+</a>')
			arr = pattern.findall(html)
			arr = [int(x.replace('>', '').replace('</a', '')) for x in arr]
			arr = [x for x in arr if x >= 50]
			itemArr += arr
		print('%s => %d' % (category[0], len(itemArr)))
		result.append({category[0]: len(itemArr)})
		helper.writeFile(json.dumps(result), 'result.text')

