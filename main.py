'''
CIV102 Course Project
Last Modified 2022-11-10
'''

def reaction_forces():
    '''
    This function calculates the reaction forces on the bridge.
    '''

    global r_a, r_b  # reaction forces at both supports (a and b)
    r_b = (400*xtrain)/span # moment equation (-400*x + r_b*length)
    r_a = 400 - r_b # vertical force equilibrium

def shear_force(cut):
    '''
    This function takes the input, cut, and uses it to calculate the shear forve (V) at that cut.
    '''
    global xtrain  # placement of load
    global span  # length of bridge in mm
    global r_a, r_b

    V = 0
    if cut >= span:
        V = r_a - 400 + r_b
    elif cut >= xtrain:
        V = r_a - 400
    else:
        V = r_a

    return V

def bending_moment(cut):
    '''
    This function takes the input, cut, and uses it to calculate the bending moment (M) at that cut.
    '''
    global xtrain  # placement of train
    global span  # span of bridge in mm
    global r_a, r_b

    M = 0
    if cut >= span:
        M = 0
    elif cut >= xtrain:
        M = xtrain*r_a - (cut-xtrain)*(r_a-400)
    else:
        M = xtrain*r_a

    return M

def required_SF():
    '''
    This function collects the SF forces at all points necessary to plot the diagram.
    '''
    pass

def required_BM():
    pass

def plot_BMD():
    pass

def plot_SFD():
    pass

if '__name__' == '__main__':
    xtrain = input("starting location of train (0 ≤ xtrain ≤ 240 mm): ")
    span = 1200 # span of bridge in mm
