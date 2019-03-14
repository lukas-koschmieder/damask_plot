# Copyright (c) 2019 Lukas Koschmieder

from ipywidgets import Box
from aixplot.widget import Filter, NoneFilter
from aixplot.widget import Widget as Aixplot
import numpy as np
from .cacher import IterationCacher
from .label import Label

from IPython.core.magic import line_magic, magics_class, Magics
from IPython.core.magic_arguments import argument, magic_arguments, \
                                         parse_argstring

class ConvergenceFilter(Filter):
    def __repr__(self):
        return "Convergence"
    def __call__(self, label, cache):
        a = np.array(cache[label])
        f = np.array(cache[Label.CONVERGENCE])
        return a[f]

class Widget(Aixplot):
    def __init__(self, cacher_class=IterationCacher, logger=None, **traits):
        self.filters = [NoneFilter(), ConvergenceFilter()]
        self.filter = self.filters[1]
        self.x, self.y = Label.STEP, Label.VONMISES_STRESS
        super(Widget, self).__init__(cacher_class, logger=logger, **traits)

@magics_class
class DamaskPlotMagics(Magics):
    @line_magic
    @magic_arguments()
    @argument('--filename', '-f', help='DAMASK stdout filename to be plotted')
    def damask_plot(self, line=''):
        args = parse_argstring(self.damask_plot, line)
        if args.filename:
            display(Widget(filename=args.filename))
        else:
            display(Widget())
