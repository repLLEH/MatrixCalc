class Matrix():
    def __init__(self,N,M):
         self.N_size = N    # Number of rows in the matrix
         self.M_size = M    # Number of cols in the matrix
         self.__matrix = []


    def createMatrix (self, args : list):   # take list [] of matrix elements
        if(self.N_size * self.M_size == len(args)):
            for i in range(self.N_size):
                self.__matrix.append([])
                for j in range(self.M_size):
                    self.__matrix[i].append(args[j+self.M_size*i])
        else:
            print("the number of list items does not match the size of the matrix")


    def printMatrix(self):
        for rows in self.__matrix:
            print(*rows)
        print("")

    def __add__(self, other):
        result=Matrix(self.N_size,self.M_size)
        for i in range(self.N_size):
            result.__matrix.append([])
            for j in range(self.M_size):
                result.__matrix[i].append(self.__matrix[i][j]+other.__matrix[i][j])
        return result


    def __str__(self):
        self.printMatrix()
        return ""

    def __multipleMatrix(self,iterCount,firstElem,secondElem):
        result=0
        for i in range(iterCount):
            result += firstElem * secondElem
        return result

    def __mul__(self, other):
        if(type(other) is int):
            result = Matrix(self.N_size, self.M_size)
            for rows in range(self.N_size):
                result.__matrix.append([])
                for cols in range(self.M_size):
                    result.__matrix[rows].append(self.__matrix[rows][cols]*other)
            return result
        else:
            result = Matrix(self.N_size, other.M_size)
            for rows in range(self.N_size):
                result.__matrix.append([])
                for cols in range(other.M_size):
                    result.__matrix[rows].append(0)

            for i in range(self.N_size):
                for j in range(other.M_size):
                    for q in range(self.M_size):
                        result.__matrix[i][j] += self.__matrix[i][q] * other.__matrix[q][j]
            return result

