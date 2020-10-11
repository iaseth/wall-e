import os

from PIL import Image

from .benchmark import Benchmark



class SolidColor():
	def __init__(self, resolution, color):
		self.resolution = resolution
		self.color = color
		self.benchmark = Benchmark(self)
		pass

	def exists_on_disk(self):
		if os.path.isfile(self.filepath()):
			return True
		else:
			return False
		pass

	def save_to_disk(self):
		self.benchmark.reset()
		self.benchmark.record_event("entered save_to_disk()")
		color = self.color.get_RGB()
		data = self.resolution.get_numpy_array()

		self.benchmark.record_event("before the loop")
		for x in range(0, self.resolution.height):
			for y in range(0, self.resolution.width):
				data[x, y, 0] = color[0]
				data[x, y, 1] = color[1]
				data[x, y, 2] = color[2]
				pass
			pass

		self.benchmark.record_event("after the loop")
		im = Image.fromarray(data)
		im.save(self.filepath())
		self.benchmark.record_event("saved image")
		self.benchmark.print_events()
		pass

	def filepath(self):
		return f"pngs/solidcolors/{self.filename()}"

	def filename(self):
		return f"solidcolor_{self.color.name}_{self.resolution.name}.png"

	def __str__(self):
		return f"({self.color.name}) {self.resolution}"


