# Copyright (c) 2019 Lukas Koschmieder

from abc import abstractmethod
from aixplot.reader import Reader
from .parser import IncrementParser, IterationParser

class DamaskReader(Reader):
    def __init__(self):
        super(DamaskReader, self).__init__()
        self._cache = []
        self._iscaching = False

    @abstractmethod
    def _parse(self, cache):
        pass

    def _process_cache(self):
        data = self._parse(self._cache)
        self._cache = []
        return data

class IncrementReader(DamaskReader):
    def __init__(self):
        super(IncrementReader, self).__init__()
        self._parser = IncrementParser()

    def _parse(self, cache):
        return self._parser.parse(cache)

    def _process_line(self, line):
        if line.startswith(' ###'):
            if self._iscaching:
                return self._process_cache()
            else:
                self._iscaching = True
        elif self._iscaching:
            self._cache.append(line)

class IterationReader(DamaskReader):
    def __init__(self):
        super(IterationReader, self).__init__()
        self._parser = IterationParser()

    def _parse(self, cache):
        return self._parser.parse(cache)

    def _process_line(self, line):
        if line.startswith(' ###'):
            self._iscaching = True
        elif line.startswith(' ==='):
            return self._process_cache()
        elif self._iscaching:
            self._cache.append(line)
