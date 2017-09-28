#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helper
import re
import json


if __name__ == '__main__':
	# https://search.jd.com/Search?keyword=肌酸&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=肌酸&page=1&s=1&click=0
	# https://search.jd.com/Search?keyword=肌酸&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=肌酸&page=3&s=60&click=0
	# https://search.jd.com/Search?keyword=肌酸&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=肌酸&page=5&s=112&click=0
	# https://search.jd.com/Search?keyword=肌酸&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=肌酸&page=7&s=165&click=0
	pq = helper.get('https://search.jd.com/Search?keyword=肌酸&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=肌酸&page=1&s=1&click=0')
