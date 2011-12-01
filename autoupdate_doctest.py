
from doctest import *
import re

class Update(DocTestRunner):
    def report_success(self, out, test, example, got):
        self.__show(out, example, got)
    def report_failure(self, out, test, example, got):
        self.__show(out, example, got)
    def report_unexpected_exception(self, out, test, example, exc_info):
        out('>>> {0}'.format(example.source))
        out('Traceback (most recent call last):\n')
        out('...\n')
        e = exc_info[1]
        type = repr(e).split('(')[0]
        out('{0}: {1}\n'.format(type, e))
    def summarize(self, verbose): pass
    @staticmethod
    def __show(out, example, got):
        out('>>> {0}'.format(example.source))
        got = re.sub('\n\n','\n<BLANKLINE>\n',got)
        out(got)

import granpa_smpp.node
test = DocTestFinder().find(granpa_smpp.node.Node, granpa_smpp.node)

for t in test: _ = Update().run(t)
