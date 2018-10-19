"""
calcualte the spectrum for a heterogeneous sphere
"""
import numpy as np
from grid_map import grid_map, spot_map
from dopplerTools import dopplerShift
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def calSpec(wavelength, spotList, specBck, specSpot, omega, radius, inclination):
    """ calculate the spectrum
    TODO incorporate limb darkening in the weight calculation
    """
    # get the grid_map
    areaGrid, projAreaGrid, vGrid = grid_map(omega, radius, inclination)
    totalArea = projAreaGrid.sum()
    sMap = spot_map(spotList)
    # calculate the map
    NLat, NLon = areaGrid.shape
    spectrum = np.zeros_like(wavelength)
    for i in range(NLat):
        print(i)
        for j in range(NLon):
            if sMap[i, j] == 0:  # photosphere scenerio
                spec_i = projAreaGrid[i, j] / totalArea * \
                    dopplerShift(specBck['wavelength'],
                                 specBck['flux'],
                                 vGrid[i, j],
                                 wavelength)
            else:
                print('Spotty grid')
                spec_i = projAreaGrid[i, j] / totalArea * \
                    dopplerShift(specSpot['wavelength'],
                                 specSpot['flux'],
                                 vGrid[i, j],
                                 wavelength)
            spectrum += spec_i
    return spectrum


if __name__ == '__main__':
    wl1, fl1 = np.loadtxt('spec1.dat', unpack=True)
    wl2, fl2 = np.loadtxt('spec2.dat', unpack=True)
    spec1 = {
        'wavelength': wl1,
        'flux': fl1
    }
    spec2 = {
        'wavelength': wl2,
        'flux': fl2
    }
    omega = 1.7e-4  # 10 hr rotation period, a fast rotating star
    R = 6.957e5  # use solar radius in km
    spotList = [(0, -np.pi / 3, 30 * np.pi / 180)]
    spec = calSpec(wl1, spotList, spec1, spec2, omega, R, 0)
    spec0 = calSpec(wl1, [], spec1, spec2, omega, R, 0)
    plt.close('all')
    plt.plot(wl1, spec)
    plt.plot(wl1, spec0)
    plt.xlabel('Wavelength [$\AA$]')
    plt.ylabel('flux')
    xcorr = np.correlate(spec, spec0, 'same')
    dV = (wl1 - wl1.mean()) / wl1.mean() * 3e5
    plt.figure()
    plt.plot(dV, xcorr)
    plt.xlabel('$\Delta V [km]$')
    plt.show()


    # wl_low = 6000
    # wl_high = 10000
    # R = 90000
    # wl0 = np.linspace(wl_low, wl_high, R * (wl_high - wl_low) /
    #                   (wl_low + wl_high) * 2)
    # wl1, log_fl1 = np.loadtxt(
    #     './lte3400-5.08-M-1.00-A+0.40-C+0.35-O+0.89.txt',
    #     unpack=True)
    # fl1 = 10**(log_fl1)
    # spec1_interp = interp1d(wl1, fl1)
    # fl1 = spec1_interp(wl0)
    # spec1 = {
    #     'wavelength': wl0,
    #     'flux': fl1
    # }
    # wl2, log_fl2 = np.loadtxt(
    #     './lte3200-5.08-M-0.50-A-0.10-C+0.12-O+0.28.txt',
    #     unpack=True)
    # fl2 = 10**(log_fl2)
    # spec2_interp = interp1d(wl2, fl2)
    # fl2 = spec2_interp(wl0)
    # spec2 = {
    #     'wavelength': wl0,
    #     'flux': fl2
    # }
