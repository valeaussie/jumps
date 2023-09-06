import random
import numpy as np

#############################################################
#This script creates input files for PTASim using values
#for the red noise from a dictionary. All the parameters
#can be added manually at the start
#############################################################

#Author:Valentina Di Marco



def create_inp(psr_file, gammas_file, P0s_file, Ds_file, taus_file, starts_file, toaerrs_3100MHz_file, toaerrs_1400MHz_file, toaerrs_600MHz_file):

    # Open the file with the name of the pulsars
    with open(psr_file, 'r') as f:
        psr_names = f.read().splitlines()
    #count the pulsars
    num_pulsars = len(psr_names)

    # Open the file with the values of P0 for red noise
    P0s = {}
    with open(P0s_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        P0s[key] = value

    # Open the file with the values of gamma for red noise
    gammas = {}
    with open(gammas_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        gammas[key] = value

    # Open the file with the values of D_1000 for Kolmogorov DM noise
    Ds = {}
    with open(Ds_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        Ds[key] = value
        
    # Open the file with the values of tau for Kolmogorov DM noise
    taus = {}
    with open(taus_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        taus[key] = value

    # Open the file with the start times for each pulsar
    starts = {}
    with open(starts_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        starts[key] = value

    # Open the file with the time or arrivals errors for each pulsar at 600 MHz
    toaerrs_3100 = {}
    with open(toaerrs_3100MHz_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        toaerrs_3100[key] = value
        
    # Open the file with the time or arrivals errors for each pulsar at 1400 MHZ
    toaerrs_1400 = {}
    with open(toaerrs_1400MHz_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        toaerrs_1400[key] = value

    # Open the file with the time or arrivals errors for each pulsar at 600 MHz
    toaerrs_600 = {}
    with open(toaerrs_600MHz_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        toaerrs_600[key] = value

        
    ###########
    #This is where we add all the parameters
    ###########
    
    # Number of realisations and processors
    nreal = 100
    nproc = 1
    #output name
    counter = 'final-noDM-no_jumps'
    file_name = f'{num_pulsars}psr_{nreal}reals_{counter}'
    out_file_name = f'{num_pulsars}psr_{nreal}reals_{counter}.inp'

    with open(out_file_name, 'w') as f:
        # Definitions
        f.write('<define>\n')
        f.write(f'name: {file_name}\n')
        f.write(f'nproc: {nproc}\n')
        f.write(f'nreal: {nreal}\n')
        f.write('</define>\n\n')

        # Add the pulsars
        f.write('<pulsars>\n')
        for psr_name in psr_names:
            f.write(f'psr: name={psr_name}\n')
        f.write('</pulsars>\n\n')

        # Add the timing noise
        f.write('<add>\n')
        for key_P0, value_gamma, value_P0 in zip(P0s.keys(), gammas.values(), P0s.values()):
            f.write(f'tnoise: psr={key_P0},alpha=-{value_gamma},p0={value_P0},fc=0.01\n')
        f.write('</add>\n\n')

        # GW Signal
        #GW_A = 0.20e-14
        #f.write('<add>\n')
        #f.write(f'gwb: amp={GW_A}\n')
        #f.write('</add>\n\n')

        
        # Observing run
        start = 50000
        end = 58000
        cadence = 25
        f.write('<obsRun>\n')
        f.write('name: pks\n')
        f.write('tel: pks\n')
        f.write(f'start: {start}\n')
        f.write(f'finish: {end}\n')
        f.write(f'sampling: cadence={cadence}\n')
        f.write('sched: sched_similar_regsamp\n')
        f.write('</obsRun>\n\n')

        # DM noise
        #ref_freq = 1400
        #f.write('<add>\n')
        #for key_D, value_D, value_tau in zip(Ds.keys(), Ds.values(), taus.values()):
        #    f.write(f'dmvar: psr={key_D},D=[{value_tau};{ref_freq};{value_D}]\n')
        #f.write('</add>\n\n')
        
        # jumps (400 nanoseconds)
        # tot_days = end - start
        # freq_days = int(6*30.4167) #a jump every 6 months
        # num_jumps = int(tot_days/freq_days)
        # size = 2 #2 for 400 nanoseconds
        # def get_jumps(num_jumps, max_size, start, end):
        #    mjds = np.zeros(num_jumps)
        #    jumps = np.zeros(num_jumps)
        #    for j in range(num_jumps):
        #        mjds[j] = round(random.uniform(start, end))
        #        size = round(random.uniform(0, max_size), 1)
        #        sign = random.choice([-1, 1])
        #        jumps[j] = size * sign
        #    return mjds, jumps

        # mjds, sizes = get_jumps(num_jumps, size, start, end)
        # f.write('<be>\n')
        # f.write('name: be1\n')
        # for mjd, size in zip(mjds, sizes):
        #    f.write(f'offset: mjd={mjd},size={size}e-7\n')
        # f.write('</be>\n\n')
        
        # Schedule
        f.write('<schedule>\n')
        f.write('name: sched_similar_regsamp\n')
        for key_psr, value_psr, value_toaerr_3100, value_toaerr_1400, value_toaerr_600 in zip(starts.keys(), starts.values(), toaerrs_3100.values(), toaerrs_1400.values(), toaerrs_600.values()):
            #f.write(f'observe: psr={key_psr},toaerr={value_toaerr_3100},freq=3100,be=be1,start={value_psr}\n')
            f.write(f'observe: psr={key_psr},toaerr={value_toaerr_3100},freq=3100,start={value_psr}\n') 
            #f.write(f'observe: psr={key_psr},toaerr={value_toaerr_3100},freq=3100\n') 
            f.write(f'observe: psr={key_psr},toaerr={value_toaerr_1400},freq=1400,start={value_psr}\n')
            #f.write(f'observe: psr={key_psr},toaerr={value_toaerr_1400},freq=1400\n')
            f.write(f'observe: psr={key_psr},toaerr={value_toaerr_600},freq=600,start={value_psr}\n')
            #f.write(f'observe: psr={key_psr},toaerr={value_toaerr_600},freq=600\n')
        f.write('</schedule>\n\n')

files_dir = '/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/'

dr3_psrs_list = files_dir+'dr3_psrs_list.txt'
P0s_list = files_dir+'P0s_for_PTASim.txt'
Ds_list = files_dir+'Ds_for_PTASim.txt'
taus_list = files_dir+'taus_for_PTASim.txt'
gammas_list = files_dir+'gammas_for_PTASim.txt'
starts_list = files_dir+'starts_for_PTASim.txt'
toaerrs_3100_list = files_dir+'toaerrs_for_PTASim_3100MHZ.txt'
toaerrs_1400_list = files_dir+'toaerrs_for_PTASim_1400MHZ.txt'
toaerrs_600_list = files_dir+'toaerrs_for_PTASim_600MHZ.txt'

create_inp(dr3_psrs_list, gammas_list, P0s_list, Ds_list, taus_list, starts_list, toaerrs_3100_list, toaerrs_1400_list, toaerrs_600_list)
