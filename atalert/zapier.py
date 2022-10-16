# zapier.py


import os, logging

# this is more for testing the core api backend's response to posting an alert as from zapier
# zapier integration already config'd to add 'from_zapier' query string
def check():
	is_zap = os.environ.get('ZAPIER_TEST')
	if is_zap:
		return {
			'from_zapier': True
		}