"""
File: web_crawler_avg.py
Name:
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	header = {
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('div', {'class': 'sc-9ab53865-0 bIaPYM sc-43986a27-2 bvCMEK cli-ratings-container'})
	print(tags)
	#########################
	#                       #
	#         TODO:         #
	#                       #
	#########################
	# total = 0
	# for tag in tags:
	# 	# print(tag.span['aria-label'][13:16])
	# 	# print('-'*44)
	# 	total += float(tag.span['aria-label'][13:16])
	# print(total/250)


if __name__ == '__main__':
	main()
