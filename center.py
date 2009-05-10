from __future__ import with_statement
import json
import random

import web

urls = (
    '/center', 'center',
    '/reset', 'reset',
	'/click', 'click'
)
app = web.application(urls, globals())
cnt = {'x': 0, 'y': 0}
delta = {'x': 10, 'y': 10}

class center:
	def GET(self):
		cnt['x'] += delta['x']
		cnt['y'] += delta['y']
		
		delta['x'] += random.randint(-5, 5)
		delta['y'] += random.randint(-5, 5)
		
		cnt['x'] = cnt['x'] % 250
		cnt['y'] = cnt['y'] % 250

		return json.dumps(cnt)
		
class reset:
	def GET(self):
		cnt = {'x': 100, 'y': 100}

class click:
	def GET(self):
		form = web.input(x=0, y=0)
		cnt['x'] = int(form.x)
		cnt['y'] = int(form.y)

if __name__ == "__main__":
	app.run()
