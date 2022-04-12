class Matrix:
    def __init__(self, *data):
        self.data = data
        self.size = [len(data), len(data[0])]
    
    def __repr__(self):
        return f"Matrix{self.data}"
    
    def __add__(self, other):
        assert self.size == other.size, "크기가 다릅니다."

        result = [] 
        for i in range(len(self.data)):
            tmp = []
            for j in range(len(self.data[0])):
                tmp.append(self.data[i][j] + other.data[i][j])
            result.append(tmp)
        
        return Matrix(result)

            

    def __sub__(self, other):
        assert self.size == other.size, "크기가 다릅니다."

        result = []
        for i in range(len(self.data)):
            tmp = []
            for j in range(len(self.data[0])):
                tmp.append(self.data[i][j] - other.data[i][j])
            result.append(tmp)
        
        return Matrix(result) 

        
    def __mul__(self, other):
        if type(other) == Matrix:
            assert self.size[1] == other.size[0], "곱셉이 불가능합니다."

            result = []
            for zero in range(self.size[0]):
                result.append([0] * other.size[1])               

            for i in range(self.size[0]):
                for j in range(other.size[1]): 
                    for k in range(self.size[1]):
                        result[i][j] += self.data[i][k] * other.data[k][j]

            return Matrix(result)
        
        else:            
            result = []
            for i in range(len(self.data)):
                tmp = []

                for j in range(len(self.data[0])):
                    tmp.append(self.data[i][j]*other)
                result.append(tmp)

            return Matrix(result) 
            

    def __rmul__(self, other):
        result = []
        for i in range(len(self.data)):
            tmp = []
            for j in range(len(self.data[0])):
                tmp.append(self.data[i][j]*other)
            result.append(tmp)

        return Matrix(result) 