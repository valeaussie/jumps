import matplotlib.pyplot as plt
import numpy as np
import json
from scipy import stats 

rang = 100

OS = []
p_est_unsorted = []
for i in range(rang):
    # Import data for the unscrambled optimal statistic
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_with_starting_times/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS.append(OS_value)

    # Import the data for the scrambles
    scrambles_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/final_no_jumps_with_starting_times/output/real_{i}/scrambles.txt'

    with open(scrambles_file_path, 'r') as scrambles_file:
        contents = scrambles_file.readlines()
    scramble_np = np.array([float(line.strip()) for line in contents])

    # calculate the estimated p-value 
    t_stat, p_val = stats.ttest_1samp(scramble_np, OS_value)
    p_est_unsorted.append(p_val)

OS = np.array(OS)
idx = np.argsort(OS)
OS_sorted = OS[idx]

cdf = np.arange(1, len(OS_sorted) + 1) / len(OS_sorted)
p_real = 1 - cdf

p_est_unsorted = np.array(p_est_unsorted)
p_est_sorted = p_est_unsorted[idx]


print(p_est_unsorted)
print(p_est_sorted)

for i in range(rang):
    print(p_real[i])
    print(p_est_sorted[i])
    print("next")

fig, ax = plt.subplots()
#plt.hist(scramble_np, density=True)
#plt.hist(OS, density=True)
#ax.axvline(x=OS[6], color='r')
#print(OS[6])

#p_est_unsorted_ = np.array(p_est_unsorted)
#p_est = np.sort(p_est_unsorted)
#p_est = p_est_[::-1]
#p_est_sorted = p_est[idx]

# 45 degrees line
#x = np.arange(0.99, -0.01, -0.01)
#y = np.arange(0.99, -0.01, -0.01)


# Plot
#plt.figure(figsize=(8, 6))
#plt.plot(x, p_est, label='no jumps 1')
#plt.plot(x, p_est_sorted, label='no jumps 1') 
#plt.plot(x, y)


# Add labels and title
#plt.xlabel(r'$p_{\mathrm{true}}$', fontsize=18)
#plt.ylabel(r'$p_{\mathrm{estimated}}$', fontsize=18)
#plt.ylim(1e-2, 1)
#plt.xlim(1e-2, 1)


# Add legend
#plt.legend()

# Display
#plt.grid(True)
#plt.show()
