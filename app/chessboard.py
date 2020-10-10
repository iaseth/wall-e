import os
import math
import json

import numpy
from PIL import Image

from pywall.color import Color
from pywall.resolution import Resolution



class Chessboard():
	def __init__(self, primary, secondary, resolution):
		self.primary = primary
		self.secondary = secondary
		self.resolution = resolution
		pass

	def hasTwoColors(self):
		return (self.primary != self.secondary)

	def existsOnDisk(self):
		if os.path.isfile(self.filepath()):
			return True
		else:
			return False
		pass

	def saveToDisk(self):
		data = self.resolution.getNumpyArray()

		primary = self.primary.getRGB()
		secondary = self.secondary.getRGB()

		cell_height = math.ceil(self.resolution.height / 8)
		cell_width = math.ceil(self.resolution.width / math.floor(self.resolution.width/cell_height))

		for x in range(0, self.resolution.height):
			for y in range(0, self.resolution.width):
				cx = math.floor(x / cell_height)
				cy = math.floor(y / cell_width)
				cx_even = cx%2 == 0
				cy_even = cy%2 == 0
				white = (cx_even and cy_even) or ((not cx_even) and (not cy_even))
				if white:
					data[x, y] = primary
				else:
					data[x, y] = secondary
				pass
			pass

		im = Image.fromarray(data)
		im.save(self.filepath())
		pass

	def filepath(self):
		return f"pngs/chessboards/{self.filename()}"

	def filename(self):
		return f"chessboard_{self.primary.name}_{self.secondary.name}_{self.resolution.name}.png"

	def __str__(self):
		return f"({self.primary.name}|{self.secondary.name}) {self.resolution}"


class App():
	def __init__(self):
		self.setupColors()
		self.setupResolutions()
		self.setupChessboards()
		pass

	def setupColors(self):
		with open("jsons/colors.json") as f:
			jo = json.loads(f.read())

		self.colors = []
		for jsonObject in jo["colors"]:
			color = Color(jsonObject)
			self.colors.append(color)
		pass

	def setupResolutions(self):
		with open("jsons/resolutions.json") as f:
			jo = json.loads(f.read())

		self.resolutions = []
		for jsonObject in jo["resolutions"]:
			resolution = Resolution(jsonObject)
			self.resolutions.append(resolution)
		pass

	def setupChessboards(self):
		self.chessboards = []
		for primary in self.colors:
			for secondary in self.colors:
				for resolution in self.resolutions:
					chessboard = Chessboard(primary, secondary, resolution)
					if chessboard.hasTwoColors():
						self.chessboards.append(chessboard)
		pass

	def printColors(self):
		for color in self.colors:
			print(color)
		pass

	def printResolutions(self):
		for resolution in self.resolutions:
			print(resolution)
		pass

	def printChessboards(self):
		x = 0
		for chessboard in self.chessboards:
			print(f"{x+1}. {chessboard}")
			x += 1
		pass

	def saveChessboards(self):
		x = 0
		for chessboard in self.chessboards:
			print(f"({x+1} of {len(self.chessboards)}) Saving chessboard {chessboard} ...")
			if chessboard.existsOnDisk():
				print(f"\tFile already exists: {chessboard.filepath()}")
			else:
				#chessboard.saveToDisk()
				print(f"\tSaved: {chessboard.filepath()}")
			x += 1
		pass


def chessboard_stuff():
	app = App()
	app.saveChessboards()
	pass


def main():
	chessboard_stuff()


if __name__ == '__main__':
	main()
	pass
