import numpy as np
# from astropy import units as u
# from astropy import constants as cs
from scipy import interpolate


def dopplerShift(wavelength, flux, v, wavelength_out=None, interpKind='linear', fillVal='extrapolate'):
    """ Doppler shift a spectrum.

    Parameters
    ----------
    wavelength: array
            array containing rest frame wavelength values, in A
    flux: array
            array containing rest frame flux values
    v velocity of shift, in km/s
    wavelength_out: output wavelength. If not set, use the input wavelength wavelength
    interpKind: str
            interpolation (kind); see scipy.interpolate documentation for details
    fillVal: str
            fill value (fill_value) for interpolation; see scipy.interpolate documentation for details

    Returns
    ----------
    dopplerWav: array
            shifted wavelength array
    dopplerFlux: array
            the shifted flux array at the *original* wavelength array values
    """
    # ckm = (cs.c).to (u.km / u.s).value
    if wavelength_out is None:
        wavelength_out = wavelength
    ckm = 2.99792458e5  # speed of light in km
    dopplerWav = wavelength * (1 + v/ckm)
    F = interpolate.interp1d(
        dopplerWav, flux, kind=interpKind, fill_value=fillVal)
    dopplerFlux = F(wavelength_out)
    return dopplerFlux
