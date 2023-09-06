####################################################################
#This script creates the noise files for Enterprise
####################################################################


def create_noisefiles(psr_list, efac, equad, ecorr):

    # Open the file with the name of the pulsars
    with open(psr_list, 'r') as f:
        psr_names = f.read().splitlines()
    print(psr_names)
    out_file_name = f'/DATA/CETUS_3/dim052/forvalentina/jumps_or_no_jumps/sims/noisefiles/all_WhiteNoiseParams.json'
    with open(out_file_name, 'w') as f:
        f.write('{\n')
        for psr_name in psr_names:
            f.write(f'"{psr_name}_efac": {efac},\n')
            f.write(f'"{psr_name}_log10_tnequad": {equad},\n')
            f.write(f'"{psr_name}_log10_ecorr": {ecorr},\n')
        f.write('}\n')

psr_list = '/DATA/CETUS_3/dim052/forvalentina/jumps_or_no_jumps/sims/dr3_psrs_list.txt'

create_noisefiles(psr_list, 1.0, -8.0, -8.0)
