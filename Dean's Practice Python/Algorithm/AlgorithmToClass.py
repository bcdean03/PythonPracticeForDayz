__author__ = 'Dean'
class Algo:
    def __init__(self,pA,pB,rA,rB,vA,vB):
        self.vector_position_A = pA
        self.vector_position_B = pB
        self.radius_A = rA
        self.radius_B = rB
        self.velocity_A = vA
        self.velocity_B = vB

    #vector 2 minus vector 1
    def vector_subtraction(self, matrix_A, matrix_B):
        return [b-a for a, b in zip(matrix_A, matrix_B)]

    def dot_product(self, vector1, vector2):
        return sum(p*q for p,q in zip(vector1, vector2))

    def multiple_vector(self,int_var, vector):
        return [i*int_var for i in vector]

    def calculate_b_in_algo(self):
        return 2*(self.dot_product(self.vector_subtraction(self.velocity_A, self.velocity_B),
                       self.vector_subtraction(self.vector_position_A, self.vector_position_B)))

    def calculate_a_in_algo(self):
        return self.dot_product(self.vector_subtraction(self.velocity_A, self.velocity_B),
                        self.vector_subtraction(self.velocity_A, self.velocity_B))

    def calculate_c_in_algo(self):
        return self.dot_product(self.vector_subtraction(self.vector_position_A, self.vector_position_B),
                        self.vector_subtraction(self.vector_position_A, self.vector_position_B)) - \
                        (self.radius_A+self.radius_B)**2

    def calculate_a_b_c_of_algo(self):
        # u = b*b-4*a*c
        #if postivive have to do roots
        return self.calculate_b_in_algo()**2-4*self.calculate_a_in_algo()*self.calculate_c_in_algo()
    def printAlgo(self):
        print "Positive or negative: {}".format(self.calculate_a_b_c_of_algo())
        print "A: {}".format(self.calculate_a_in_algo())
        print "B: {}".format(self.calculate_b_in_algo())
        print "C: {}".format(self.calculate_c_in_algo())