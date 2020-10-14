import json
import math
import os

from PIL import Image

from .benchmark import Benchmark

from .color import Color
from .resolution import Resolution


class WallEImage():
	def __init__(self, name):
		self.name = name
		self.setup_colors()
		self.setup_resolutions()
		self.resolution = None
		self.background = None
		self.data = None
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
			if self.background != None:
				self.fill_rectangle(0, 0, self.resolution.height, self.resolution.width, self.background)
				pass
			pass
		pass

	def fill_horizontal_strip(self, start_x, width, color):
		if self.resolution != None:
			self.fill_rectangle(start_x, 0, width, self.resolution.width, color)
		pass

	def fill_vertical_strip(self, start_y, width, color):
		if self.resolution != None:
			self.fill_rectangle(0, start_y, self.resolution.height, width, color)
		pass

	def fill_border(self, width, color):
		if self.resolution != None:
			self.fill_horizontal_strip(0, width, color)
			self.fill_horizontal_strip(self.resolution.height - width, width, color)
			self.fill_vertical_strip(0, width, color)
			self.fill_vertical_strip(self.resolution.width - width, width, color)
		pass

	def fill_square(self, start_x, start_y, side_width, color):
		self.fill_rectangle(start_x, start_y, side_width, side_width, color)
		pass

	def fill_rectangle(self, start_x, start_y, height, width, color):
		if self.resolution != None:
			end_x = (start_x + height) if (start_x + height) < self.resolution.height else self.resolution.height
			end_y = (start_y + width) if (start_y + width) < self.resolution.width else self.resolution.width
			color_rgb = color.get_RGB()
			data = self.data
			for x in range(start_x, end_x):
				for y in range(start_y, end_y):
					data[x, y, 0] = color_rgb[0]
					data[x, y, 1] = color_rgb[1]
					data[x, y, 2] = color_rgb[2]
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


