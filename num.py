# Python script to display all pixels RGB values
# from an image and output them a row at a time
#
# Import the PIL library - pip3 install Pillow
from PIL import Image

# Open our image
im = Image.open("not_art.png")
 
# Convert our image to RGB
rgb_im = im.convert('RGB')

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Use the .size object to retrieve a tuple contain (width,height) of the image
# and assign them to width and height variables
width = rgb_im.size[0]
height = rgb_im.size[1]
size = rgb_im.size[0]

# set some counters for current row and column and total pixels
row = 0
col = 0
codel = 10
codel_count = 0
color_format = 'hex' # rgb / hex

# Get color from the middle of the codel:
# col + codel / 2, row + codel / 2

limit = 0
while limit < size / 2:
	print("limit = ", limit)
	while col + codel < size - limit:
		print("%3d,%3d:" %(row,col))
		#get the RGB values from the current pixel
		r, g, b = rgb_im.getpixel((col + codel / 2, row + codel / 2))
		if color_format == 'rgb':
			print("\t(%3s,%3s,%3s)" % (str(r), str(g), str(b)))
		else:
			print("\t", rgb2hex(r, g, b))
		col += codel
		codel_count += 1
	while row + codel < size - limit:
		print("%3d,%3d:" %(row,col))
		# get the RGB values from the current pixel
		r, g, b = rgb_im.getpixel((col + codel / 2, row + codel / 2))
		if color_format == 'rgb':
			print("\t(%3s,%3s,%3s)" % (str(r), str(g), str(b)))
		else:
			print("\t", rgb2hex(r, g, b))
		row += codel
		codel_count += 1
	while col - codel >= limit:
		print("%3d,%3d:" %(row,col))
		# get the RGB values from the current pixel
		r, g, b = rgb_im.getpixel((col + codel / 2, row + codel / 2))
		if color_format == 'rgb':
			print("\t(%3s,%3s,%3s)" % (str(r), str(g), str(b)))
		else:
			print("\t", rgb2hex(r, g, b))
		col -= codel
		codel_count += 1
	limit += codel * 2
	while row - codel >= limit:
		print("%3d,%3d:" %(row,col))
		# get the RGB values from the current pixel
		r, g, b = rgb_im.getpixel((col + codel / 2, row + codel / 2))
		if color_format == 'rgb':
			print("\t(%3s,%3s,%3s)" % (str(r), str(g), str(b)))
		else:
			print("\t", rgb2hex(r, g, b))
		row -= codel
		codel_count += 1

# output for proof!
print("")
print("Width        = " + str(width) + " pixels")
print("Height       = " + str(height) + " pixels")
print("Codel size   = " + str(codel) + " pixels")
print("Total Codels = " + str(codel_count) + ".")
