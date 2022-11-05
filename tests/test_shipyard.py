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
	os.environ['SHIPYARD_PROJECT_NAME'] = 'project name'
	os.environ['SHIPYARD_VESSEL_NAME'] = 'vessel name'
	os.environ['SHIPYARD_FLEET_NAME'] = 'fleet name'
	os.environ['SHIPYARD_VESSEL_START_TIME'] = '2021-03-12T21:22:47Z'
	
	resp = atalert.ok(slug, {'data': 'shipyard fake data'}, template=AlertTemplates.json)
	
	assert resp.status_code == 200