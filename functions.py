# define a function that takes an integer and multiplies it by two

def mult2(n):
    # why are return statements necessary?
    # without the return statment, nothing  'comes out' of our function 
    return n * 2

# define another function that multiplies every number in a list by 2
def mult2_list(l):
    # iterate through every list index
    for i in range(len(l)):
        l[i] *=2
    return l

# passing by reference vs passing by value 
# PBR: we have a reference to a list l, we passed that into a function
    # the function changed the contents of the list 
    # so even when we exited out of the function, the changes persisted

# PBV: the function receives a brand new copy of the data; outside the function
    # the changes that the function makes don't persist unless we explicityly save it (return) 

# When does PBR happen and when does PBV happen? 
    # We don't have explicit control over when one happens over the other 

# Typically, we see PBR when we pass 'large' things into a function 
# Do we just pass a reference to the data structure, or copy the whole thing before passing it in? 


# anonymous functions in python which are called lambdas 
add = lambda x, y: x + y 