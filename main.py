from Matrix import Matrix
from pic_converter import Pic_converter
from Neyron import NeyralNetwork

image_file= 'Pictures/test-2.png'
conv=Pic_converter(image_file)
conv.setBlockSize(2,2)
vectors_arr=conv.ImageConverting()

NeyralNet=NeyralNetwork()

# print(len(NeyralNet.weight_matrix_generator(256*2)))
# print(len(NeyralNet.weight_matrix[0]))

#print(conv.ImageConverting())

# img_arr = conv.convert(image_file)
# blocks=conv.block_division(4,4,img_arr)
#
# NeyralNet=NeyralNetwork(conv.returnBlocksCount(),blocks)
# NeyralNet.pixel_converting()
# newVector=NeyralNet.returnStandartVectorArr()
# print(len(newVector))
# print(blocks)
# A = Matrix(2,3)
# A.createMatrix([1,2,3,4,5,6])
# #A.printMatrix()
# A.matrix_transpose()
# #A.printMatrix()
#

# #print(img_raw_data)
