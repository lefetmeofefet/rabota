#Import required Image library
from PIL import Image, ImageFilter

#Open existing image
OriImage = Image.open('../shlombif/test.png')
# OriImage.show()

OriImage = OriImage.filter(ImageFilter.BLUR)
OriImage = OriImage.filter(ImageFilter.BLUR)
OriImage = OriImage.filter(ImageFilter.BLUR)
OriImage = OriImage.filter(ImageFilter.BLUR)
OriImage = OriImage.filter(ImageFilter.BLUR)
# blurImage.show()
#Save blurImage
OriImage.save('test.png')