import math
import json

import numpy
from PIL import Image

from pywall.color import Color
from pywall.resolution import Resolution
from pywall.chessboard import Chessboard



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
		with open("jsons/chessboards.json") as f:
			jo = json.loads(f.read())
		self.chessboards = []
		for pair in jo["colors"]:
			primary = self.getColorFromName(pair[0])
			secondary = self.getColorFromName(pair[1])
			for resolutionName in jo["resolutions"]:
				resolution = self.getResolutionFromName(resolutionName)
				chessboard = Chessboard(primary, secondary, resolution)
				if chessboard.hasTwoColors():
					self.chessboards.append(chessboard)
		pass

	def getColorFromName(self, colorName):
		for color in self.colors:
			if color.name == colorName:
				return color
		return None

	def getResolutionFromName(self, resolutionName):
		for resolution in self.resolutions:
			if resolution.name == resolutionName:
				return resolution
		return None

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
