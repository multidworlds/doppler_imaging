import starry
import numpy as np
import matplotlib.pyplot as plt

# Spherical harmonic degree & number of wavelength bins
lmax = 10
nwav = 500

# Spot properties
sigma = 0.1
lat = 45
lon = -30

# Generate a random spectrum
spectrum = 0.2 * np.random.randn(nwav) + np.sin(np.linspace(0, 4 * np.pi, nwav))

# Generate a wavelength-dependent gaussian with that spectrum
ncoeff = (lmax + 1) ** 2
gaussian2d = np.zeros((ncoeff, nwav))
tmp = starry.Map(lmax=lmax)
for n in range(nwav):
    tmp.reset()
    tmp.add_gaussian(sigma=0.1, amp=spectrum[n], lat=lat, lon=lon)
    gaussian2d[:, n] = np.array(tmp.y)

# Assign it to the map
map = starry.Map(lmax=lmax, nwav=nwav)
map[:, :] = gaussian2d

# Compute the rotational phase curve
theta = np.linspace(0, 360, 1000)
# flux = map.flux(theta=theta)

# # Plot the data
# fig, ax = plt.subplots(2, figsize=(7, 7))
# ax[0].plot(theta, flux)
# ax[1].plot(range(nwav), flux.transpose())
# ax[0].set_ylabel("Flux")
# ax[0].set_xlabel("Rotational angle")
# ax[1].set_ylabel("Flux")
# ax[1].set_xlabel("Wavelength bin")

# # Show the map
# map.show()
