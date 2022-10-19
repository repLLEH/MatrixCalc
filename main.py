from pic_converter import Pic_converter
image_file='test-2.png'
conv=Pic_converter()
img_arr = conv.convert(image_file)
for img in img_arr:
    #print(img)
    for pixel in img:
        print(pixel)
#print(img_arr)
#print(img_raw_data)