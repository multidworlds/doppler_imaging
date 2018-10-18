#! /usr/bin/env python3
"""
map the the sphere to a surface.
Caculate the projected area size radial velocity for a given pair of latitute and longitude
"""
import numpy as np

# global parameters to define the number of samples
N_LAT = 100
N_LON = 100
D_LAT = np.pi / N_LAT
D_LON = 2 * np.pi / N_LON
LAT_LIST = np.linspace(-np.pi / 2, np.pi / 2, N_LAT)
LON_LIST = np.linspace(0, 2 * np.pi, N_LON)
LAT_GRID, LON_GRID = np.meshgrid(LAT_LIST, LON_LIST)


def grid_proj(latitude, longitude, d_lat, d_long, omega, radius, incl):
    """

    :param latitude: the latitude of the differential area
    :param longitude: the longitude of the differential are
    :param d_lat: the size of the differential area in latitude direction
    :param d_long: the size of the differential area in longitude direction
    :param omega: angular velocity of the star
    :param radius: radius of the star
    :param incl: the inclination of the spin axis
    TODO: include inclination in the calcualtion
    currently the calcualtion only deal with the scenario where spin axis is perpendicular to the line-of-sight
    """
    cos_lat = np.cos(latitude)
    cos_long = np.cos(longitude)
    # projected radial veloctiy
    Vr = omega * radius * cos_lat * cos_long
    # actual area size
    dS = radius * radius * cos_lat * d_lat * d_long
    # projected area size
    dA = radius * radius * cos_lat**2 * cos_long * d_lat * d_long
    return dS, dA, Vr


def grid_map(omega, radius, incl):
    """return a grid for latitude and longitude
    """
    areaGrid = np.mgrid[N_LAT, N_LON]
    projectedAreaGrid = np.mgrid[N_LAT, N_LON]
    velocityGrid = np.mgrid[N_LAT, N_LON]
    for i, lat_i in enumerate(N_LAT):
        for j, lon_i in enumerate(N_LON):
            dS, dA, Vr = grid_proj(lat_i, lon_i, D_LAT, D_LON,
                                   omega, radius, incl)
            areaGrid[i, j] = dS
            projectedAreaGrid[i, j] = dA
            velocityGrid[i, j] = Vr

    return areaGrid, projectedAreaGrid, velocityGrid


def spot_map(spotList):
    """ given a list of spot
    return the map showing which grid are covered by the spot
    spotList should be a list of tuples showing the lon, lat
    and size of the spot
    """
    spotGrid = np.mgrid[N_LAT, N_LON]
    for spot in spotList:
        distGrid = np.sqrt((LAT_GRID - spot[0])**2 +
                    (LON_GRID - spot[1])**2)
        spotGrid[distGrid < spot[2]] = 1

    return spotGrid
