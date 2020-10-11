import json

from .benchmark import Benchmark

from .color import Color
from .resolution import Resolution
from .chessboard import Chessboard



class WallEApp():
	def __init__(self):
		self.setup_colors()
		self.setup_resolutions()
		self.setup_chessboards()
		pass


	def setup_colors(self):
		with open("jsons/colors.json") as f:
			jo = json.loads(f.read())

		self.colors = []
		for jsonObject in jo["colors"]:
			color = Color(jsonObject)
			self.colors.append(color)
		pass

	def setup_resolutions(self):
		with open("jsons/resolutions.json") as f:
			jo = json.loads(f.read())

		self.resolutions = []
		for jsonObject in jo["resolutions"]:
			resolution = Resolution(jsonObject)
			self.resolutions.append(resolution)
		pass


	def get_color_from_name(self, colorName):
		for color in self.colors:
			if color.name == colorName:
				return color
		return None

	def get_resolution_from_name(self, resolutionName):
		for resolution in self.resolutions:
			if resolution.name == resolutionName:
				return resolution
		return None


	def print_colors(self):
		for color in self.colors:
			print(color)
		pass

	def print_resolutions(self):
		for resolution in self.resolutions:
			print(resolution)
		pass


	def setup_chessboards(self):
		with open("jsons/chessboards.json") as f:
			jo = json.loads(f.read())
		self.chessboards = []
		for pair in jo["colors"]:
			primary = self.get_color_from_name(pair[0])
			secondary = self.get_color_from_name(pair[1])
			for resolutionName in jo["resolutions"]:
				resolution = self.get_resolution_from_name(resolutionName)
				chessboard = Chessboard(primary, secondary, resolution)
				if chessboard.has_two_colors():
					self.chessboards.append(chessboard)
		pass

	def print_chessboards(self):
		x = 0
		for chessboard in self.chessboards:
			print(f"{x+1}. {chessboard}")
			x += 1
		pass

	def save_chessboards(self):
		benchmark = Benchmark("saveChessboards")
		x = 0
		for chessboard in self.chessboards:
			print(f"({x+1} of {len(self.chessboards)}) Saving chessboard {chessboard} ...")
			if chessboard.exists_on_disk():
				print(f"\tFile already exists: {chessboard.filepath()}")
			else:
				#chessboard.save_to_disk()
				print(f"\tSaved: {chessboard.filepath()}")
			benchmark.record_event(chessboard)
			x += 1
		benchmark.print_events()
		pass


