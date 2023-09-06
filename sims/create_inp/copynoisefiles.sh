#!/bin/csh

set parent_dest_dir = "/DATA/CETUS_3/dim052/forvalentina/jumps_or_no_jumps/sims/30psr_100reals_f005-noDM/output"

foreach i (`seq 0 99`)
    set dest_dir = "${parent_dest_dir}/real_${i}"
    cp -r noisefiles $dest_dir/

end
