import math
import numpy as np

#Author: Valentina Di Marco

####################################################################
# This code converts the Amplitude of the Power Spectral Density
# to the one used by PTASimulates. It takes the values of
# the log amplitudes (logA_red) for a set of pulsars,
# and the spectral index (gamma_red) and gives a dictionary
# with the new values of the log amplitude (P0) for a certain value
# of the corner frequency f_c
####################################################################



####
#Importing files
####


filename_A = "logA_red"
data_logA = {}

# Open the file with the values of the log amplitude
with open(filename_A, 'r') as file:
    # Read the contents of the file
    contents = file.readlines()

# Process the contents and create the dictionary
for line in contents:
    # Split each line by comma
    elements = line.strip().split(', ')
    key = elements[0]
    value = float(elements[1])
    data_logA[key] = value


filename_g = "gamma_red"
data_gamma = {}

# Open the file with the values of the spectral indexes
with open(filename_g, 'r') as file:
    # Read the contents of the file
    contents = file.readlines()

# Process the contents and create the dictionary
for line in contents:
    # Split each line by comma
    elements = line.strip().split(', ')
    key = elements[0]
    value = float(elements[1])
    data_gamma[key] = value

#######
# Define the value of the corner frequency f_c
# Create an array of the same length of the dictionaries for the corner frequencies
#######
fc_value = 0.01    
l = len(data_logA)
f_c = np.full(l, fc_value)

######
#Modify files and save
######

# Define conversion function
def conversion(logA, gamma, f_c):

    A = {}
    for key in logA:
        A[key] = 10**(logA[key])
#    print(A)
    
    P0 = {}
    for key in gamma:
        P0_long = (A[key]**2) * (f_c**(-gamma[key])) / (12 * math.pi**2)
        P0[key] = "{:.{decimal_places}e}".format(P0_long, decimal_places=2)
       # mantissa, exponent = math.frexp(P0[key])
       # new_exponent = 10 ** (math.log10(abs(mantissa)) + exponent)
       # if P0[key] < 0:
       #     new_exponent *= -1
        


        #P0_log10_int[key] = int(math.log10(P0[key]))
        #P0_log10[key] = math.log10(P0[key])
        #print(P0_log10)
        #a0[key] = round(10**(P0_log10[key]+P0_log10_int[key]), 3)
    return P0

# Call the conversion function        
P0s= conversion(data_logA, data_gamma, 0.01)

#print(P02)
#print(P0s)
#print(data_gamma)

#dA = {"J123":-16.3}
#dg = {"J123":3.4}
#t1, t2, t3 = conversion(dA, dg, 0.01)
#print(t1, t2, t3)

#print(P0s)
#print(a0s)

# Save file
filename1 = 'P0s_for_PTASim.txt'
#filename2 = 'a0s_for_PTASim.txt'
with open(filename1, 'w') as file:
    for key, value in P0s.items():
        line = f"{key}, {value}\n"
        file.write(line)
#with open(filename2, 'w') as file:
#    for key, value in a0s.items():
#        line = f"{key}, {value}\n"
#        file.write(line)
