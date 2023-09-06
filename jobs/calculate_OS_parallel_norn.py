import os
import json
import matplotlib.pyplot as plt
import numpy as np
import glob
import csv
import pandas as pd

from enterprise.signals import signal_base
from enterprise.signals import gp_signals
from enterprise.pulsar import Pulsar
from enterprise_extensions import model_utils, blocks
from enterprise_extensions.frequentist import optimal_statistic as opt_stat


#set up pulsar objects 
parfiles = sorted(glob.glob('*par'))
timfiles = sorted(glob.glob('*tim'))

psrs = []
ephemeris = 'DE421'
for p, t in zip(parfiles, timfiles):
    psr = Pulsar(p, t, ephem=ephemeris)
    psrs.append(psr)
    
    # Load up the noise dictionary to get values for the white noise parameters
    noisefile = '/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/noisefiles/all_WhiteNoiseParams.json'
    
with open(noisefile, 'r') as f:
    noisedict = json.load(f)

Tspan = model_utils.get_tspan(psrs)
s = gp_signals.TimingModel()
s += blocks.white_noise_block(vary=False, inc_ecorr=False, select='backend',tnequad=True)
s += blocks.red_noise_block(prior='log-uniform', Tspan=Tspan, components=30)
s += blocks.common_red_noise_block(psd='powerlaw', prior='log-uniform', Tspan=Tspan, components=5, gamma_val=4.33, name='gw')

# Set up the PTA object using the signal we defined above and the pulsars
pta = signal_base.PTA([s(p) for p in psrs])

# Set the white noise parameters to the values in the noise dictionary
pta.set_default_params(noisedict)

ostat = opt_stat.OptimalStatistic(psrs, pta=pta, orf='hd')
#ostat_dip = opt_stat.OptimalStatistic(psrs, pta=pta, orf='dipole')
#ostat_mono = opt_stat.OptimalStatistic(psrs, pta=pta, orf='monopole')

# Load up the maximum-likelihood values for the pulsars' red noise parameters and the common red process

with open('/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/noisefiles/all_singlePsrNoise_norn_nogw.json', 'r') as f:
    ml_params = json.load(f)

# Compute the optimal statistic
# The optimal statistic returns five quantities:
#  - xi: an array of the angular separations between the pulsar pairs (in radians)
#  - rho: an array of the cross-correlations between the pulsar pairs
#  - sig: an array of the uncertainty in the cross-correlations
#  - OS: the value of the optimal statistic
#  - OS_sig: the uncertainty in the optimal statistic

xi, rho, sig, OS, OS_sig = ostat.compute_os(params=ml_params)
print(OS, OS_sig, OS/OS_sig)

data_OS = {"OS": OS, "OS_error": OS_sig, "OS_snr": OS/OS_sig}


# Save outputs

pd.DataFrame(xi).to_csv(f'xi', header=None, index=None)
pd.DataFrame(rho).to_csv(f'rho', header=None, index=None)
pd.DataFrame(sig).to_csv(f'sig', header=None, index=None)
json_string = json.dumps(data_OS)
with open(f'OS.txt', 'w') as file:
    file.write(json_string)

