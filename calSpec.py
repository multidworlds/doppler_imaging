"""
calcualte the spectrum for a heterogeneous sphere
"""
from grid_map import grid_map, spot_map


def calSpec(spotList, specBck, specSpot, omega, radius, inclination):
    """ calculate the spectrum
    """
    # get the grid_map
    gMap = grid_map(omega, radius, inclination)
    sMap = spot_map(spotList)
    # calculate the map
