import shodan
import os
import time
import datetime

SHODAN_API_KEY = "PSKINdQe1GyxGgecYz2191H2JoS9qvgD"

api = shodan.Shodan(SHODAN_API_KEY)

def find_only_ip():
	try:
		results = api.search('''{s}'''.format(s=search))
		print('Results found: %s' % results['total'])
		for result in results['matches']:
				print('{}'.format(result['ip_str']))
	except (shodan.APIError)as e:
		print('Error: {}'.format(e))
def find():
	try:
		results = api.search('''{ts}'''.format(ts=search))
		print('Results found: %s' % results['total'])
		for result in results['matches']:
				print('IP: {}'.format(result['ip_str']))
				print(result['data'])
				print('')
	except (shodan.APIError)as e:
		print('Error: {}'.format(e))
		var = find()



print ('''
here are the search filters (with example):
country: Country
city: City
geo: Geo location
hostname: Host
net: ip address
os: Operating system
port: Port
''')

search = input('enter your search term==>')

question = input('''you only need ip or all data? data/ip==>''')

if question == ("ip"):
	find_only_ip()
elif question == ("data"):
	find()
else:
	print('you entered incorrect data restart module...')
	time.sleep(2)
	cmd = os.system("python3 hm1-.py")
