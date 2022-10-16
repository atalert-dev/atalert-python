# test_shipyard.py
import os
from atalert import atalert
atalert.ATALERT = 'http://127.0.0.1:8000/post'
from atalert.atalert import AlertTemplates

def test_shipyard_meta(slug):
	# fake the env
	os.environ['SHIPYARD_ORG_NAME'] = 'testorg'
	os.environ['SHIPYARD_PROJECT_ID'] = 'testprojectid'
	os.environ['SHIPYARD_VESSEL_ID'] = 'testvesselid'
	os.environ['SHIPYARD_LOG_ID'] = 'testlogid'
	
	resp = atalert.ok(slug, {'data': 'shipyard fake data'}, template=AlertTemplates.json)
	
	assert resp == 200