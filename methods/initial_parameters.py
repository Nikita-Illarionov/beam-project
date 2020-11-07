from initial_data import *
from mip_functions import *


def solve_MIP():

    F = np.zeros((6, 7))
    F[0, :] = make_row(a2)
    F[1, :] = make_row(a3)
    F[2, :] = make_row(a5)
    F[3, :] = make_row(a6, adding=1/k)
    F[4, :] = derivative(make_row, l, dx=1e-3, n=2)
    F[5, :] = make_row2(l)
    A = F[:, 0:-1].copy()
    B = F[:, -1].copy()
    
    solution = np.linalg.solve(A, B)

    return get_w(*solution), get_tetta(*solution), get_Q(*solution), get_M(*solution)


def make_row(x, adding = 0):
    return np.array([_R2(x), _R3(x), _R5(x), _R6(x) - adding*E*I, _Q(x), _M(x), free(x)])

def make_row2(x):
    return np.array([1, 1, 1, 1, 1, 0, -q*(x - a2) + q*(x - a4) + P])





x = np.linspace(0,l,1000)
w_x = []
tetta_x = []
M_x = []
Q_x = []
beam = []
for el in x:
    beam.append(0)
    w_x.append(w(el))
    tetta_x.append(tetta(el))
    Q_x.append(QQ(el))
    M_x.append(MM(el))
