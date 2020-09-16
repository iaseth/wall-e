import numpy
from PIL import Image



def main():
	data = numpy.zeros((1024, 1024, 3), dtype=numpy.uint8)
	max_pixel = 1024
	for x in range(0, max_pixel):
		for y in range(0, max_pixel):
			data[x, y] = [x/4, 0, 0]
			pass
		pass

	im = Image.fromarray(data)
	im.save('test.png')
	pass


if __name__ == '__main__':
	main()
	pass
