# Copyright (c) 2015 Mingxuan Lin
# Copyright (c) 2019 Lukas Koschmieder

from .label import _Label as L
from parsimonious.grammar import Grammar, NodeVisitor
import re

rules = """
main       = element+
element    = itr_begin / itr_end / inc_begin / inc_end / inc_sep / infoline / expr / nl+ / any
itr_begin  = ws inc_num ws "@" ws ~"Iteration +(\d+[^\d\s]){2}\d+" nl
itr_end    = ws ~"=+" nl
inc_begin  = ws "Time" float "s:" ws inc_num ~" +of load case +(\d+)/(\d+)" nl
inc_end    = ws "increment" integer ws "converged" nl
inc_num    = "Increment" ws ~"(\d+)/(\d+)-(\d+)/(\d+)"
inc_sep    = ws ~"#+" nl
infoline   = ws dotsline ws keywords dotsline nl
dotsline   = ~"\.+"
expr       = ws keywords ~" *=" float+ ws range? nl
range      = "(" float ~"[a-z ,=/]+"i  float  ")"
float      = ~"\s*?[-+]?\d*\.?\d+([eE][-+]?\d+)?"
integer    = ~"\s*?[-+]?\d+"
keywords   = ~"([\w\-/]+ *)+"
nl         = ws "\\n"
ws         = ~"[ \t\v\f]*"
any        = ~"(.+\\n?)|\\n"
"""

class Parser(NodeVisitor):
    def __init__(self):
        self.grammar = Grammar(rules)

    def visit_inc_begin(self, node, visited_children):
        self._data[L.TIME] = float(node.children[2].text)
        self._data.update(zip([L.LC_INC, L.LC_MAX_INC, L.LC_SUBINC, L.LC_MAX_SUBINC], map(int, node.children[5].children[2].match.groups())))
        self._data.update(zip([L.LOADCASE, L.MAX_LOADCASE], map(int, node.children[6].match.groups())))

    def visit_itr_begin(self, node, visited_children):
        self._data.update(zip([L.INC, L.MAX_INC, L.SUBINC, L.MAX_SUBINC], map(int, node.children[1].children[2].match.groups())))
        itr_num = [int(v) for v in re.findall(r'\d+', node.children[5].text)]
        self._data.update(zip([L.MIN_ITER, L.ITER, L.MAX_ITER,], itr_num))

    def visit_expr(self, node, visited_children):
        n_kw, n_values, n_range = node.children[1], node.children[3], node.children[5]
        name = n_kw.text.strip()
        value = tuple(float(v.text) for v in n_values if v.expr_name == "float")
        if n_range.children:
            ext_value = tuple(float(v.text) for v in n_range.children[0] if v.expr_name == "float")
            self._data[name] = (value, ext_value)
        else:
            self._data[name] = value

    def visit_inc_end(self, node, visited_children):
        self._data[L.INC] = int(node.children[2].text)
        self._data[L.CONVERGED] = True

    def visit_any(self, node, visited_children):
        if node.text.strip():
            self._unparsed += node.text

    def generic_visit(self, node, visited_children):
        pass

    def parse(self, lines):
        self._data, self._unparsed = {}, ""
        super(Parser, self).parse(''.join(lines))
        return self._data

class IncrementParser(Parser):
    def __init__(self):
        super(IncrementParser, self).__init__()

class IterationParser(Parser):
    def __init__(self):
        super(IterationParser, self).__init__()
