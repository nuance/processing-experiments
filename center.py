from __future__ import with_statement

import web
import json

urls = (
    '/center', 'center',
    '/reset', 'reset',
)
app = web.application(urls, globals())
cnt = {'x': 0, 'y': 0}

class center:
	def GET(self):
		cnt['x'] += 25
		cnt['y'] += 25
		
		if cnt['x'] > 750:
			cnt['x'] = 0
			cnt['y'] = 0

		return json.dumps(cnt)
		
class reset:
	def GET(self):
		cnt = {'x': 100, 'y': 100}

if __name__ == "__main__":
	app.run()
