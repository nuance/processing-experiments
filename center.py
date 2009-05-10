from __future__ import with_statement
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

class center:
	def GET(self):
		for runner in runners.itervalues():
			runner.move()

		return json.dumps([r.point for r in runners.itervalues()])

class create:
	def GET(self):
		runners[len(runners)] = (Runner(randint(-5, 5), randint(-5, 5)))

class click:
	def GET(self):
		form = web.input(x=0, y=0)
		x = int(form.x)
		y = int(form.y)

		for runner in runners.itervalues():
			runner.poke(x, y)

if __name__ == "__main__":
	app.run()
