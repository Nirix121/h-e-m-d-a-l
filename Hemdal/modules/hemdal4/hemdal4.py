import requests
import os
import time
from bs4 import BeautifulSoup as BS

RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'

def get_html(url):
	return requests.get(url).text

def parse_ua(tutilka):
	soup = BS(tutilka, 'html.parser')
	for date in soup.findAll('td'):
		content = date.getText().split('  ')
		for g in content:
			if g == '':
				pass
			elif '\n' in g:
				g = g.replace("\n", "")
			else:
				print(f'{CYAN}[{RED}*{CYAN}] {GREEN}'+g)

print ('''
    
[1] Car Scan (UK)   [2] Phone Scan  [3] IP Scan
[4] TorrentScan     [5] Parse Proxy  [6] Avito Scan
                    [7] BSSID Locate
[!] Run with proxy or VPN.

''')

while True:
	shell = input(f'Choose number: ')
	if shell == '1':
		num = input(f'Car-Number: ')
		parse_ua(get_html('https://baza-gai.com.ua/nomer/' + num))
	elif shell == '2':
		phone = input(f'Phone Number: ')
		try:
			response = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone)
			data = response.json()
			user_country = data[ 'country' ][ 'english' ]
			user_id = data[ 'country' ][ 'id' ]
			user_location = data[ 'country' ][ 'location' ]
			user_city = data[ 'capital' ][ 'english' ]
			user_lat = data[ 'capital' ][ 'latitude' ]
			user_log = data[ 'capital' ][ 'longitude' ]
			user_post = data[ 'capital' ][ 'post' ]
			user_oper = data[ '0' ][ 'oper' ]
			uty = requests.get("https://api.whatsapp.com/send?phone="+phone)
			if uty.status_code==200:
				utl2 = "https://api.whatsapp.com/send?phone="+phone
			else:
				utl2 = 'Not founded!'
			userr_all_info = f'[*] Country: {str(user_country)}\n[*] ID: {str(user_id)}\n[*] Location: str(user_location)\n[*] City: {str(user_city)}\n[*] Latitude: {str(user_lat)}\n[*] Longitude: {str(user_log)}\n[*] Index post: {str(user_post)}\n[*] Operator: {str(user_oper)}'
			num_name = []
			phone_ow = requests.get(f'https://phonebook.space/?number=%2B{phone}').text
			content = BS(phone_ow, 'html.parser').find('div', class_='results')
			for i in content.find_all('li'):
				num_name.append(i.text.strip())
			name = ', '.join(num_name)
			user_all_info = f"""
35m-===[Operator Info]===-
{userr_all_info}
[35m-===[Social Networks]===-
WhatsApp: {utl2}
[35m-===[Personal Info]===-
Possible names: {name}
	"""
			print(user_all_info)
		except:
			print(f'Error 003')
	elif shell == '3':
		query = input(f'Ip For Scan: ')
		try:
			r = requests.get(f'http://ip-api.com/json/{query}').json()
			print(f'[*] Country: {r["country"]}\n[*] CountryCode: {r["countryCode"]}\n[*] Region {r["region"]}\n[*] Region Name: {r["regionName"]}\n[*] City: {r["city"]}\n[*] Zip: {r["zip"]}\n[*] Latinude: {r["lat"]}\n[*] Longitude: {r["lon"]}\n[*] Timezone: {r["timezone"]}\n[*] ISP: {r["isp"]}\n[*] Org: {r["org"]}\n[*] As: {r["as"]} ')
		except:
			print(f'Error 004 ')
	elif shell == '4':
		query = input(f'Ip For Scan: ')
		target_ip = query
		try:
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36","Connection": "keep-alive","Host": "iknowwhatyoudownload.com","Referer": "https://iknowwhatyoudownload.com"}
			page = requests.get("https://iknowwhatyoudownload.com/ru/peer/?ip=" + target_ip, headers=headers)
			soup = BS(page.content, "html.parser")
			table = soup.find(class_="table").find("tbody")
			torrents = table.find_all("tr")
			for torrent in torrents:
				first, last = torrent.find_all(class_="date-column")
				first, last = first.text, last.text
				category = torrent.find(class_="category-column").text
				name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
				size = torrent.find(class_="size-column").text
				print(f'Использовано первый раз: {first}, использовано последний раз: {last}, тип торента: {category}, название торента: {name}, размер торента: {size}\n')
		except:
			print(f'Error 005')
	elif shell == '5':
		res1 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes')
		print(f'Your proxy, ser:\n' + '\n'.join(res1.text.split('\r\n')))
	elif shell == '6':
		phone = input(f'Phone Number:  ')
		try:
			page = requests.get('https://mirror.bullshit.agency/search_by_phone/'+phone)
			soup = BS(page.text, 'html.parser')
			classsell=soup.find(class_='media-heading')
			namesell= soup.find_all('h4')
			for classsell in namesell:
				print(f"Name: ", classsell.text)
			classtext = soup.find(class_='text-muted')
			nametext = soup.find_all('span')
			for classtext in nametext:
				print(f"Address and data: ", classtext.text)
		except:
			print(f' Error 006')
	elif shell == '7':
		query = input(f' BSSID: ')
		try:
			response = requests.get("https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + query)
			data = response.json()
			status = data["result"]
			if status == 200:
				lat = data["data"]["lat"]
				lon = data["data"]["lon"]
				print(f'Latinude: {lat}\n[*] Longitude: {lon}')
			else:
				errorCode = data["message"]
				errorMessage = data["desc"]
				print(f'Error code: {errorCode}\n[*] Error message: {errorMessage}')
		except:
			print(f'Error 007')