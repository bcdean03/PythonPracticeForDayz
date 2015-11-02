__author__ = 'Dean'
vector_position_A = [2,2]
vector_position_B = [6,5]
radius_A = 1
radius_B = 1
velocity_A = [0, 1]
velocity_B = [-3, 0]


#vector 2 minus vector 1
def vector_subtraction(matrix_A, matrix_B):
    return [b-a for a, b in zip(matrix_A, matrix_B)]

def dot_product(vector1, vector2):
    return sum(p*q for p,q in zip(vector1, vector2))

def multiple_vector(int_var, vector):
    return [i*int_var for i in vector]

def calculate_b_in_algo():
    return 2*(dot_product(vector_subtraction(velocity_A, velocity_B),
                   vector_subtraction(vector_position_A, vector_position_B)))

def calculate_a_in_algo():
    return dot_product(vector_subtraction(velocity_A, velocity_B),
                    vector_subtraction(velocity_A, velocity_B))

def calculate_c_in_algo():
    return dot_product(vector_subtraction(vector_position_A, vector_position_B),
                    vector_subtraction(vector_position_A, vector_position_B)) - \
                    (radius_A+radius_B)**2

def calculate_a_b_c_of_algo():
    # u = b*b-4*a*c
    #if postivive have to do roots
    return calculate_b_in_algo()**2-4*calculate_a_in_algo()*calculate_c_in_algo()

print "Positive or neggative: {}".format(calculate_a_b_c_of_algo())
print "A: {}".format(calculate_a_in_algo())
print "B: {}".format(calculate_b_in_algo())
print "C: {}".format(calculate_c_in_algo())