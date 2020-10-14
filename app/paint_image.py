
from pywall.image import WallEImage



def main():
	im = WallEImage()
	im.set_name("pinter")
	im.set_resolution("UHD")
	im.set_background("facebook")
	im.fill_background()
	im.fill_horizontal_strip(400, 200, im.colors[2])
	im.fill_vertical_strip(400, 200, im.colors[2])
	im.save_to_disk()
	im.print()
	pass

if __name__ == '__main__':
	main()
