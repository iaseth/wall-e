import math
import json

import numpy
from PIL import Image


class Color():
	def __init__(self, jsonObject):
		self.name = jsonObject["name"]
		self.color = jsonObject["color"]
		pass

	def __str__(self):
		return f"{self.name} [{self.color}]"


class Resolution():
	def __init__(self, jsonObject):
		pass


class App():
	def __init__(self):
		self.setupColors()
		self.resolutions = []
		pass

	def setupColors(self):
		with open("colors.json") as f:
			jo = json.loads(f.read())

		self.colors = []
		for jsonObject in jo["colors"]:
			color = Color(jsonObject)
			self.colors.append(color)
		pass

	def setupResolutions(self):
		pass

	def printColors(self):
		for color in self.colors:
			print(color)
		pass


def chessboard_stuff():
	app = App()
	app.printColors()
	pass


def main():
	chessboard_stuff()


if __name__ == '__main__':
	main()
	pass
