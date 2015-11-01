__author__ = 'Dean'
cubes = range(1,6,2) #[x*1 for x in range(1, 6)]
m={"a":10,"b":23,}
print cubes
print filter(lambda x: x % 3 == 0, cubes)
print reduce(lambda x, y: x + y, cubes)
print(map(lambda x: m[x] + 10, m))

def make_incrementor (n):
    return lambda x: x + n
def new_try(n):
    return lambda x: x + n*3

f = make_incrementor(2)
g = make_incrementor(6)
print f(25)