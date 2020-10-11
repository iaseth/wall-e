import math

import numpy
from PIL import Image
from pywall.walleapp import WallEApp



def some_stuff():
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


def chessboard_stuff():
	app = WallEApp()
	app.saveChessboards()
	pass


def test_stuff():
	number = 0
	for x in range(0, 1000):
		for y in range(0, 1000):
			for z in range(0, 100):
				number += 1
	pass


def main():
	#chessboard_stuff()
	test_stuff()
	pass


if __name__ == '__main__':
	main()
	pass
