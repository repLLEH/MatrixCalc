from pic_converter import Pic_converter
image_file= 'Pictures/test-2.png'
conv=Pic_converter()
img_arr = conv.convert(image_file)
blocks=conv.block_division(64,64,img_arr)
print(blocks[0])
#print(img_raw_data)