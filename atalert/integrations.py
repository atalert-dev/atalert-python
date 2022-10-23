# integrations.py

# auto-detect what environment we're running in, add tracking params to the post url

import atalert.shipyard as shipyard
import atalert.zapier as zapier

def check():

	zapier_meta = zapier.check()
	if zapier_meta:
		return zapier_meta

	shipyard_meta = shipyard.check()
	if shipyard_meta:
		return shipyard_meta

	return

	# TODO find other env things to check for follow same module.check() pattern
	# return dictionaries we can convert to query strings