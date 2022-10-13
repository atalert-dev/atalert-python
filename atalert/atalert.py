# atalert.py

# easy and centralized alerts from any platform (that can run python) to your slack

import json
from enum import Enum
import logging
from functools import wraps
from traceback import format_exception
import requests

ATALERT = 'https://atalert-platform.atadataco.com/post'

class AlertTemplates(str, Enum):
	form = 'form'
	text = 'text'
	json = 'json'

def send(status: str, slug: str, data, template: AlertTemplates = AlertTemplates.text):
	"""Send an alert to your webhook by slug."""
	try:
		url = f"{ATALERT}/{status}/{slug}"
		logging.error(url)
		resp = None
		if template == AlertTemplates.form:
			resp = requests.post(url, data=json.dumps(data))
		if template == AlertTemplates.text:
			resp = requests.post(url, data=data)
		if template == AlertTemplates.json:
			resp = requests.post(url, json=data)
		# error handle - might be 404, 429
		logging.error(resp.status_code)
		return resp.status_code
	except Exception as err:
		logging.error(f"atalert.send: {err}")

# shorthand methods for basic webhook send
def ok(slug: str, data, template: AlertTemplates = AlertTemplates.text):
	return send('ok', slug, data)

def warn(slug: str, data, template: AlertTemplates = AlertTemplates.text):
	return send('warning', slug, data)

def err(slug: str, data, template: AlertTemplates = AlertTemplates.text):
	return send('error', slug, data)

# error alert any exceptions within the wrapped method
# exceptions are not re-raised
def atalert_on_error(slug):
	# logging.error(slug)
	def wrap_errors(func):
		@wraps(func)
		def wrapped(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except Exception as error:
				e = format_exception(error)
				exc_lines = [x for x in e if not 'atalert/atalert.py' in x]
				err(slug, data="\n".join(exc_lines))
		return wrapped
	return wrap_errors

# ok alert the result of a wrapped method
def atalert_ok_result(slug):
	# prefab 'ok' with result data
	def wrap_results(func):
		@wraps(func)
		def wrapped(*args, **kwargs):
			result = func(*args, **kwargs)
			ok(slug, data=result, template=AlertTemplates.form)
			return result
		return wrapped
	return wrap_results