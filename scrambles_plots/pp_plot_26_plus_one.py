import matplotlib.pyplot as plt
import numpy as np
import json
from scipy import stats 

#plt.style.use('plot_style.txt') 

rang = 100

# Import data for the unscrambled optimal statistic
OS_J0030 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0030+0451_and_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS_J0030.append(OS_value)
OS_J0300 = np.array(OS_J0030)

OS_J0125 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0125-2327_and_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS_J0125.append(OS_value)
OS_J0125 = np.array(OS_J0125)

OS_J0614 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0614-3329_and_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value  = data_dict.get('OS')
        OS_J0614.append(OS_value)
OS_J0614 = np.array(OS_J0614)

OS_J0900 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0900-3144_and_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_J0900.append(OS_value)
OS_J0900 = np.array(OS_J0900)

OS_J1902 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J1902-5105_and_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_J1902.append(OS_value)
OS_J1982 = np.array(OS_J1902)

OS_J1933 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J1933-6211_and_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_J1933.append(OS_value)
OS_J1933 = np.array(OS_J1933)


OS_26_dr2 = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/26_DR2_no_start_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_26_dr2.append(OS_value)
OS_26_dr2J1933 = np.array(OS_26_dr2)

OS_26_dr2_late = []
for i in range(rang):
    OS_file_path = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/26_DR2_late_time/output/real_{i}/OS.txt'
    with open(OS_file_path, 'r') as OS_file:
        contents = OS_file.read()
        data_dict = json.loads(contents)
        OS_value = data_dict.get('OS')
        OS_26_dr2_late.append(OS_value)
OS_26_dr2_lateJ1933 = np.array(OS_26_dr2_late)


# Import scrambles
p_est_unsorted_J0030 = []
p_est_unsorted_J0125 = []
p_est_unsorted_J0614 = []
p_est_unsorted_J0900 = []
p_est_unsorted_J1902 = []
p_est_unsorted_J1933 = []
p_est_unsorted_26_dr2 = []
p_est_unsorted_26_dr2_late = []
for i in range(rang):
    # import the data for the scrambles
    scrambles_file_path_J0030 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0030+0451_and_DR2_no_start_time//output/real_{i}/scrambles.txt'
    scrambles_file_path_J0125 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0125-2327_and_DR2_no_start_time/output/real_{i}/scrambles.txt'
    scrambles_file_path_J0614 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0614-3329_and_DR2_no_start_time/output/real_{i}/scrambles.txt'
    scrambles_file_path_J0900 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J0900-3144_and_DR2_no_start_time/output/real_{i}/scrambles.txt'
    scrambles_file_path_J1902 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J1902-5105_and_DR2_no_start_time/output/real_{i}/scrambles.txt'
    scrambles_file_path_J1933 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/J1933-6211_and_DR2_no_start_time/output/real_{i}/scrambles.txt'
    scrambles_file_path_26_dr2 = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/26_DR2_no_start_time/output/real_{i}/scrambles.txt'
    scrambles_file_path_26_dr2_late = f'/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/26_DR2_late_time/output/real_{i}/scrambles.txt'

    with open(scrambles_file_path_J0030, 'r') as scrambles_file_J0030:
        contents_J0030 = scrambles_file_J0030.readlines()
    scramble_np_J0030 = np.array([float(line.strip()) for line in contents_J0030])
    
    with open(scrambles_file_path_J0125, 'r') as scrambles_file_J0125:
        contents_J0125 = scrambles_file_J0125.readlines()
    scramble_np_J0125 = np.array([float(line.strip()) for line in contents_J0125])

    with open(scrambles_file_path_J0614, 'r') as scrambles_file_J0614:
        contents_J0614 = scrambles_file_J0614.readlines()
    scramble_np_J0614 = np.array([float(line.strip()) for line in contents_J0614])

    with open(scrambles_file_path_J0900, 'r') as scrambles_file_J0900:
        contents_J0900 = scrambles_file_J0900.readlines()
    scramble_np_J0900 = np.array([float(line.strip()) for line in contents_J0900])

    with open(scrambles_file_path_J1902, 'r') as scrambles_file_J1902:
        contents_J1902 = scrambles_file_J1902.readlines()
    scramble_np_J1902 = np.array([float(line.strip()) for line in contents_J1902])
    
    with open(scrambles_file_path_J1933, 'r') as scrambles_file_J1933:
        contents_J1933 = scrambles_file_J1933.readlines()
    scramble_np_J1933 = np.array([float(line.strip()) for line in contents_J1933])

    with open(scrambles_file_path_26_dr2, 'r') as scrambles_file_26_dr2:
        contents_26_dr2 = scrambles_file_26_dr2.readlines()
    scramble_np_26_dr2 = np.array([float(line.strip()) for line in contents_26_dr2])

    with open(scrambles_file_path_26_dr2_late, 'r') as scrambles_file_26_dr2_late:
        contents_26_dr2_late = scrambles_file_26_dr2_late.readlines()
    scramble_np_26_dr2_late = np.array([float(line.strip()) for line in contents_26_dr2_late])


    # calculate the estimated p-value 
    t_stat_J0030, p_val_J0030 = stats.ttest_1samp(scramble_np_J0030, OS_J0030[i])
    p_est_unsorted_J0030.append(p_val_J0030)

    t_stat_J0125, p_val_J0125 = stats.ttest_1samp(scramble_np_J0125, OS_J0125[i])
    p_est_unsorted_J0125.append(p_val_J0125)
    
    t_stat_J0614, p_val_J0614 = stats.ttest_1samp(scramble_np_J0614, OS_J0614[i])
    p_est_unsorted_J0614.append(p_val_J0614)

    t_stat_J0900, p_val_J0900 = stats.ttest_1samp(scramble_np_J0900, OS_J0900[i])
    p_est_unsorted_J0900.append(p_val_J0900)

    t_stat_J1902, p_val_J1902 = stats.ttest_1samp(scramble_np_J1902, OS_J1902[i]) 
    p_est_unsorted_J1902.append(p_val_J1902)

    t_stat_J1933, p_val_J1933 = stats.ttest_1samp(scramble_np_J1933, OS_J1933[i])
    p_est_unsorted_J1933.append(p_val_J1933)

    t_stat_26_dr2, p_val_26_dr2 = stats.ttest_1samp(scramble_np_26_dr2, OS_26_dr2[i])
    p_est_unsorted_26_dr2.append(p_val_26_dr2)

    t_stat_26_dr2_late, p_val_26_dr2_late = stats.ttest_1samp(scramble_np_26_dr2_late, OS_26_dr2_late[i])
    p_est_unsorted_26_dr2_late.append(p_val_26_dr2_late)


p_est_unsorted_J0030 = np.array(p_est_unsorted_J0030)
p_est_J0030 = np.sort(p_est_unsorted_J0030)
p_est_J0030 = p_est_J0030[::-1]

p_est_unsorted_J0125 = np.array(p_est_unsorted_J0125)
p_est_J0125 = np.sort(p_est_unsorted_J0125)
p_est_J0125 = p_est_J0125[::-1]

p_est_unsorted_J0614 = np.array(p_est_unsorted_J0614)
p_est_J0614 = np.sort(p_est_unsorted_J0614)
p_est_J0614 = p_est_J0614[::-1]

p_est_unsorted_J0900 = np.array(p_est_unsorted_J0900)
p_est_J0900 = np.sort(p_est_unsorted_J0900)
p_est_J0900 = p_est_J0900[::-1]

p_est_unsorted_J1902 = np.array(p_est_unsorted_J1902) 
p_est_J1902 = np.sort(p_est_unsorted_J1902)
p_est_J1902 = p_est_J1902[::-1] 

p_est_unsorted_J1933 = np.array(p_est_unsorted_J1933) 
p_est_J1933 = np.sort(p_est_unsorted_J1933)
p_est_J1933 = p_est_J1933[::-1] 

p_est_unsorted_26_dr2 = np.array(p_est_unsorted_26_dr2) 
p_est_26_dr2 = np.sort(p_est_unsorted_26_dr2)
p_est_26_dr2 = p_est_26_dr2[::-1] 

p_est_unsorted_26_dr2_late = np.array(p_est_unsorted_26_dr2_late) 
p_est_26_dr2_late = np.sort(p_est_unsorted_26_dr2_late)
p_est_26_dr2_late = p_est_26_dr2_late[::-1] 

# 45 degrees line
x = np.arange(0.99, -0.01, -0.01)
y = np.arange(0.99, -0.01, -0.01)


# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, p_est_J0030, label='J0030')
plt.plot(x, p_est_J0125, label='J0125')
plt.plot(x, p_est_J0614, label='J0614')
plt.plot(x, p_est_J0900, label='J0900')
plt.plot(x, p_est_J1902, label='J1902')
plt.plot(x, p_est_J1933, label='J1933')
plt.plot(x, p_est_26_dr2, label='26_dr2')
plt.plot(x, p_est_26_dr2_late, label='26_dr2_late')
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
