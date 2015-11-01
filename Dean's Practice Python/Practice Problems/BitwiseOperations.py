__author__ = 'Dean'
'''
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

#to put binary numbers, put 0b in front
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11
'''
one = 0b1
two = 0b10
three = 0b11
four  = 0b100
five  = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print bin(one) #bin() to print the string binary representation
print bin(9000)
print one

print hex(15)

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)
#The second arguement is what base number you the string is in
print int("0xff", 16)

#and operator (&) -> returns a binary number with 1 in the position
#where both of the binary numbers had a 1
print bin(0b1110 & 0b101)

#or operator (|)-> returns a binary number with 1 in the position
#where either of the binary numbers had a 1
print bin(0b101010 | 0b1111)

#XOR operator (^) -> returns a binary number with 1 in the position
#where only 1 of the binary numbers had a 1
print bin(0b101010 ^ 0b1111)

def check_bit4(input):
    if input & 0b1000 > 0:
        return "on"
    return "off"
'''
In the editor is a variable, a. Use a bitmask and the value
a in order to achieve a result where the third bit from the right of a is turned on.
'''
a = 0b10111011
print bin(a | 0b100)


def flip_bit(number, n):
    mask = (0b1 << n)
    result = number ^ mask
    return bin(result)

print flip_bit(0b111, 2)