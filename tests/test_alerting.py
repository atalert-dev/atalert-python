# test_alerting.py

from atalert import atalert

def test_ok_alert(slug):
	resp = atalert.ok(slug, {'test': 'data'})
	assert resp == 200

def test_warn_alert(slug):
	resp = atalert.warn(slug, {'test': 'data'})
	assert resp == 200

def test_error_alert(slug):
	resp = atalert.err(slug, {'test': 'data'})
	assert resp == 200