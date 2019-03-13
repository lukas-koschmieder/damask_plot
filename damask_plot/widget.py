# Copyright (c) 2019 Lukas Koschmieder

from ipywidgets import Box
from aixplot.widget import Filter, NoneFilter
from aixplot.widget import Widget as Aixplot
import numpy as np
from .cacher import IterationCacher
from .label import Label as L

class ConvergenceFilter(Filter):
    def __repr__(self):
        return "Convergence"
    def __call__(self, label, cache):
        a = np.array(cache[label])
        f = np.array(cache[L.CONVERGENCE])
        return a[f]

class Widget(Aixplot):
    def __init__(self, cacher_class=IterationCacher, logger=None, **traits):
        self.filters = [NoneFilter(), ConvergenceFilter()]
        self.filter = self.filters[1]
        self.x, self.y = L.STEP, L.VONMISES_STRESS
        super(Widget, self).__init__(cacher_class, logger=logger, **traits)
