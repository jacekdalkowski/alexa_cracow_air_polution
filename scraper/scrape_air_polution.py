from pymongo import MongoClient
from lxml import html
import requests
import datetime

def is_float(value):
	try:
		float(value)
		return True
	except:
		return False

def update_db(pm_10_level):
	mongo_client = MongoClient('mongodb://airpolution-db:27017')
	airpolution_db = mongo_client['airpolution']
	airpolution_col = airpolution_db['airpolution']

	airpolution_col.update_one({'_id': 1}, {'$set': {'_id': 1, 'pm_10': pm_10_level, 'timestamp': datetime.datetime.utcnow() }}, True)

def fetch_pm_10_level():
	#page = requests.get('http://powietrzewkrakowie.pl/')
	page = requests.get('http://powietrze.gios.gov.pl/pjp/current/station_details/table/10121/1/0')
	dom = html.fromstring(page.content)
	#quality = dom.xpath('//h3[1]/span/text()')
	quality = dom.xpath('//tr/td[1]/text()')
	quality = [q.replace('\t', '').replace('\r', '').replace('\n', '').replace(',', '.') for q in quality]
	del quality[-3:]
	quality = [q for q in quality if is_float(q)]

	latest_pm_10_level = quality[-1]
	if latest_pm_10_level and is_float(latest_pm_10_level):
		return float(quality[-1])
	return None

pm_10_level = fetch_pm_10_level()
print 'pm_10 level fetched: ' + str(pm_10_level)
update_db(pm_10_level)

