from nodes import data_gathering
from nodes import data_preparation
from params import Params
import logging

def process(params):
	"""
	The ETL pipeline.

	It contains the main nodes of the extract-transform-load 
	pipeline from the process. 
	"""

	if not data_preparation.done(params):
		data_preparation.update(params)

	if not data_gathering.done(params):
		data_gathering.update(params)


if __name__ == '__main__': 

	params = Params()
	logging.basicConfig(filename=params.log_name,
						level=logging.INFO,
						format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    					datefmt='%Y-%m-%d %H:%M:%S')
	
	process(params)