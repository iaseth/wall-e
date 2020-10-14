import os
import math

from PIL import Image

from .benchmark import Benchmark



class FullSquare():
	def __init__(self, primary, secondary, resolution):
		self.primary = primary
		self.secondary = secondary
		self.resolution = resolution
		self.benchmark = Benchmark(self)
		pass

	def has_two_colors(self):
		return (self.primary != self.secondary)

	def exists_on_disk(self):
		if os.path.isfile(self.filepath()):
			return True
		else:
			return False
		pass

	def save_to_disk(self):
		self.benchmark.reset()
		self.benchmark.record_event("entered save_to_disk()")
		data = self.resolution.get_numpy_array()

		primary = self.primary.get_RGB()
		secondary = self.secondary.get_RGB()

		square_width = math.ceil(self.resolution.height * 3 / 5)
		half_square_width = math.ceil(square_width / 2)
		square_start_x = math.ceil(self.resolution.height / 2) - half_square_width
		square_start_y = math.ceil(self.resolution.width / 2) - half_square_width

		square_end_x = square_start_x + square_width
		square_end_y = square_start_y + square_width

		self.benchmark.record_event("before the loop")
		for x in range(0, self.resolution.height):
			if x > square_start_x and x < square_end_x:
				for y in range(0, self.resolution.width):
					if y > square_start_y and y < square_end_y:
						data[x, y, 0] = primary[0]
						data[x, y, 1] = primary[1]
						data[x, y, 2] = primary[2]
						pass
					else:
						data[x, y, 0] = secondary[0]
						data[x, y, 1] = secondary[1]
						data[x, y, 2] = secondary[2]
						pass
					pass
				pass
			else:
				for y in range(0, self.resolution.width):
					data[x, y, 0] = secondary[0]
					data[x, y, 1] = secondary[1]
					data[x, y, 2] = secondary[2]
					pass
				pass

		self.benchmark.record_event("after the loop")
		im = Image.fromarray(data)
		im.save(self.filepath())
		self.benchmark.record_event("saved image")
		self.benchmark.print_events()
		pass

	def filepath(self):
		return f"pngs/fullsquares/{self.filename()}"

	def filename(self):
		return f"fullsquare_{self.primary.name}_{self.secondary.name}_{self.resolution.name}.png"

	def __str__(self):
		return f"({self.primary.name}|{self.secondary.name}) {self.resolution}"




