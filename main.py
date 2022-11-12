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
    

    return V

def bending_moment(cut):
    '''
    This function takes the input, cut, and uses it to calculate the bending moment (M) at that cut.
    '''
    global xtrain  # placement of train
    global span  # span of bridge in mm
    global r_a, r_b

    M = 0
    

    return M

def plot_BMD():
    pass

def plot_SFD():
    pass

if '__name__' == '__main__':
    xtrain = input("starting location of train (0 ≤ xtrain ≤ 240 mm): ")
    span = 1200 # span of bridge in mm
    load = 400/6

    d1 = xtrain + 52
    d2 = xtrain + 228
    d3 = xtrain + 392
    d4 = xtrain + 568
    d5 = xtrain + 732
    d6 = xtrain + 784

    reaction_forces()


