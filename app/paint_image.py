
from pywall.image import WallEImage



def main():
	im = WallEImage()
	im.set_name("pinter")
	im.set_resolution("UHD")
	im.set_background("facebook")
	im.fill_background()
	im.save_to_disk()
	im.print()
	pass

if __name__ == '__main__':
	main()
