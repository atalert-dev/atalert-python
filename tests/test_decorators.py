# test_decorators.py
import logging
import atalert
atalert.ATALERT = 'http://127.0.0.1:8000/post'
from atalert.atalert import atalert_on_error
from atalert.atalert import atalert_ok_result
import statistics

def test_exception_decorator(slug):

	@atalert_on_error(slug)
	def math_error():
		business = 'business'
		numbers = business / 0
		return numbers

	result = math_error()
	logging.error(result)
	assert result == None


def test_result_decorator(slug):

	@atalert_ok_result(slug)
	def math_success():
		business = [5,6,7,8,1000000,2000000]
		logging.error(business)
		return {
			'stdev': statistics.stdev(business),
			'mean': statistics.mean(business),
			'quants': statistics.quantiles(business)
		}

	result = math_success()
	# logging.error(result)
	# stdev=836656.9189412508&mean=500004.3333333333&quants=5.75&quants=7.5&quants=1250000.0
	assert result['stdev'] == 836656.9189412508
	assert result['mean'] == 500004.3333333333

