from pyautogui import size
from PIL import Image, ImageDraw,ImageFilter,ImageEnhance

image = Image.new("RGBA",(size().width,size().height) )


def resizeH(H , img) :
    h = img.height
    w = img.width   
    p = (H - h) / H 

    h_ = H
    w_ = int(w*p)+w
    print((w_,h_))
    return img.resize((w_,h_))

width = size().width # x
height = size().height # y

for i in range(3) : 
    img = Image.open(f"{i+1}.jpg")
    img = resizeH(height,img)
    image.paste(img,(width//3*i,0))
    image.show()


enhancer = ImageEnhance.Brightness(image)        
im = enhancer.enhance(0.4)

image.save("image.png")
im.save("image.png")
im.show()

