def H(x):
    return 0 if x <= 0 else 1


def _R(a):
    def iter(x):
        return (x - a)**3 * H(x - a) / 6
    return iter


_R2 = _R(a2)
_R3 = _R(a3)
_R5 = _R(a5)
_R6 = _R(a6)


def free(x):
    return -q*((x - a2)**4) * H(x - a2) / 24 + q*((x - a4)**4) * H(x - a4) / 24 - M*((x - a1)**2) * H(x - a1) / 2


def _Q(x):
    return x**3 / 6


def _M(x):
    return x**2 / 2

def get_w(R2, R3, R5, R6, Q, M_0):
    def inner(x):
        return (1/(E*I))*(R2*_R2(x) + R3*_R3(x) + R5*_R5(x) + R6*_R6(x) + Q*_Q(x) + M_0*_M(x) - free(x))
    return inner


def get_tetta(R2, R3, R5, R6, Q, M_0):
    def inner(x):
        return derivative(w, x, dx=1e-3)
    return inner


def get_Q(R2, R3, R5, R6, Q, M_0):
    def inner(x):
        return (R2*H(x-a2) + R3*H(x-a3) + R5*H(x-a5) + R6*H(x-a6) + Q + q*(x-a2)*H(x-a2) - q*(x-a4)*H(x-a4))
    return inner


def get_M(R2, R3, R5, R6, Q, M_0):
    def inner(x):
        return (R2*H(x-a2)*(x-a2) + R3*H(x-a3)*(x-a3) + R5*H(x-a5)*(x-a5) + R6*H(x-a6)*(x-a6) + Q*x + M_0 + q*((x-a2)**2)*H(x-a2)/2 - q*((x-a4)**2)*H(x-a4)/2 + M*H(x-a1))
    return inner
