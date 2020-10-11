import numpy



class Resolution():
	def __init__(self, jsonObject):
		self.name = jsonObject["name"]
		self.height = jsonObject["height"]
		self.width = jsonObject["width"]
		pass

	def get_numpy_array(self):
		data = numpy.zeros((self.height, self.width, 3), dtype=numpy.uint8)
		return data

	def __str__(self):
		return f"{self.name} [{self.width}x{self.height}]"


