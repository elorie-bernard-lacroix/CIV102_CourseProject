'''
CIV102 Course Project
Last Modified 2022-11-10
'''

def internal_forces(cut): # step 1
    '''
    Calculate internal forces, Shear Force, 𝑉(𝑥), and Bending Moment, 𝑀(𝑥), from a 400 N train 
    a. Under train loading, consideration must be made to account for the train being at multiple 
    locations (I.e., moving) along the bridge 
    [𝑉(𝑥),𝑀(𝑥)]=𝑆𝑜𝑙𝑣𝑖𝑛𝑔 𝑒𝑞𝑢𝑎𝑡𝑖𝑜𝑛𝑠 𝑜𝑓 𝑒𝑞𝑢𝑖𝑙𝑖𝑏𝑟𝑖𝑢𝑚

    Input: "cut" is the placement of the cut/location of interest for shear forces
    '''
    # declaring local variables
    global load  # placement of load
    length = 240  # length of bridge in mm

    # calculating reaction forces
    r_a, r_b  # reaction forces at both supports (a and b)
    r_b = (400*load)/length # moment equation (-400*x + r_b*length)
    r_a = 400 - r_b # vertical force equilibrium

    # calculating internal forces
    V = 0
    if cut > length:
        V = r_a - 400 + r_b
    elif cut > load:
        V = r_a - 400
    else:
        V = r_a

    M = 0
    if cut > length:
        M = 0
    elif cut > load:
        M = load*r_a - (cut-load)(r_a-400)
    else:
        M = load*r_a

    return V, M

def bridge_geometry():  #step 2
    '''
    Define bridge geometry (Design Parameters): 
    a. Define bridge cross-section shape, and parameterize dimensions: widths (𝑏), height (ℎ), 
    thickness (𝑡), ... 
    b. Define changes (if any) to cross-sectional dimensions along the length of the bridge  
    𝐶ℎ𝑜𝑜𝑠𝑒 𝑔𝑒𝑜𝑚𝑒𝑡𝑟𝑦 {𝑏(𝑥),ℎ(𝑥),𝑡(𝑥),...} 
    '''
    pass

def cross_sectional_prop():  #step 3
    '''
    Calculate cross-sectional geometric properties 
    [𝑦̅(𝑥),𝑄(𝑥),𝐼(𝑥)]=𝑓(𝑔𝑒𝑜𝑚𝑒𝑡𝑟𝑦) 
    '''
    pass

def applied_stress():  # step 4
    '''
    Calculate applied stresses  
    [𝜎𝑡𝑜𝑝(𝑥),𝜎𝑏𝑜𝑡(𝑥),𝜏𝑐𝑒𝑛𝑡(𝑥),𝜏𝑔𝑙𝑢𝑒(𝑥)]=𝑓(𝑉(𝑥),𝑀(𝑥),𝑦̅(𝑥),𝑄(𝑥),𝐼(𝑥)) 
    '''
    pass

def max_capacities():  # step 5
    '''
    Calculate material/thin plate buckling capacities 
    [𝜎𝑡𝑒𝑛𝑠(𝑥),𝜎𝑐𝑜𝑚𝑝(𝑥),𝜎𝑏𝑢𝑐𝑘(𝑥) 𝜏𝑚𝑎𝑥(𝑥),𝜏𝑔𝑙𝑢𝑒(𝑥),𝜏𝑏𝑢𝑐𝑘(𝑥)]=𝑓(𝑔𝑒𝑜𝑚𝑒𝑡𝑟𝑦,𝑚𝑎𝑡𝑒𝑟𝑖𝑎𝑙 𝑝𝑟𝑜𝑝𝑒𝑟𝑡𝑖𝑒𝑠) 
    '''
    pass

def factor_of_safety():  # step 6
    '''
    Compare applied stresses vs capacities to determine Factors of Safety (FOS) against each failure mechanism 
    𝐹𝑂𝑆𝑡𝑒𝑛𝑠𝑖𝑜𝑛(𝑥)=𝜎𝑡𝑒𝑛𝑠(𝑥) 𝜎𝑏𝑜𝑡(𝑥)⁄  
    𝐹𝑂𝑆𝑐𝑜𝑚𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛(𝑥)=𝜎𝑐𝑜𝑚𝑝(𝑥) 𝜎𝑡𝑜𝑝(𝑥)⁄  
    𝐹𝑂𝑆𝑓𝑙𝑒𝑥.𝑏𝑢𝑐𝑘1,2,3(𝑥)=𝜎𝑏𝑢𝑐𝑘1,2,3(𝑥) 𝜎𝑡𝑜𝑝(𝑥)⁄  
    𝐹𝑂𝑆𝑠ℎ𝑒𝑎𝑟(𝑥)=𝜏𝑚𝑎𝑥(𝑥) 𝜏𝑐𝑒𝑛𝑡(𝑥)⁄  
    𝐹𝑂𝑆𝑔𝑙𝑢𝑒(𝑥)=𝜏𝑔𝑙𝑢𝑒(𝑥) 𝜏𝑔𝑙𝑢𝑒(𝑥)⁄  
    𝐹𝑂𝑆𝑠ℎ𝑒𝑎𝑟.𝑏𝑢𝑐𝑘(𝑥)=𝜏𝑏𝑢𝑐𝑘(𝑥) 𝜏𝑐𝑒𝑛𝑡(𝑥)⁄  
    '''
    pass

def min_FOS():  # step 7
    '''
    Find minimum FOS. This value represents “how many” trains would fail the current design 
    a. If minimum FOS < 1, the current design will not support the given train 
    b. If minimum FOS > 1, the current design will be able to carry a heavier train. Calculate 
    maximum train weight the current design can hold. 
    '''
    pass

def SF_BM_capacities(): # step 8
    '''
    For visualization, find the Shear Force Capacities, Vfail(x), and Bending Moment Capacities, Mfail(x)  
    𝑀𝑓𝑎𝑖𝑙_𝑡𝑒𝑛𝑠(𝑥)=𝐹𝑂𝑆𝑡𝑒𝑛𝑠𝑖𝑜𝑛(𝑥)∙𝑀(𝑥) 
    𝑀𝑓𝑎𝑖𝑙_𝑐𝑜𝑚𝑝(𝑥)=𝐹𝑂𝑆𝑐𝑜𝑚𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛(𝑥)∙𝑀(𝑥) 
    𝑀𝑓𝑎𝑖𝑙_𝑏𝑢𝑐𝑘1,2,3(𝑥)=𝐹𝑂𝑆𝑓𝑙𝑒𝑥.𝑏𝑢𝑐𝑘1,2,3(𝑥)∙𝑀(𝑥) 
    𝑉𝑓𝑎𝑖𝑙_𝑠ℎ𝑒𝑎𝑟(𝑥)=𝐹𝑂𝑆𝑠ℎ𝑒𝑎𝑟(𝑥)∙𝑉(𝑥) 
    𝑉𝑓𝑎𝑖𝑙_𝑔𝑙𝑢𝑒(𝑥)=𝐹𝑂𝑆𝑔𝑙𝑢𝑒(𝑥)∙𝑉(𝑥) 
    𝑉𝑓𝑎𝑖𝑙_𝑏𝑢𝑐𝑘(𝑥)=𝐹𝑂𝑆𝑠ℎ𝑒𝑎𝑟.𝑏𝑢𝑐𝑘(𝑥)∙𝑉(𝑥)
    '''
    pass


if '__name__' == '__main__':
    load = input("starting location of train (0 ≤ xtrain ≤ 240 mm): ")

    max_capacities()
    min_FOS()

