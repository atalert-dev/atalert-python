# test_files.py

from atalert import atalert
atalert.ATALERT = 'http://127.0.0.1:8000/post'

def test_ok_json_file(slug):
	resp = atalert.send_file_path('ok', slug, './tests/files/data.json')
	assert resp.status_code == 200

def test_warn_image_file(slug):
	resp = atalert.send_file_path('warning', slug, './tests/files/testcat.jpg')
	assert resp.status_code == 200

def test_ok_file(slug):
	resp = atalert.ok_file(slug, './tests/files/data.json')
	assert resp.status_code == 200

def test_warn_file(slug):
	resp = atalert.warn_file(slug, './tests/files/data.json')
	assert resp.status_code == 200

def test_err_file(slug):
	resp = atalert.err_file(slug, './tests/files/data.json')
	assert resp.status_code == 200
