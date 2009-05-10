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

cnts = [{'x': 0, 'y': 0}]
deltas = [{'x': 10, 'y': 10}]

class center:
	def GET(self):
		for cnt, delta in zip(cnts, deltas):
			cnt['x'] += delta['x']
			cnt['y'] += delta['y']

			delta['x'] = max(-10, min(10, random.randint(-5, 5) + delta['x']))
			delta['y'] = max(-10, min(10, random.randint(-5, 5) + delta['y']))

			cnt['x'] = cnt['x'] % 750
			cnt['y'] = cnt['y'] % 750

		return json.dumps(cnts)

class reset:
	def GET(self):
		cnt = {'x': 100, 'y': 100}

class click:
	def GET(self):
		form = web.input(x=0, y=0)

		for cnt, delta in zip(cnts, deltas):
			delta['x'] = max(-10, min(10, int(form.x) - cnt['x']))
			delta['y'] = max(-10, min(10, int(form.y) - cnt['y']))

		cnts.append({'x': int(form.x), 'y': int(form.y)})
		deltas.append({'x': random.randint(-10, 10), 'y': random.randint(-10, 10)})

if __name__ == "__main__":
	app.run()
