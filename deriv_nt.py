def derivative(f, a, method="central", h=0.01):
    if method == "central":
        return (f(a+h) - f(a-h)) / (2*h)
    elif method == "forward":
        return (f(a+h) - f(a)) / h
    elif method == "backward":
        return (f(a) - f(a-h)) / h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'")

# Define function here
def f(x):
    return x**3 - 4*(x**2) + 1

def Newton(x):
    '''
        Newton's method
    '''
    derive = derivative(f, x)
    return x - f(x)/derive

def test_N(x, margin=0.000006):
    '''
        x round to 4 digits
    '''
    i = 1
    while abs(f(x)) > margin:
        print ("Now trial: {}".format(i))
        print ("Input value: {}".format(x))
        x = round(Newton(x), 4)
        i = i + 1
    print("Total trial: {}".format(i))
    print("The final value is: {}".format(x))
    print("The final y is: {}".format(f(x)))