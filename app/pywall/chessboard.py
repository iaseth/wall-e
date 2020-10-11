import os



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


