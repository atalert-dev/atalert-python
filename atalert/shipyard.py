# shipyard.py

import os, logging


def check():
	vals = {
		"from_shipyard": True,
		"org_name": os.environ.get('SHIPYARD_ORG_NAME'),
		"project_id": os.environ.get('SHIPYARD_PROJECT_ID'),
		"vessel_id": os.environ.get('SHIPYARD_VESSEL_ID'),
		"log_id": os.environ.get('SHIPYARD_LOG_ID'),
	}
	if vals['project_id'] and vals['vessel_id'] and vals['log_id']:
		return vals

def get_link():
	"""
	Check environment for Shipyard values, if present, generate a link.
	"""
	vals = check()
	if vals:
		logging.info("Found shipyard environment, generating link to project/vessel/log")
		return f"https://app.shipyardapp.com/{vals['org_name']}/projects/{vals['project_id']}/vessels/{vals['vessel_id']}/logs/{vals['log_id']}"
