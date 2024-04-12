# I couldn't get the py file to work so all functions are here instead.
def utility(x, alpha):
    ### Takes values for x1, x2, and alpha and calculates the utility
    x1, x2 = x
    u = (x1**(alpha)) * (x2**(1-alpha))
    return u

def demand_x1(p1, p2, omega1, omega2, alpha):
    ### Takes prices, endowments, and alpha and returns the individuals demand for x1
    y = (alpha/p1)*(p1*omega1 + p2*omega2)
    return y

def demand_x2(p1, p2, omega1, omega2, alpha):
    ### Takes prices, endowments, and alpha and returns the individuals demand for x2
    y = ((1-alpha)/p2)*(p1*omega1 + p2*omega2)
    return y

def error(x_A, x_B, omega_A, omega_B):
    ### Takes the demand and endowments from both individual and calculates the error in the market clearing condition
    y = abs(x_A - omega_A + x_B - omega_B)
    return y

def objective_function_Q3(p1):
    ### Takes p1 and calculates the error in the market clearing condition for good 1
    x_1A = demand_x1(p1, p2, omega_A1, omega_A2, alpha)
    x_1B = demand_x1(p1, p2, omega_B1, omega_B2, beta)
    return abs(error(x_1A, x_1B, omega_A1, omega_B1))

def objective_function_Q4(p1):
    ### Takes p1 and calculates the utility of person A
    x_1B = demand_x1(p1, p2, omega_B1, omega_B2, beta)
    x_2B = demand_x2(p1, p2, omega_B1, omega_B2, beta)
    return -utility((max(0,1-x_1B), max(0,1-x_2B)), alpha)

def constraint_func_Q5(x):
    ### Takes a set of x1 and x2 and checks whether person B's utility is at least the same as with his endowment
    x1_A, x2_A = x[:2]
    y = utility((max(0,1-x1_A), max(0,1-x2_A)), beta) - utility((omega_B1, omega_B2), beta)
    return y

def objective_func_Q5(x):
    ### Takes x1 and x2 and calucaltes the utility of person A
    x1_A, x2_A = x[:2]
    return -utility((x1_A, x2_A), alpha)

def totalUtility(x):
    ### Takes x1 and x2 for person A and returns the total utility of both person A and B
    x1_A, x2_A = x[:2]
    y = utility((x1_A, x2_A), alpha) + utility((1-x1_A, 1-x2_A), beta)
    return -y