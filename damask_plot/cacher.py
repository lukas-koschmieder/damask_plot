# Copyright (c) 2019 Lukas Koschmieder

import asyncio
from aixplot.cacher import Cacher
from .filter import filter
from .label import labels
from .reader import IncrementReader, IterationReader

class DamaskCacher(Cacher):
    def __init__(self, file, logger=None):
        super(DamaskCacher, self).__init__(file, logger)

    def _filter(self, data, cache):
        return filter(data, cache)

    async def _async_read(self, file):
        data = await self._reader.async_read(file, tries=1)
        return data

class IncrementCacher(DamaskCacher):
    def __init__(self, file, logger=None):
        super(IncrementCacher, self).__init__(file, logger)
        self._reader = IncrementReader()

class IterationCacher(DamaskCacher):
    def __init__(self, file, logger=None):
        super(IterationCacher, self).__init__(file, logger)
        self._reader = IterationReader()
