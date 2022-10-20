# test_zapier.py

# test zapier-specific formatting and output

import os
from atalert import atalert
atalert.ATALERT = 'http://127.0.0.1:8000/post'
from atalert.atalert import AlertTemplates

def test_zapier_formatting(slug):
	# fake the env
	os.environ['ZAPIER_TEST'] = 'testorg'
	# os.environ['SHIPYARD_PROJECT_ID'] = 'testprojectid'
	# os.environ['SHIPYARD_VESSEL_ID'] = 'testvesselid'
	# os.environ['SHIPYARD_LOG_ID'] = 'testlogid'
	
	resp = atalert.ok(slug, {'zapier_payload': 'Testing *markdown* data from _zapier_\n\nIt will work great!'}, template=AlertTemplates.json)
	
	assert resp.status_code == 200