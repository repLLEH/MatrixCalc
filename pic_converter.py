import matplotlib.image as img
import math
import PIL.Image as img_open
import numpy
class Pic_converter():
    def __init__(self,file_name):
        self.__file_name = file_name
        self.__file = ''
        self.__img_arr=[]
        self.__vector_arr=[]
        self.__image_size=[0,0]
        self.__block_width = 0
        self.__block_height =0
        self.__img_vector_converted=[]
        self.__img_arr_conv=[]
        self.__pixel_size=0
    def __setImageSize(self):
        self.__image_size[0]=len(self.__img_np_arr[0])
        self.__image_size[1]=len(self.__img_np_arr)
    def __imgToNpArr(self):
        self.__file = img_open.open(self.__file_name, mode='r')
        self.__img_np_arr=img.pil_to_array(self.__file)
        return self.__img_np_arr

    def ImageConverting(self):
        self.__img_arr=list(self.__imgToNpArr().flat)
        self.__setImageSize()
        self.__set_pixel_size()
        self.__pixelValueTransform()
        self.__splitImageArrayIntoBlocks()
        return self.__vector_arr
    def __pixelValueTransform(self):
        new_arr=[]
        for value in self.__img_arr:
            new_value = (2 * value / 255) - 1
            new_arr.append(new_value)
        self.__img_arr_conv=new_arr
    def setBlockSize(self,width,height):
        self.__block_width=width
        self.__block_height=height
    def __set_pixel_size(self):
        self.__pixel_size=len(self.__img_np_arr[0][0])
    def __splitImageArrayIntoBlocks(self):
        #self.blocks.clear()
        count_of_blocks_in_column = math.ceil(self.__image_size[1] / self.__block_height)
        count_of_blocks_in_row = math.ceil(self.__image_size[0] / self.__block_width)

        for number_of_block_in_column in range(0, count_of_blocks_in_column):
            for number_of_block_in_row in range(0, count_of_blocks_in_row):
                new_block = []
                first_column_of_block = number_of_block_in_row * self.__block_width
                first_row_of_block = number_of_block_in_column * self.__block_height

                if number_of_block_in_row == count_of_blocks_in_row - 1:
                    rest_of_pixels = self.__image_size[0] - self.__block_width * (count_of_blocks_in_row - 1)
                    if rest_of_pixels > 0:
                        first_column_of_block -= (self.__block_width - rest_of_pixels)

                if number_of_block_in_column == count_of_blocks_in_column - 1:
                    rest_of_pixels = self.__image_size[1] - self.__block_height * (count_of_blocks_in_column - 1)
                    if rest_of_pixels > 0:
                        first_row_of_block -= (self.__block_height - rest_of_pixels)

                for number_of_row_in_block in range(0, self.__block_height):
                    for number_of_column_in_block in range(0, self.__block_width * self.__pixel_size):
                        try:
                            index = (first_row_of_block + number_of_row_in_block) * self.__image_size[
                                0] * self.__pixel_size + \
                                    (first_column_of_block * self.__pixel_size + number_of_column_in_block)
                            # print(index, first_row_of_block, number_of_row_in_block,
                            #      first_column_of_block, number_of_column_in_block)
                            # print(index)
                            new_block.append( self.__img_arr_conv[index])
                        except Exception as ex:
                            pass  # print(ex)
                # print("--- block end ---")
                self.__vector_arr.append(new_block)
