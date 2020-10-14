import json

from .benchmark import Benchmark

from .color import Color
from .resolution import Resolution

from .solidcolor import SolidColor
from .chessboard import Chessboard
from .fullsquare import FullSquare



class WallEApp():
	def __init__(self):
		self.setup_colors()
		self.setup_resolutions()
		self.setup_solidcolors()
		self.setup_chessboards()
		self.setup_fullsquares()
		pass


	def setup_colors(self):
		with open("jsons/colors.json") as f:
			self.colors_json = json.loads(f.read())

		self.colors = []
		for jsonObject in self.colors_json["colors"]:
			color = Color(jsonObject)
			self.colors.append(color)
		pass

	def setup_resolutions(self):
		with open("jsons/resolutions.json") as f:
			self.resolutions_json = json.loads(f.read())

		self.resolutions = []
		for jsonObject in self.resolutions_json["best"]:
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


	def setup_solidcolors(self):
		self.solidcolors = []
		for color in self.colors:
			for resolution in self.resolutions:
				solidcolor = SolidColor(resolution, color)
				self.solidcolors.append(solidcolor)
		pass

	def print_solidcolors(self):
		x = 0
		for solidcolor in self.solidcolors:
			print(f"{x+1}. {solidcolor}")
			x += 1
		pass

	def save_solidcolors(self):
		benchmark = Benchmark("save_solidcolors")
		x = 0
		for solidcolor in self.solidcolors:
			print(f"({x+1} of {len(self.solidcolors)}) Saving solidcolor {solidcolor} ...")
			#solidcolor.save_to_disk()
			if solidcolor.exists_on_disk():
				print(f"\tFile already exists: {solidcolor.filepath()}")
			else:
				solidcolor.save_to_disk()
				print(f"\tSaved: {solidcolor.filepath()}")
			benchmark.record_event(solidcolor)
			x += 1
		benchmark.print_events()
		pass


	def setup_chessboards(self):
		self.chessboards = []
		for pair in self.colors_json["pairs"]:
			primary = self.get_color_from_name(pair[0])
			secondary = self.get_color_from_name(pair[1])
			for resolution in self.resolutions:
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
			#chessboard.save_to_disk()
			if chessboard.exists_on_disk():
				print(f"\tFile already exists: {chessboard.filepath()}")
			else:
				chessboard.save_to_disk()
				print(f"\tSaved: {chessboard.filepath()}")
			benchmark.record_event(chessboard)
			x += 1
		benchmark.print_events()
		pass


	def setup_fullsquares(self):
		self.fullsquares = []
		for pair in self.colors_json["pairs"]:
			primary = self.get_color_from_name(pair[0])
			secondary = self.get_color_from_name(pair[1])
			for resolution in self.resolutions:
				fullsquare = FullSquare(primary, secondary, resolution)
				if fullsquare.has_two_colors():
					self.fullsquares.append(fullsquare)
		pass

	def print_fullsquares(self):
		x = 0
		for fullsquare in self.fullsquares:
			print(f"{x+1}. {fullsquare}")
			x += 1
		pass

	def save_fullsquares(self):
		benchmark = Benchmark("save_fullsquares")
		x = 0
		for fullsquare in self.fullsquares:
			print(f"({x+1} of {len(self.fullsquares)}) Saving fullsquare {fullsquare} ...")
			#fullsquare.save_to_disk()
			if fullsquare.exists_on_disk():
				print(f"\tFile already exists: {fullsquare.filepath()}")
			else:
				fullsquare.save_to_disk()
				print(f"\tSaved: {fullsquare.filepath()}")
			benchmark.record_event(fullsquare)
			x += 1
		benchmark.print_events()
		pass


