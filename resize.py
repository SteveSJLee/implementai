import os
from PIL import Image

def resize(img_name, resize_ratio):
	max_height = resize_ratio
# get image size
	i = Image.open(img_name)
	width, height = i.size
	w_ratio = width/resize_ratio
	crop_size = ((height/w_ratio) - max_height)/2 
	# limit image size to (x = resize_ratio, y <= max_height)
	i = i.resize((int(width/w_ratio), int(height/w_ratio)))
	#crop if height is too long
	if i.size[1] > max_height:
		i = i.crop(
			(
				0, 
				int(i.size[1]/2) - max_height/2,
				resize_ratio, 
				int(i.size[1]/2) + max_height/2
			)
		)
			
	#save
	i.convert('RGB').save(img_name, dpi=(720,720))

for file in os.listdir():
	if not file.endswith('.py'):
		resize(file, 64)
