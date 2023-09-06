import matplotlib.pyplot as plt
import numpy as np
import json
from scipy import stats 

rang = 100

# Import data for the unscrambled optimal statistic
OS_no_jumps = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_norednoise/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS_no_jumps.append(OS_value)
OS_no_jumps = np.array(OS_no_jumps)

# Sort the OS values
idx_no_jumps = np.argsort(OS_no_jumps)
OS_no_jumps_sorted = OS_no_jumps[idx_no_jumps]

# Calculate CDF and real p-value
cdf_nojumps = np.arange(1, len(OS_no_jumps_sorted) + 1) / len(OS_no_jumps_sorted)
p_real_nojumps = 1 - cdf_nojumps

# Import scrambles
p_est_unsorted_nojumps = []
scramb = []
for i in range(rang):
    # import the data for the scrambles
    scrambles_file_path_nojumps = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_norednoise/output/real_{i}/scrambles.txt'

    with open(scrambles_file_path_nojumps, 'r') as scrambles_file_nojumps:
        contents_nojumps = scrambles_file_nojumps.readlines()
    scramble_np_nojumps = np.array([float(line.strip()) for line in contents_nojumps])

    scramb.append(scramble_np_nojumps)
    scramble_np_nojumps.sort()
    # calculate the estimated p-value )
    p_val_nojumps = 1 - stats.percentileofscore(scramble_np_nojumps, OS_no_jumps[i]) / 100
    p_est_unsorted_nojumps.append(p_val_nojumps)
    
p_est_unsorted_nojumps = np.array(p_est_unsorted_nojumps)
p_est_nojumps = np.sort(p_est_unsorted_nojumps)

# 45 degrees line
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

# Plot
plt.figure(figsize=(8, 6))
#plt.plot(x, p_est_nojumps, label='no jumps with RN and unequal start times')
#plt.plot(x, y)
# Add labels and title
#plt.xlabel(r'$p_{\mathrm{true}}$', fontsize=18)
#plt.ylabel(r'$p_{\mathrm{estimated}}$', fontsize=18)
#plt.ylim(0, 1)
#plt.xlim(0, 1)

plt.hist(scramb[1], density=True, label='distribution of scramble number 1')
plt.hist(scramb[76], density=True, label='distribution od scramble number 76')
plt.axvline(x=OS_no_jumps_sorted[0])
plt.axvline(x=OS_no_jumps_sorted[99])
plt.hist(OS_no_jumps, density=True, label='distribution of OS')

# Add legend
plt.legend()

# Display
plt.show()
