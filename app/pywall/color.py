


class Color():
	def __init__(self, jsonObject):
		self.name = jsonObject["name"]
		self.color = jsonObject["color"]
		pass

	def get_RGB(self):
		hex_string = self.color.strip().lstrip("#")
		if len(hex_string) == 3:
			red = int(hex_string[0] + hex_string[0], 16)
			green = int(hex_string[1] + hex_string[1], 16)
			blue = int(hex_string[2] + hex_string[2], 16)
			return [red, green, blue]
		elif len(hex_string) == 6:
			red = int(hex_string[0:2], 16)
			green = int(hex_string[2:4], 16)
			blue = int(hex_string[4:6], 16)
			return [red, green, blue]
		else:
			return [0, 200, 0]

	def __str__(self):
		return f"{self.name} [{self.color}]"


