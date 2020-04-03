from datetime import datetime


class Params:
	"""
	Parameters class.

	This file centralizes anything that can be 
	parametrized in the code.
	"""

	raw_data = '../data/raw/'
	processed_data = '../data/processed/'

	log_name = '../log/dump.log'

	# if this is set to True, then all the nodes will be automatically 
	# considered not up-to-date and will be rerun.
	rerun = True

	today = datetime.now().strftime("%Y-%m-%d")

	url_abc = 'https://www.superabc.com.br/'
	chrome_path = 'C:/Users/pedro/selenium/chromedriver.exe'
	path_base = 'C:/Users/pedro/Ironhack_DAFT/Labs/week4_remote/Data Pipeline/web_scraping_super_abc/'

	#path's to use in data preparation
	path_data_raw = path_base + 'data/raw/'
	sub_cat_processed = path_data_raw + 'sub_cat.csv'
	product_links =  path_data_raw +'product_links.csv'
	last_update_links = path_data_raw + 'last_update.txt'
	days_to_update_prep = 15

	#path's to use in data processed
	path_data_processed = path_base + 'data/processed/'
	links_processed = path_data_processed + 'links_worked.csv'
	data_csv = path_data_processed + today + '.csv'