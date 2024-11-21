import csv
import numpy as np
import matplotlib as plt
##############################################
def LoadSigmaDeltaTransitions():
    """
    Helper function loading the data sets and transforming the trajectories in it into transitions
    """
    x1_string_trajectories = []
    x2_string_trajectories = []
    x3_string_trajectories = []

    x1_small_err_string_trajectories = []
    x2_small_err_string_trajectories = []
    x3_small_err_string_trajectories = []

    x1_large_prop_err = []
    x2_large_prop_err = []
    x3_large_prop_err = []

    x1_noise_string_trajectories = []
    x2_noise_string_trajectories = []
    x3_noise_string_trajectories = []

    with open('x1V.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x1_string_trajectories.append(row[1:])

    with open('x1E.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x1_small_err_string_trajectories.append(row[1:])

    with open('x2V.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x2_string_trajectories.append(row[1:])

    with open('x2E.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x2_small_err_string_trajectories.append(row[1:])

    with open('x3V.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x3_string_trajectories.append(row[1:])

    with open('x3E.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x3_small_err_string_trajectories.append(row[1:])

    with open('x1ELarge.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x1_large_prop_err.append(row[1:])

    with open('x2ELarge.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x2_large_prop_err.append(row[1:])

    with open('x3ELarge.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x3_large_prop_err.append(row[1:])

    with open('x1Noise.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x1_noise_string_trajectories.append(row[1:])

    with open('x2Noise.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x2_noise_string_trajectories.append(row[1:])

    with open('x3Noise.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            x3_noise_string_trajectories.append(row[1:])

    x1_trajectories = []
    x2_trajectories = []
    x3_trajectories = []

    x1n_trajectories = []
    x2n_trajectories = []
    x3n_trajectories = []

    x1eLarge_trajectories = []
    x2eLarge_trajectories = []
    x3eLarge_trajectories = []

    x1_noise_trajectories = []
    x2_noise_trajectories = []
    x3_noise_trajectories = []

    for traj in x1_string_trajectories:
        x1_trajectories.append([float(num) for num in traj])

    for traj in x2_string_trajectories:
        x2_trajectories.append([float(num) for num in traj])

    for traj in x3_string_trajectories:
        x3_trajectories.append([float(num) for num in traj])

    for traj in x1_small_err_string_trajectories:
        x1n_trajectories.append([float(num) for num in traj])

    for traj in x2_small_err_string_trajectories:
        x2n_trajectories.append([float(num) for num in traj])

    for traj in x3_small_err_string_trajectories:
        x3n_trajectories.append([float(num) for num in traj])

    for traj in x1_large_prop_err:
        x1eLarge_trajectories.append([float(num) for num in traj])

    for traj in x2_large_prop_err:
        x2eLarge_trajectories.append([float(num) for num in traj])

    for traj in x3_large_prop_err:
        x3eLarge_trajectories.append([float(num) for num in traj])

    for traj in x1_noise_string_trajectories:
        x1_noise_trajectories.append([float(num) for num in traj])

    for traj in x2_noise_string_trajectories:
        x2_noise_trajectories.append([float(num) for num in traj])

    for traj in x3_noise_string_trajectories:
        x3_noise_trajectories.append([float(num) for num in traj])

    x_transitions = []
    xn_transitions = []
    xeLarge_transitions = []
    x_noise_transitions = []

    xeLarge_trajectories = []
    x_noise_trajectories = []
    x_trajectories = []
    xn_trajectories = []

    for i in range(0,len(x1_trajectories)):
        x_trajectory = []
        for j in range(0,len(x1_trajectories[i])):
            x_trajectory.append(np.array([x1_trajectories[i][j],x2_trajectories[i][j],x3_trajectories[i][j]]))
        x_trajectories.append(x_trajectory)

    for i in range(0,len(x1n_trajectories)):
        x_trajectory = []
        for j in range(0,len(x1n_trajectories[i])):
            x_trajectory.append(np.array([x1n_trajectories[i][j],x2n_trajectories[i][j],x3n_trajectories[i][j]]))
        xn_trajectories.append(x_trajectory)

    for i in range(0,len(x1eLarge_trajectories)):
        x_trajectory = []
        for j in range(0,len(x1eLarge_trajectories[i])):
            x_trajectory.append(np.array([x1eLarge_trajectories[i][j],x2eLarge_trajectories[i][j],x3eLarge_trajectories[i][j]]))
        xeLarge_trajectories.append(x_trajectory)

    for i in range(0,len(x1_noise_trajectories)):
        x_trajectory = []
        for j in range(0,len(x1_noise_trajectories[i])):
            x_trajectory.append(np.array([x1_noise_trajectories[i][j],x2_noise_trajectories[i][j],x3_noise_trajectories[i][j]]))
        x_noise_trajectories.append(x_trajectory)


    for traj in x_trajectories:
        for i in range(1,len(traj)):
            t = traj[i-1]
            tp1 = traj[i]
            conc = np.concatenate((t,tp1),axis=0)
            x_transitions.append(conc)

    for traj in xn_trajectories:
        for i in range(1,len(traj)):
            t = traj[i-1]
            tp1 = traj[i]
            conc = np.concatenate((t,tp1),axis=0)
            xn_transitions.append(conc)

    for traj in xeLarge_trajectories:
        for i in range(1,len(traj)):
            t = traj[i-1]
            tp1 = traj[i]
            conc = np.concatenate((t,tp1),axis=0)
            xeLarge_transitions.append(conc)

    for traj in x_noise_trajectories:
        for i in range(1,len(traj)):
            t = traj[i-1]
            tp1 = traj[i]
            conc = np.concatenate((t,tp1),axis=0)
            x_noise_transitions.append(conc)

    return x_transitions,xn_transitions,xeLarge_transitions,x_noise_transitions

##############################################
def monitor(classifiers,x):
    """
    Helper Function that acts as a monitor keeping all the different options and looks if the transition satisfies any of the options
    """
    verdict = False
    idx = 0
    for cs in classifiers:
        if classify(cs,x):
            verdict = True
            break
        idx+=1

    return verdict,idx

##############################################
def classify(cs,x):
    """
    Helper Function that checks if the otpion, specifically an inequality system, is satisfied by the given transition x. If so it returns True else False
    """
    csx = np.dot(cs[0],x)
    if np.all(csx<=cs[1]):
        return True
    else:
        return False

##############################################
def computeJointRangeZonotop(*affine_forms):
    """
    affine_forms: list of affine forms
    """
     # Separate G and c from each affine form
    G_list = [af[0] for af in affine_forms]
    c_list = [af[1] for af in affine_forms]

    # Convert lists to numpy arrays
    G = np.array(G_list)
    c = np.array(c_list)

    #print("G:", G)
    #print("c:", c)
    
    return (G, c)

##############################################
def transformInequationSystem(Ieq,Z):
    """
    Function that is at the core of the H-Classifier method. It transforms the inequation system from the noise symbol space into the transition space.
    Ieq := Inequality set defined by matrix A and vector b. Interpretation A epsilon <= b, thus inequality system over the noise symbols
    Z := Zonotop that also describes the linear transformation of the inequality system 
    """
    G_pinv = np.linalg.pinv(Z[0]) # Moore Penrose inverse of the generator matrix G of the zonotop
    A_prime = np.dot(Ieq[0],G_pinv) # A' = AG*
    A_prime_C = np.dot(A_prime,Z[1]) # A'c
    A_prime_C_b = A_prime_C + Ieq[1] # b + A'c
    return (A_prime,A_prime_C_b)

##############################################
def SigmaDeltaClassificationUsecase():
    """
    H-Classifier method applied to a Sigma Delta modulator of third order

    The matricies from the inequation systems come as described in the corresponding paper from the leafs and their associated paths. Due to the fact
    that the symbolic simulation code that is required to generate the AACDD is in the kotlin ecosystem and there is no standardized parsing, the implementaion
    here has been done fully manual.

    ITE(1, ITE(2, (,
    x0= -0.044399999999999995 + 0.05000000000000233 e_r + -0.1 e_1 + 1.9 e_7 + 0.022199999999999998 e_10,
    x1=-0.2881+0.10000000000000635 e_r+-0.2 e_2+ 1.9 e_7+ 2.4 e_8+ 0.14405 e_10,
    x2=-0.7997+ 0.10000000000000779 e_r+ -0.20000000000000007 e_3+ 2.4 e_8+ 2.9 e_9+ 0.39985 e_10,

    ((0.0056, −0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 0.0, 0.0, 0.022199999999999998), -0.044)
    ((0.10000000000000635, 0.0, -0.2, 0.0, 0.0, 0.0, 0.0, 1.9, 2.4, 0.0, 0.14405), -0.2881)
    ((0.10000000000000779, 0.0, 0.0, -0.20000000000000007, 0.0, 0.0, 0.0, 0.0, 2.4, 2.9, 0.39985), -0.7997) 
    
    ITE(5, (,
    x0=0.044399999999999995+ 0.0500000000000023 e_r+ 0.1 e_1+ 0.022199999999999998 e_10+ 1.9 e_7,
    x1=0.2881+ 0.10000000000000622 e_r+ 2.4 e_8+ 0.2 e_2+ 0.14405 e_10+ 1.9 e_7,
    x2=0.7997+0.10000000000000758 e_r+2.4 e_8+2.9 e_9+0.39985 e_10+0.20000000000000007 e_3+0.0 e_6,
    d=True),

    ((0.0500000000000023, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 0.0, 0.0, 0.022199999999999998), 0.044399999999999995)
    ((0.10000000000000622, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 1.9, 2.4, 0.0, 0.14405), 0.2881)
    ((0.10000000000000758, 0.0, 0.0, 0.20000000000000007, 0.0, 0.0, 0.0, 0.0, 2.4, 2.9, 0.39985), 0.7997)

    Cond 5:
    0.7997 + 0.10000000000001001e_r + 2.4e_8 + 2.9e_9 + 0.89985e_10 + 0.20000000000000007e_3

    ((0.10000000000001001, 0.0, 0.0, 0.20000000000000007, 0.0, 0.0, 0.0, 0.0, 2.4, 2.9, 0.89985),0.7997)

    Cond 2
    -0.7997 + 0.10000000000001022e_r + 2.4e_8 + 2.9e_9 + 0.89985e_10 + -0.20000000000000007e_3
    ((0.10000000000001022, 0.0, 0.0, -0.20000000000000007, 0.0, 0.0, 0.0, 0.0, 2.4, 2.9, 0.89985), -0.7997)

    """
    delta = 0.5

    # Affine Constraint System
    AAf = np.array([[1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
    [-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0]])
    bAf = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]) 

    x0 = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.2,0.0,0.0,0.0],0.0)
    x1 = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0],0.0)
    x2 = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.5,0.0],0.0)

    x0kp = ([0.005+delta,-0.01,0.0,0.0,0.0,0.0,0.0,1.2,0.0,0.0,0.0222],-0.0444)
    x1kp = ([0.05+delta,0.0,-0.09,0.0,0.0,0.0,0.0,1.2,2.0,0.0,0.14405],-0.2881)
    x2kp = ([0.05+delta,0.0,0.0,-0.09,0.0,0.0,0.0,0.0,2.0,2.5,0.39985],-0.7997)

    x0pkp = ([0.005+delta,0.01,0.0,0.0,0.0,0.0,0.0,1.2,0.0,0.0,0.0222],0.0444)
    x1pkp = ([0.05+delta,0.0,0.09,0.0,0.0,0.0,0.0,1.2,2.0,0.0,0.14405],0.2881)
    x2pkp = ([0.05+delta,0.0,0.0,0.09,0.0,0.0,0.0,0.0,2.0,2.5,0.39985],0.7997)

    Z = computeJointRangeZonotop(x0,x1,x2,x0kp,x1kp,x2kp)
    Zp = computeJointRangeZonotop(x0,x1,x2,x0pkp,x1pkp,x2pkp)

    # CHI 5
    chi5 = ([0.0,0.0,0.09,0.0,0.0,0.0,0.0,2.0,2.5,0.89985],[-0.7997])
    AChi5 = np.array([
        [0.05,0.0,0.0,0.09,0.0,0.0,0.0,0.0,2.0,2.5,0.89985],
        [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
        [-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0]])
    bChi5 = np.array([-0.7997,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
    cs_chi5 = (AChi5,bChi5)
    # NEG CHI 5
    negChi5 = ([0.0,0.0,-0.09,0.0,0.0,0.0,0.0,-2.0,-2.5,-0.89985],[0.7997])

    AnegChi5 = np.array([
        [-0.05,0.0,0.0,-0.09,0.0,0.0,0.0,0.0,-2.0,-2.5,-0.89985],
        [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
        [-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0]])
    bnegChi5 = np.array([0.7997,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
    cs_negchi5 = (AnegChi5,bnegChi5)

    # CHI 2
    chi2 = ([0.0,0.0,-0.09,0.0,0.0,0.0,0.0,2.0,2.5,0.89985],[0.7997])
    
    AChi2 = np.array([
        [0.05,0.0,0.0,-0.09,0.0,0.0,0.0,0.0,2.0,2.5,0.89985],
        [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
        [-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0]])
    bChi2 = np.array([0.7997,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
    cs_chi2 = (AChi2,bChi2)

    # NEG CHI 2
    negChi2 = ([0.0,0.0,-0.09,0.0,0.0,0.0,0.0,-2.0,-2.5,-0.89985],[-0.7997])
    AnegChi2 = np.array([
        [-0.05,0.0,0.0,-0.09,0.0,0.0,0.0,0.0,-2.0,-2.5,-0.89985],
        [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
        [-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0]])
    bnegChi2 = np.array([-0.7997,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
    cs_negchi2 = (AnegChi2,bnegChi2)

    converted1 = transformInequationSystem(cs_chi5,Z)
    converted2 = transformInequationSystem(cs_negchi5,Z)

    converted3 = transformInequationSystem(cs_chi2,Zp)
    converted4 = transformInequationSystem(cs_negchi2,Zp)

    C,SPE,LPE,N = LoadSigmaDeltaTransitions()

    # 0 = In -> Out ; 1 = IN -> IN; 2 = Out -> In; 3 = Out -> Out 
    C0 = 0
    C1 = 0
    C2 = 0
    C3 = 0
    numInliersC = 0
    numOutliersC = 0
    for transition in C:
        verdict,dynamic_idx = monitor([converted1,converted2,converted3,converted4],np.array(transition))
        if verdict :
            numInliersC+=1
            match dynamic_idx:
                case 0:
                    C0 +=1
                case 1:
                    C1 +=1
                case 2:
                    C2 +=1
                case 3:
                    C3 +=1    
        else:
            numOutliersC+=1
    print("Number Inliers C: ",numInliersC)
    print("Number Outliers C: ",numOutliersC)
    print(f"Distribution: 0 - {C0} ; 1 - {C1} ; 2 - {C2} ; 3 - {C3}")


    SPE0 = 0
    SPE1 = 0
    SPE2 = 0
    SPE3 = 0
    numInliersSPE = 0
    numOutliersSPE = 0
    for transition in SPE:
        verdict,dynamic_idx = monitor([converted1,converted2,converted3,converted4],np.array(transition))
        if verdict:
            numInliersSPE+=1
            match dynamic_idx:
                case 0:
                    SPE0 += 1
                case 1:
                    SPE1 +=1
                case 2:
                    SPE2 +=1
                case 3:
                    SPE3 +=1
        else:
            numOutliersSPE+=1
    print("Number Inliers SPE: ",numInliersSPE)
    print("Number Outliers SPE: ",numOutliersSPE)
    print(f"Distribution: 0 - {SPE0} ; 1 - {SPE1} ; 2 - {SPE2} ; 3 - {SPE3}")

    LPE0 = 0
    LPE1 = 0
    LPE2 = 0
    LPE3 = 0
    numInliersLPE = 0
    numOutliersLPE = 0
    for transition in LPE:
        verdict,dynamic_idx = monitor([converted1,converted2,converted3,converted4],np.array(transition))
        if verdict:
            numInliersLPE+=1
            match dynamic_idx:
                case 0:
                    LPE0 +=1
                case 1:
                    LPE1 +=1
                case 2:
                    LPE2 +=1
                case 3:
                    LPE3 +=1
        else:
            numOutliersLPE+=1
    print("Number Inliers LPE: ",numInliersLPE)
    print("Number Outliers LPE: ",numOutliersLPE)
    print(f"Distribution: 0 - {LPE0} ; 1 - {LPE1} ; 2 - {LPE2} ; 3 - {LPE3}")

    N0 = 0
    N1 = 0
    N2 = 0
    N3 = 0
    numInliersN = 0
    numOutliersN = 0
    for transition in N:
        verdict,dynamic_idx = monitor([converted1,converted2,converted3,converted4],np.array(transition))
        if verdict:
            numInliersN+=1
            match dynamic_idx:
                case 0:
                    N0 +=1
                case 1:
                    N1 +=1
                case 2:
                    N2 +=1
                case 3:
                    N3 +=1
        else:
            numOutliersN+=1

    print("Number Inliers N: ",numInliersN)
    print("Number Outliers N: ",numOutliersN)
    print(f"Distribution: 0 - {N0} ; 1 - {N1} ; 2 - {N2} ; 3 - {N3}")


SigmaDeltaClassificationUsecase()