from PIL import Image  # need to install PIL
import sys

# User input image file name
# ex) python image.py pic.jpg
if len(sys.argv)!=2:
    print("Image file name needed")
    sys.exit()

i = Image.open(sys.argv[1])

# fixed size since LCD size is fixed (320 * 240)
width=320
height=240

# .h file would be created (the header file only include rgb565 format array)
filename=sys.argv[1].split('.',1)[0];
file = open(filename+".h","w")
file.write("const u16 "+filename+"["+str(width*height)+"] = {");

im=i.resize((width,height), Image.NEAREST) # https://www.daniweb.com/software-development/python/code/216637/resize-an-image-python
pixels = im.load()

# write pixel info as rgb565 format to header file
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        hexrgb=hex((((cpixel[0]&0xf8)>>3)<<11)|(((cpixel[1]&0xfc)>>2)<<5)|(((cpixel[2]&0xf8)>>3)))
        file.write(hexrgb)
        if(x*height+y!=width*height-1):
            file.write(',')

# close
file.write("};")
print(filename+".h is successfully created!")
file.close()

