from __future__ import with_statement
from itertools import chain
import json
from random import randint

import web

urls = (
    '/center', 'center',
    '/create', 'create',
	'/click', 'click'
)
app = web.application(urls, globals())

class Runner(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.dx = randint(-10, 10)
		self.dy = randint(-10, 10)

	def move(self):
		self.x += self.dx
		self.y += self.dy

		self.dx = max(-10, min(10, randint(-5, 5) + self.dx))
		self.dy = max(-10, min(10, randint(-5, 5) + self.dy))

		self.x = self.x % 750
		self.y = self.y % 750

	def poke(self, x, y):
		self.dx = max(-10, min(10, x - self.x))
		self.dy = max(-10, min(10, y - self.y))

	@property
	def point(self):
		return {'x': self.x, 'y': self.y}

runners = {}
flares = []

class center:
	def GET(self):
		client = web.cookies().get("client")
		if client == None:
			return

		for runner in runners.itervalues():
			runner.move()

		ret = json.dumps([pt.point for pt in chain(runners.values(), [f for f, c in flares if client not in c])])
		for _, c in flares:
			c.add(client)

		return ret

class create:
	def GET(self):
		client = web.cookies().get("client")
		if client == None:
			client = len(runners)
			web.setcookie('client', client, 300)

		runners[client] = (Runner(randint(-5, 5), randint(-5, 5)))

class click:
	def GET(self):
		if web.cookies().get("client") == None:
			return

		form = web.input(x=0, y=0)
		x = int(form.x)
		y = int(form.y)

		for runner in runners.itervalues():
			runner.poke(x, y)

		flares.append((Runner(x, y), set(web.cookies().get("client"))))

if __name__ == "__main__":
	app.run()
