import matplotlib.image as img
import PIL.Image as img_open
class Pic_converter():
    def __init__(self):
        self.__file = ''
    def convert(self,file_name):
        self.__file = img_open.open(file_name, mode='r')
        #print(type(self.__file))
        self.__img_list=img.pil_to_array(self.__file)
        return self.__img_list