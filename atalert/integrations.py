# integrations.py

# auto-detect what environment we're running in, add tracking params to the post url

import atalert.shipyard as shipyard

def check():

	shipyard_meta = shipyard.check()
	if shipyard_meta:
		return shipyard_meta

	return {'params': 'testing'}

	# TODO find other env things to check for follow same module.check() pattern
	# return dictionaries we can convert to query strings