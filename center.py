from __future__ import with_statement

import web
import json

urls = (
    '/center', 'center',
    '/reset', 'reset',
	'/click', 'click'
)
app = web.application(urls, globals())
cnt = {'x': 0, 'y': 0}

class center:
	def GET(self):
		cnt['x'] += 25
		cnt['y'] += 25
		
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
