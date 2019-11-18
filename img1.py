from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# random character:
def rndChar():
	return chr(random.randint(65, 90))

# random color1:
def rndColor1():
	return(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	
# random color2:
def rndColor2():
	return(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	
# 240 * 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# creat font object:
font = ImageFont.truetype('G:\\Windows\\Fonts\\arial.ttf', 36)

# creat draw object:
draw = ImageDraw.Draw(image)

# fill each pixels:
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor1())

# output character:
for t in range(4):
	draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())
	
# blur:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')