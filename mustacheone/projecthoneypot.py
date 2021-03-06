#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2

sys.path.append('libs/')
from bs4 import BeautifulSoup

def get_header():
	rtn = """
###Project Honey Pot
[Project Honey Pot Website](http://www.projecthoneypot.org)

"""
	return rtn

def get_info(inquery):
	if inquery.__class__.__name__ == 'IP':
		html = get_html_ip(inquery.address)
		return get_elements(html)
	if inquery.__class__.__name__ == 'URL':
		rtn = """
Project Honey Pot does not let you query urls.

"""		
		return rtn
def get_html_ip(ip):
	html = urllib2.urlopen('http://www.projecthoneypot.org/ip_'+ip).read()	
	return html
def get_elements(html):
	soup =BeautifulSoup(html)
	theTag = soup.find("div", { "class" : "contain" })
	rtn = theTag.contents[3].get_text().encode('ascii', 'ignore').strip() + "\n"
	return rtn

# def get_html_url(url):
# 	rtn = """
# 	Project Honey Pot does not let you query urls.

# 	"""
# 	return rtn