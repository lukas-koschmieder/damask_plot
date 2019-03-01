# Copyright (c) 2019 Lukas Koschmieder
# Copyright (c) 2015 Mingxuan Lin

from .label import _Label as L
import numpy as np

def Piola2Cauchy(P, F):
    """
    Convert Piola-Kirchhoff stress tensor (P) to Cauchy stress tensor (sigma)
    """
    P = np.array(P).reshape([3,3])
    F = np.array(F).reshape([3,3])
    sigma = 1.0 / np.linalg.det(F) * np.dot(P, F.T)
    return sigma

def Cauchy2Mises(sigma):
    """
    Compute von Mises stress (aka equivalent tensile stress) (sigma_v)
    """
    sigma = np.array(sigma).reshape([3,3])
    sigma_dev = sigma - (1.0/3.0) * np.trace(sigma) * np.eye(3)
    sigma_dev_sym = (1.0/2.0) * (sigma_dev + sigma_dev.T)
    sigma_v = np.sqrt((3.0/2.0) * np.sum(sigma_dev_sym * sigma_dev_sym))
    return sigma_v

def fallback(label, new, cache):
    if label in new:
        return new[label]
    else:
        return cache[label][-1]

def mag(label, new):
    a = np.asarray(new[label])
    return np.sqrt(a.dot(a))

def filter(new, cache):
    cache[L.STEP].append(len(cache[L.STEP]))
    for label in [L.ITER, L.MIN_ITER, L.MAX_ITER,]:
        cache[label].append(new[label])
    for label in [L.INC, L.MAX_INC, L.SUBINC, L.MAX_SUBINC,
                  L.LOADCASE, L.MAX_LOADCASE, L.LC_INC, L.LC_MAX_INC,
                  L.LC_SUBINC, L.LC_MAX_SUBINC, L.TIME,]:
        cache[label].append(fallback(label, new, cache))
    cache[L.ERROR_DIVERGENCE].append(
        new[L.TUPLE_ERROR_DIVERGENCE][0][0])
    cache[L.ERROR_STRESS_BC].append(
        new[L.TUPLE_ERROR_STRESS_BC][0][0])

    P = L.TUPLE_PIOLA_KIRCHHOFF_STRESS
    F = L.TUPLE_DEF_GRADIENT_AIM
    cache[L.MAG_PIOLA_KIRCHHOFF_STRESS].append(mag(P, new))
    cache[L.MAG_DEF_GRADIENT_AIM].append(mag(F, new))
    cache[L.VONMISES_STRESS].append(
        Cauchy2Mises(Piola2Cauchy(new[P],new[F])))
