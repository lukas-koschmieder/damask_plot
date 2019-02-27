# Copyright (c) 2019 Lukas Koschmieder

class Label(object):
    STEP = "Step"
    ITER = "Iteration"
    MIN_ITER = "Min iteration"
    MAX_ITER = "Max iteration"
    INC = "Increment"
    MAX_INC = "Max increment"
    SUBINC = "Subincrement"
    MAX_SUBINC = "Max subincrement"
    LOADCASE = "Loadcase"
    MAX_LOADCASE = "Max loadcase"
    LC_INC = "Loadcase increment"
    LC_MAX_INC = "Loadcase max increment"
    LC_SUBINC = "Loadcase subincrement"
    LC_MAX_SUBINC = "Loadcase max subincrement"
    TIME = "Time [s]"
    ERROR_DIVERGENCE = "Error divergence"
    ERROR_STRESS_BC = "Error stress BC"
    MAG_DEF_GRADIENT_AIM = "Deformation gradient aim magnitude"
    MAG_PIOLA_KIRCHHOFF_STRESS = "Piola-Kirchhoff stress magnitude [MPa]"

class _Label(Label):
    TUPLE_ERROR_DIVERGENCE = "error divergence"
    TUPLE_ERROR_STRESS_BC = "error stress BC"
    TUPLE_DEF_GRADIENT_AIM = "deformation gradient aim"
    TUPLE_PIOLA_KIRCHHOFF_STRESS = "Piola--Kirchhoff stress       / MPa"
    CONVERGED = "converged"

labels = [getattr(Label, a) for a in dir(Label) if not a.startswith("_")]
