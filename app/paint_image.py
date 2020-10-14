
from pywall.image import WallEImage



def main():
	im = WallEImage()
	im.set_name("pinter")
	im.set_resolution("UHD")
	im.set_background("facebook")
	im.fill_background()
	im.fill_square(100, 100, 200, im.colors[2])
	im.save_to_disk()
	im.print()
	pass

if __name__ == '__main__':
	main()
