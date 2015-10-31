__author__ = 'Dean'
'''
When you try to access an attribute from an instance of a class, it
first looks at its instance namespace. If it finds the attribute,
it returns the associated value. If not, it then looks in the class namespace and
returns the attribute (if it’s present, throwing an error otherwise). For example:
'''