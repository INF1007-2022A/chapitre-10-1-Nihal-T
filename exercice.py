#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    a = np.linspace(start=-1.3, stop=2.5, num=64)
    return a


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    rayon = np.sqrt((cartesian_coordinates[0]**2) +(cartesian_coordinates[1]**2))
    angle = np.arctan(cartesian_coordinates[1]/cartesian_coordinates[0])
    return(rayon,angle)

def find_closest_index(values: np.ndarray, number: float) -> int:
    for i in range(len(values)):
        if np.abs(values[i]-number) < np.abs(values[i+1]-number):
            index = i
        else:
            index= (i+1)
    return index


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
