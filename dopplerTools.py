import numpy as np 
from astropy import units as u 
from astropy import constants as cs
from scipy import interpolate

def dopplerShift(wavelength, flux, v, interpKind = 'linear', fillVal = 'extrapolate'):
	""" Doppler shift a spectrum.

	Parameters
	----------
	wavelength: array
		array containing wavelength values, in A
	flux: array
		array containing flux values
	v velocity of shift, in km/s
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
	ckm = (cs.c).to(u.km / u.s).value
	dopplerWav = wavelength * (1 + v/ckm)
	F = interpolate.interp1d(dopplerWav, flux, kind=interpKind, fill_value=fillVal)
	dopplerFlux = F(wavelength)
	return dopplerWav, dopplerFlux








