import matplotlib.image as img
import math
import PIL.Image as img_open
class Pic_converter():
    def __init__(self):
        self.__file = ''
    def convert(self,file_name):
        self.__file = img_open.open(file_name, mode='r')
        #print(type(self.__file))
        self.__img_list=img.pil_to_array(self.__file)
        return self.__img_list
    def block_division(self,N,M,img_arr):
        block_width, block_height = N,M

        pixels = []
        for img in img_arr:
            for pixel in img:
                pixels.append(pixel)

        count_blocks_in_row = 256 / block_width
        count_blocks_in_column = 256 / block_height

        blocks = []

        for i in range(0, math.ceil(count_blocks_in_column)):
            first_row = i * block_height
            last_row = (i + 1) * block_height
            for j in range(0, math.ceil(count_blocks_in_row)):
                first_pix_in_row = j * block_width
                last_pix_in_row = (j + 1) * block_width
                new_block = []
                for row in range(first_row, last_row):
                    row_in_block = []
                    for pix in range(first_pix_in_row, last_pix_in_row):
                        try:
                            row_in_block.append(list(img_arr[row][pix]))
                        except:
                            pass
                    new_block.append(row_in_block)
                blocks.append(new_block)
        return blocks
