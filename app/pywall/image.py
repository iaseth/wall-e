import json
import math
import os

from PIL import Image

from .benchmark import Benchmark

from .color import Color
from .resolution import Resolution


class WallEImage():
	def __init__(self):
		self.setup_colors()
		self.setup_resolutions()
		self.resolution = None
		self.background = None
		self.data = None
		self.name = None
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
		for jsonObject in self.resolutions_json["resolutions"]:
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


	def set_resolution(self, resolution_name):
		resolution = self.get_resolution_from_name(resolution_name)
		if resolution and resolution != self.resolution:
			self.resolution = resolution
			self.data = self.resolution.get_numpy_array()
			pass
		pass

	def set_background(self, color_name):
		color = self.get_color_from_name(color_name)
		if color and color != self.background:
			self.background = color
		pass


	def fill_background(self):
		if self.resolution != None:
			background = self.background.get_RGB()
			data = self.data
			for x in range(0, self.resolution.height):
				for y in range(0, self.resolution.width):
					data[x, y, 0] = background[0]
					data[x, y, 1] = background[1]
					data[x, y, 2] = background[2]
					pass
				pass
			pass
		pass


	def get_name(self):
		return self.name
		pass

	def set_name(self, name):
		self.name = name
		pass


	def save_to_disk(self):
		im = Image.fromarray(self.data)
		im.save(self.get_filepath())
		pass


	def get_filename(self):
		return f"{self.name}.png"
		pass

	def get_filepath(self):
		return f"pngs/{self.get_filename()}"
		pass


	def print_all(self):
		self.print_colors()
		self.print_resolutions()
		pass

	def print_data(self):
		print(f"{self.data}")
		pass

	def print(self):
		print(f"Resolution: {self.resolution}")
		print(f"Background: {self.background}")
		print(f"      Path: {self.get_filepath()}")
		pass


