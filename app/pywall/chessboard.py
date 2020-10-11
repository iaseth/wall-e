import os
import math

from PIL import Image

from .benchmark import Benchmark



class Chessboard():
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

		cell_height = math.ceil(self.resolution.height / 8)
		cell_width = math.ceil(self.resolution.width / math.floor(self.resolution.width/cell_height))

		self.benchmark.record_event("before the loop")
		for x in range(0, self.resolution.height):
			cx = math.floor(x / cell_height)
			cx_even = cx%2 == 0
			for y in range(0, self.resolution.width):
				cy = math.floor(y / cell_width)
				cy_even = cy%2 == 0
				white = (cx_even and cy_even) or ((not cx_even) and (not cy_even))
				if white:
					data[x, y] = primary
				else:
					data[x, y] = secondary
				pass
			pass

		self.benchmark.record_event("after the loop")
		im = Image.fromarray(data)
		im.save(self.filepath())
		self.benchmark.record_event("saved image")
		self.benchmark.print_events()
		pass

	def filepath(self):
		return f"pngs/chessboards/{self.filename()}"

	def filename(self):
		return f"chessboard_{self.primary.name}_{self.secondary.name}_{self.resolution.name}.png"

	def __str__(self):
		return f"({self.primary.name}|{self.secondary.name}) {self.resolution}"


