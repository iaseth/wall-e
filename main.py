from PIL import Image



def main():
	im = Image.new('RGB', (1024, 1024))
	im.putdata([(255,0,0), (0,255,0), (0,0,255)])
	im.save('test.png')


if __name__ == '__main__':
	main()
