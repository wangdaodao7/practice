from collections import Counter
import glob,os
from PIL import Image


ss = ' sssss21joiomo'

j = Counter(ss)
print(j.most_common(5)[2:4])




for infile in glob.glob('*.png'):
    print(infile)


# im = Image.open(r'D:\python\1111\h\AppIcon60x60@2x.png')
# im2 = im.resize((400, 400), Image.ANTIALIAS)
# im2.show()

for root, dirs, files in os.walk(r'D:\video'):
	# print(files)
	for file in files:
		
		if 'mp4' in file:
			print('--------------{}---------------------'.format(file))
		else:
			print(file ,type(file))
