from initial_parameters import *
from fem_functions import *


def solve_FEM():
    M_local = np.zeros((4, 4))
    F = [N1, M1, N2, M2]
    d2F = [d2N1, d2M1, d2N2, d2M2]

    for i in range(4):
        for j in range(4):
            M_local[i,j] = (1/6)*(d2F[i](0)*d2F[j](0) + 4*d2F[i](1/2)*d2F[j](1/2) + d2F[i](1)*d2F[j](1))*E*I*L

    M_global = np.zeros((n*2+2, n*2+2))

    for z in range(n):
        for i in range(4):
            for j in range(4):
                M_global[i+2*z, j+2*z] += M_local[i, j]
    for item in [0, a2, a3, a5]:
        index = 2*int(item*n/l)
        M_global[index, :] = 0
        M_global[index, index] = 1
    M_global[1, :] = 0
    M_global[1, 1] = 1
    M_global[2*int(a6*n/l),2*int(a6*n/l)] += k


    R1 = q*L/2
    R2 = q*(L**2)/12
    R3 = q*L/2
    R4 = -q*(L**2)/12

    Rq = [R1, R2, R3, R4]

    R = np.zeros(2*n+2)

    for z in range(int(a2*n/l), int(a4*n/l) + 1):
        for i in range(4):
            R[2*z+i] += Rq[i]

    R[2*int(a2*n/l)] = 0
    R[2*int(a3*n/l)] = 0
    R[2*int(a5*n/l)] = 0
    R[2*int(end*n/l)] -= P

    R[2*int(a1*n/l)+1] -= M


    solution = np.linalg.solve(M_global, R)
