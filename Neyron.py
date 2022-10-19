import random
from Matrix import Matrix
import numpy
class NeyralNetwork():
    def __init__(self,vector_arr):
        self.__block_count=0
        self.__vector_arr=[]
        self.__weight_matrix_values=[]
        self.__weight_matrix_first = []
        self.__max_allowable_error=0
        self.__input_value_vector=Matrix(0,0)
        self.__delta_x=Matrix(0,0)
        self.__input_value_vector_transporent=Matrix(0,0)
        self.__weight_matrix_first_transporent=Matrix(0,0)
        self.__alpha=0.0
        self.__input_value_vector_arr=vector_arr
        self.sum_srednekv_error=0
        self.sum_error=0
    def set_alpha(self,value):
        self.__alpha=value

    def set_max_allowable_error(self,value):
        self.__max_allowable_error=value
    def first_weight_matrix_generator(self,second_layer_neyron_count):
        self.__weight_matrix_first=Matrix(2,second_layer_neyron_count)
        for rows in range(0,2*second_layer_neyron_count):
            self.__weight_matrix_values.append(random.random())
        self.__weight_matrix_first.createMatrix(self.__weight_matrix_values)
        return self.__weight_matrix_first
    def __set_input_value_vector(self):

    def study_for_blocks(self):
        result_matrix_first=self.__weight_matrix_first*self.__input_value_vector
        self.__input_value_vector_transporent=self.__input_value_vector.matrix_transpose()
        self.__delta_x=self.__input_value_vector_transporent-self.__input_value_vector
    def weight_correction(self):
        self.__weight_matrix_first_transporent=self
    def study(self):
        while(self.sum_error>self.__max_allowable_error)

