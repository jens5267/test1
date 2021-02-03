import constants as c
import numpy as np


c1 = 0.5 * c.RHO_AIR
c2 = 0.5 * c.RHO_HYD
c3 = c.MU_VOL_N**2 / (c.MU_MECH_N * c.c_DAMP_N**2)

area = 1

def get_nozzle_radius(c, area):

    K1 = c.c_P / c.TSR**3 * c1 * np.pi * c.R_ROT**5
    K2 = c3 * c2 * c.VOL_DISP_P['m3_rad']**3 / area

    difference = 0.0001

    if K1 < K2:
        while K2 - K1 > difference:
            area *= (K2 / K1)
            K2 = c3 * c2 * c.VOL_DISP_P['m3_rad']**3 / area

    if K1 > K2:
        while K1 - K2 > difference:
            area /= (K1 / K2)
            K2 = c3 * c2 * c.VOL_DISP_P['m3_rad']**3 / area

    nozzle_radius = np.sqrt(np.sqrt(area)/np.pi)
    print(f"Nozzle radius is {nozzle_radius:.3f} m")
    return nozzle_radius

get_nozzle_radius(c, area)