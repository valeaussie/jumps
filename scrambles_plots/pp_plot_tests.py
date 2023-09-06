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

OS_no_jumps_2 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_norednoise/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS_no_jumps_2.append(OS_value)
OS_no_jumps_2 = np.array(OS_no_jumps_2)

OS_huge_jumps = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_small_jumps_with_starting_times/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS_huge_jumps.append(OS_value)
OS_huge_jumps = np.array(OS_huge_jumps)

OS_small_jumps = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_small_jumps_norednoise/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_small_jumps.append(OS_value)
OS_small_jumps = np.array(OS_small_jumps)

OS_big_jumps = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_big_jumps/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_big_jumps.append(OS_value)
OS_big_jumps = np.array(OS_big_jumps)

OS_tiny_jumps = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_tiny_jumps/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_tiny_jumps.append(OS_value)
OS_tiny_jumps = np.array(OS_tiny_jumps)

# Sort the OS values
idx_no_jumps = np.argsort(OS_no_jumps)
OS_no_jumps_sorted = OS_no_jumps[idx_no_jumps]

idx_no_jumps_2 = np.argsort(OS_no_jumps_2)
OS_no_jumps_sorted_2 = OS_no_jumps[idx_no_jumps_2]

idx_huge_jumps = np.argsort(OS_huge_jumps)
OS_huge_jumps_sorted = OS_huge_jumps[idx_huge_jumps]

idx_small_jumps = np.argsort(OS_small_jumps)
OS_small_jumps_sorted = OS_small_jumps[idx_small_jumps]

idx_big_jumps = np.argsort(OS_big_jumps)
OS_big_jumps_sorted = OS_big_jumps[idx_big_jumps]

idx_tiny_jumps = np.argsort(OS_tiny_jumps)
OS_tiny_jumps_sorted = OS_big_jumps[idx_tiny_jumps]

# Calculate CDF and real p-value
cdf_small = np.arange(1, len(OS_small_jumps_sorted) + 1) / len(OS_small_jumps_sorted)
p_real_small = 1 - cdf_small

cdf_huge = np.arange(1, len(OS_huge_jumps_sorted) + 1) / len(OS_huge_jumps_sorted)
p_real_huge = 1 - cdf_huge

cdf_nojumps = np.arange(1, len(OS_no_jumps_sorted) + 1) / len(OS_no_jumps_sorted)
p_real_nojumps = 1 - cdf_nojumps

cdf_nojumps_2 = np.arange(1, len(OS_no_jumps_sorted_2) + 1) / len(OS_no_jumps_sorted_2)
p_real_nojumps_2 = 1 - cdf_nojumps_2

cdf_big = np.arange(1, len(OS_big_jumps_sorted) + 1) / len(OS_big_jumps_sorted)
p_real_big = 1 - cdf_big

# Import scrambles
p_est_unsorted_small = []
p_est_unsorted_big = []
p_est_unsorted_huge = []
p_est_unsorted_nojumps = []
p_est_unsorted_nojumps_2 = []
p_est_unsorted_tiny = []

for i in range(rang):
    # import the data for the scrambles
    scrambles_file_path_small = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_small_jumps_norednoise/output/real_{i}/scrambles.txt'
    scrambles_file_path_huge = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_small_jumps_with_starting_times/output/real_{i}/scrambles.txt'
    scrambles_file_path_nojumps = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_with_starting_times/output/real_{i}/scrambles.txt'
    scrambles_file_path_nojumps_2 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_norednoise/output/real_{i}/scrambles.txt'
    scrambles_file_path_big = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_big_jumps/output/real_{i}/scrambles.txt'
    scrambles_file_path_tiny = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_tiny_jumps/output/real_{i}/scrambles.txt'

    with open(scrambles_file_path_small, 'r') as scrambles_file_small:
        contents_small = scrambles_file_small.readlines()
    scramble_np_small = np.array([float(line.strip()) for line in contents_small])
    scramble_np_small.sort()

    with open(scrambles_file_path_huge, 'r') as scrambles_file_huge:
        contents_huge = scrambles_file_huge.readlines()
    scramble_np_huge = np.array([float(line.strip()) for line in contents_huge])
    scramble_np_huge.sort()

    with open(scrambles_file_path_nojumps, 'r') as scrambles_file_nojumps:
        contents_nojumps = scrambles_file_nojumps.readlines()
    scramble_np_nojumps = np.array([float(line.strip()) for line in contents_nojumps])
    scramble_np_nojumps.sort()

    with open(scrambles_file_path_nojumps_2, 'r') as scrambles_file_nojumps_2:
        contents_nojumps_2 = scrambles_file_nojumps_2.readlines()
    scramble_np_nojumps_2 = np.array([float(line.strip()) for line in contents_nojumps_2])
    scramble_np_nojumps_2.sort()
    
    with open(scrambles_file_path_big, 'r') as scrambles_file_big:
        contents_big = scrambles_file_big.readlines()
    scramble_np_big = np.array([float(line.strip()) for line in contents_big])
    scramble_np_big.sort()

    with open(scrambles_file_path_tiny, 'r') as scrambles_file_tiny:
        contents_tiny = scrambles_file_tiny.readlines()
    scramble_np_tiny = np.array([float(line.strip()) for line in contents_tiny])
    scramble_np_tiny.sort()

    # calculate the estimated p-value 
    p_val_small = 1 - stats.percentileofscore(scramble_np_small, OS_small_jumps[i])/100
    p_est_unsorted_small.append(p_val_small)

    p_val_huge = 1 - stats.percentileofscore(scramble_np_huge, OS_huge_jumps[i])/100
    p_est_unsorted_huge.append(p_val_huge)
    
    p_val_nojumps = 1 - stats.percentileofscore(scramble_np_nojumps, OS_no_jumps[i])/100
    p_est_unsorted_nojumps.append(p_val_nojumps)

    p_val_nojumps_2 = 1 - stats.percentileofscore(scramble_np_nojumps_2, OS_no_jumps_2[i])/100
    p_est_unsorted_nojumps_2.append(p_val_nojumps_2)

    p_val_big = 1 - stats.percentileofscore(scramble_np_big, OS_big_jumps[i])/100
    p_est_unsorted_big.append(p_val_big)

    p_val_tiny = 1 - stats.percentileofscore(scramble_np_tiny, OS_tiny_jumps[i])/100
    p_est_unsorted_tiny.append(p_val_tiny)


p_est_unsorted_small = np.array(p_est_unsorted_small)
p_est_small = np.sort(p_est_unsorted_small)
p_est_small = p_est_small[::-1]

p_est_unsorted_huge = np.array(p_est_unsorted_huge)
p_est_huge = np.sort(p_est_unsorted_huge)
p_est_huge = p_est_huge[::-1]

p_est_unsorted_nojumps = np.array(p_est_unsorted_nojumps)
p_est_nojumps = np.sort(p_est_unsorted_nojumps)
p_est_nojumps = p_est_nojumps[::-1]

p_est_unsorted_nojumps_2 = np.array(p_est_unsorted_nojumps_2)
p_est_nojumps_2 = np.sort(p_est_unsorted_nojumps_2)
p_est_nojumps_2 = p_est_nojumps_2[::-1]

p_est_unsorted_big = np.array(p_est_unsorted_big) 
p_est_big = np.sort(p_est_unsorted_big)
p_est_big = p_est_big[::-1] 

p_est_unsorted_tiny = np.array(p_est_unsorted_tiny) 
p_est_tiny = np.sort(p_est_unsorted_tiny)
p_est_tiny = p_est_tiny[::-1] 


print(p_est_big)

# 45 degrees line
x = np.arange(0.99, -0.01, -0.01)
y = np.arange(0.99, -0.01, -0.01)


# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, p_est_small, label='small jumps no RN equal start times')
plt.plot(x, p_est_nojumps_2, label='no jumps no RN equal start times') 
#plt.plot(x, p_est_nojumps, label='no jumps with RN and unequal start times')
#plt.plot(x, p_est_huge, label='small jumps with RN and unequal start times')
#plt.plot(x, p_est_tiny, label=r'$~10^{-8}$ jumps')
plt.plot(x, y)


# Add labels and title
plt.xlabel(r'$p_{\mathrm{true}}$', fontsize=18)
plt.ylabel(r'$p_{\mathrm{estimated}}$', fontsize=18)
#plt.ylim(1e-2, 1)
#plt.xlim(1e-2, 1)
plt.ylim(0, 1)
plt.xlim(0, 1)


# Add legend
plt.legend()

# Display
#plt.grid(True)
plt.show()
