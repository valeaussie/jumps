import numpy as np
import json
import os
import matplotlib.pyplot as plt
import glob 
import time

import enterprise
from enterprise.pulsar import Pulsar
import enterprise.signals.parameter as parameter
from enterprise.signals import utils
from enterprise_extensions import model_utils, blocks 
from enterprise.signals import signal_base
from enterprise.signals import selections
from enterprise.signals.selections import Selection
from enterprise.signals import white_signals
from enterprise.signals import gp_signals
from enterprise.signals import deterministic_signals
from enterprise import constants as const

from enterprise_extensions.chromatic import chromatic
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

gw_log10_A = parameter.Uniform(-18, -14)('gw_log10_A')
gw_gamma = parameter.Constant(13./3)('gw_gamma')

tmin = np.amin([p.toas.min() for p in psrs])
tmax = np.amax([p.toas.max() for p in psrs])
Tspan = tmax - tmin
Tspan/(365.25*24*3600)
freqs = np.linspace(1/Tspan,30/Tspan,30)
gw_pl = utils.powerlaw(log10_A=gw_log10_A, gamma=gw_gamma)

#start_time = time.time()
num_shifts = 5000
OSs = np.zeros(num_shifts)
for j in range(num_shifts):
    # Note that ecorr is still False here
    Tspan = model_utils.get_tspan(psrs)
    s = gp_signals.TimingModel()
    s += blocks.white_noise_block(vary=False, inc_ecorr=False, select='backend',tnequad=True)
    s += blocks.red_noise_block(prior='log-uniform', Tspan=Tspan, components=30)
    s += gp_signals.FourierBasisGP(spectrum=gw_pl, name='gw', pshift=True) 
    
    # Set up the PTA object using the signal we defined above and the pulsars
    models_pshift = [s(p) for p in psrs]
    pta_pshift = signal_base.PTA(models_pshift)
    
    # Set the white noise parameters to the values in the noise dictionary
    pta_pshift.set_default_params(noisedict)
    
    ostat = opt_stat.OptimalStatistic(psrs, pta=pta_pshift, orf='hd')  
    
    with open('/fred/oz002/vdimarco/jumps/jumps_or_no_jumps/sims/noisefiles/all_singlePsrNoise_norn_smallgw.json', 'r') as f:
        ml_params = json.load(f) 
        
    _, _, _, OS, _ = ostat.compute_os(params=ml_params)           
    OSs[j] = OS
    
#end_time  = time.time()
#elapsed = end_time - start_time
        
# Save outputs
np.savetxt(f'scrambles.txt', OSs)

# Save time
#with open('elapsed.txt', 'w') as file:
#    file.write(f'Elapsed time: {elapsed:.4f} seconds\n')
    
