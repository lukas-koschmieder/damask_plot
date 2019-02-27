# Copyright (c) 2019 Lukas Koschmieder

from .label import _Label as Label
import numpy as np

def fallback(label, new, cache):
    if label in new:
        return new[label]
    else:
        return cache[label][-1]

def mag(label, new):
    a = np.asarray(new[label])
    return np.sqrt(a.dot(a))

def filter(new, cache):
    cache[Label.STEP].append(len(cache[Label.STEP]))
    cache[Label.ITER].append(new[Label.ITER])
    for label in [Label.INC, Label.MAX_INC, Label.LC_INC,
                  Label.LC_MAX_INC, Label.TIME]:
        cache[label].append(fallback(label, new, cache))
    cache[Label.ERROR_DIVERGENCE].append(
        new[Label.TUPLE_ERROR_DIVERGENCE][0][0])
    cache[Label.ERROR_STRESS_BC].append(
        new[Label.TUPLE_ERROR_STRESS_BC][0][0])
    cache[Label.MAG_DEF_GRADIENT_AIM].append(
        mag(Label.TUPLE_DEF_GRADIENT_AIM, new))
    cache[Label.MAG_PIOLA_KIRCHHOFF_STRESS].append(
        mag(Label.TUPLE_PIOLA_KIRCHHOFF_STRESS, new))
