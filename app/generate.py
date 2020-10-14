import math

import numpy
from PIL import Image
from pywall.walleapp import WallEApp



def test_stuff():
	data = numpy.zeros((1024, 1024, 3), dtype=numpy.uint8)
	max_pixel = 1024
	for x in range(0, max_pixel):
		for y in range(0, max_pixel):
			red = math.floor((y/4) / 16) * 16
			green = math.floor((x/4) / 16) * 16
			data[x, y] = [red, green, 0]
			pass
		pass

	im = Image.fromarray(data)
	im.save('test.png')
	pass


def generate_stuff():
	app = WallEApp()
	#app.save_chessboards()
	#app.save_solidcolors()
	app.save_fullsquares()
	pass


def main():
	generate_stuff()
	#test_stuff()
	pass


if __name__ == '__main__':
	main()
	pass
