# Atalert Python Package

https://atalert.dev

Too many different data notification or alert packages got you down?

Start by using the Atalert Slack App to generate alert webhooks.

Customize the template, delivery channel, and notify your team. 

Then, take note of the webhook url slug for the code examples below!

It's a best practice to make as many different webhooks as you need for different functional areas, such as code deployments, new user registrations, results of a long-running data pipeline. If there's information somewhere that's difficult to get to, use Atalert to send it to your Slack workspace.

## Installation

`pip install atalert` or `poetry add atalert`


## Basic Usage

```
import atalert


# add these to wherever you need to send a slack atalert, customize with your own data payload

# send an 'ok' atalert
atalert.ok('alert_slug_here', data)

# send a 'warning' atalert
atalert.warn('alert_slug_here', data)

# send an 'error' atalert
atalert.err('alert_slug_here', data)

```

You'll immediately get a custom alert notification in slack according to your webhook configuration. 

Then all your data or platform alerts are in the one place you are every day, Slack!


## Sending Files to Slack

First, configure your alert within the Atalert Slack App to use the 'attachment' template type.

Then, use any of the following methods:

```
from atalert import ok_file, warn_file, err_file

# send 'data.json' in the current working directory as a file attachment with OK status
ok_file('alert_slug_here', './data.json')

# send 'error.log' in as a file with ERROR status
err_file('alert_slug_here', './error.log')

# send 'datacat.jpg' as a picture with WARNING status
warn_file('alert_slug_here', './datacat.jpg')

```

Enjoy fine file-based data in your Slack workspace!


## Decorator Usage

Want to simplify error notifications? Need to automatically send a method's return object somewhere? Use the decorators!

```
from atalert import atalert_on_error
from atalert import atalert_ok_result

# decorator configured with a webhook url slug, will forward any exceptions
@atalert_on_error('alert_slug_here')
def main_processing_method(*args, **kwargs):

	# do some things here that may go wrong and throw exceptions
	numbers = business / 0

	return numbers

@atalert_ok_result('alert_slug_here')
def alternate_processing_method(*args, **kwargs):
	# do some math here that you want to send to slack
	numbers = statistics.stdev(args)
	# whatever you return will automagically go to your predefined slack channel
	return numbers 

```

You'll get your code exception or method results sent directly to slack!

