####################################################################
#This script creates the noise files for Enterprise
####################################################################



def create_noisefiles(gammas_file, a0s_file):

    # Open the file with the values of a0s for red noise                               
    a0s = {}
    with open(a0s_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        a0s[key] = value

    # Open the file with the values of gamma for red noise                             
    gammas = {}
    with open(gammas_file, 'r') as file:
        contents = file.readlines()
    for line in contents:
        elements = line.strip().split(', ')
        key = elements[0]
        value = elements[1]
        gammas[key] = value


        
    for psr_name, value_a0, value_gamma in zip(a0s.keys(), a0s.values(), gammas.values()):
        out_file_name = f'/DATA/CETUS_3/dim052/forvalentina/jumps_or_no_jumps/sims/noisefiles/{psr_name}_singlePsrNoise.json'
        with open(out_file_name, 'w') as f:
            f.write('{\n')
            f.write(f'"{psr_name}_red_noise_gamma": {value_gamma},')
            f.write(f'"{psr_name}_red_noise_log10_A": {value_a0},\n')
            f.write(f'"gw_log10_A": -15.3')
            f.write('}\n')

gammas_list = '/DATA/CETUS_3/dim052/forvalentina/jumps_or_no_jumps/sims/gammas_for_PTASim.txt'
a0s_list = '/DATA/CETUS_3/dim052/forvalentina/jumps_or_no_jumps/sims/logA_red'

create_noisefiles(gammas_list, a0s_list)
