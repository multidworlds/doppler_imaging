#! /usr/bin/env python3
"""
map the the sphere to a surface.
Caculate the projected area size radial velocity for a given pair of latitute and longitude
"""
import numpy as np


def grid_map(latitude, longitude, d_lat, d_long, omega, radius):
    """

    :param latitude: the latitude of the differential area
    :param longitude: the longitude of the differential are
    :param d_lat: the size of the differential area in latitude direction
    :param d_long: the size of the differential area in longitude direction
    :param omega: angular velocity of the star
    :param radius: radius of the star

    """
    cos_lat = np.cos(latitude)
    cos_long = np.cos(longitude)
    # projected radial veloctiy
    Vr = omega * radius * cos_lat * cos_long
    # projected area size
    dA = radius * radius * cos_lat**2 * cos_long * d_lat * d_long
    return dA, Vr
