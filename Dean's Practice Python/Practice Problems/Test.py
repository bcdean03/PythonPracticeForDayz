__author__ = 'Dean'
print "hello"
print "There is nothing"

items= {0:"Paper",1:"Tabacco",2:"Lighter"}

i1 = "Paper"
i2 = 0
missing = {v: k for k, v in items.items() if v != "Paper" and v != "Lighter"}

miss = {i: "hello" for i in range(0, 10)}

print miss
print missing
