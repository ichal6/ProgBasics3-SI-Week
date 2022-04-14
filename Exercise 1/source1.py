def my_function(a): # a - local | create
    b = a - 2 #b - local | create
    return b #a and b - destroyed 
# if we assign value 1 to c variable then my_function don't start. If we need a start function after change we can change condition if c > 2 to if c > 0
c = 3 #c - global | create 

if c > 2:
    d = my_function(5) # d - global | create
    print(d)

# c and d - destroyed