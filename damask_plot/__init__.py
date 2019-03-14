# Copyright (c) 2019 Lukas Koschmieder

from .label import Label as DamaskPlotLabel
from .widget import Widget as DamaskPlot, DamaskPlotMagics

try:
    ip = get_ipython()
    ip.register_magics(DamaskPlotMagics)
except:
    pass
