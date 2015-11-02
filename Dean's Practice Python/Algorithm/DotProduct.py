__author__ = 'Dean'
vector_position_A = [2,2]
vector_position_B = [6,5]

velocity_A = [0, 1]
velocity_B = [-3, 0]


#vector 2 minues vector 1
def vector_subtraction(matrix_A, matrix_B):
    return [b-a for a, b in zip(matrix_A, matrix_B)]

def dot_product(vector1, vector2):
    return sum(p*q for p,q in zip(vector1, vector2))

def multiple_vector(int_var, vector):
    return [i*int_var for i in vector]

def calculate_a_in_algo():
    print((vector_subtraction(velocity_A, velocity_B)))
    s = 2*(dot_product(vector_subtraction(velocity_A, velocity_B),
                   vector_subtraction(vector_position_A, vector_position_B)))
    return s

def calculate_b_in_algo():
    pass

print calculate_a_in_algo()