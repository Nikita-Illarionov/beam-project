def N1(x): 
    return 1 - 3*(x)**2 + 2*(x)**3

def N2(x): 
    return 3*(x)**2 - 2*(x)**3

def M1(x): 
    return x*L*(1-x)**2

def M2(x): 
    return x*L*(x)**2 - x*x*L

def dN1(x): 
    return - 6*(x)/L + 6/L*(x)**2

def dN2(x): 
    return 6*(x)/L - 6/L*(x)**2

def dM1(x): 
    return (1-4*x+3*x**2)

def dM2(x): 
    return 3*(x)**2 - 2*x

def d2N1(x): 
    return (-6 + 12*x)/L**2

def d2N2(x): 
    return (6 - 12*x)/L**2

def d2M1(x): 
    return -4/L + 6*x/L

def d2M2(x): 
    return -2/L + 6*x/L

def d3N1(x): 
    return  12/L**3

def d3N2(x): 
    return -12/L**3

def d3M1(x): 
    return 6/L**2

def d3M2(x): 
    return 6/L**2

def w(x):
    i = int(x/L)
    ksi = (x-i*L)/L
    
    return N1(ksi)*solution[2*i] + M1(ksi)*solution[2*i+1] + N2(ksi)*solution[2*i+2] + M2(ksi)*solution[2*i+3]


def tetta(x):
    i = int(x/L)
    ksi = (x-i*L)/L
    
    return dN1(ksi)*solution[2*i] + dM1(ksi)*solution[2*i+1] + dN2(ksi)*solution[2*i+2] + dM2(ksi)*solution[2*i+3]

def moment(x):
    i = int(x/L)
    ksi = (x-i*L)/L
    
    return E*I*(d2N1(ksi)*solution[2*i] + d2M1(ksi)*solution[2*i+1] + d2N2(ksi)*solution[2*i+2] + d2M2(ksi)*solution[2*i+3])


def Q(x):
    i = int(x/L)
    ksi = (x-i*L)/L
    
    return E*I*(d3N1(ksi)*solution[2*i] + d3M1(ksi)*solution[2*i+1] + d3N2(ksi)*solution[2*i+2] + d3M2(ksi)*solution[2*i+3])

