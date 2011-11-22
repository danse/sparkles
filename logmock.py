
import logging

import sys

def mock_log(logname):
    log = logging.getLogger(logname)
    for handler in log.handlers:
        log.removeHandler(handler)
    log.addHandler(logging.StreamHandler(sys.stdout))

mainlog=logging.getLogger('mainlog')

def method():
    '''
    An handler linked to doctest stdout descriptor must be added just into the
    _first_ doctest

    >>> mock_log('mainlog')
    >>> method()
    error
    '''
    mainlog.error('error')

def second_method():
    '''
    >>> mock_log('mainlog')
    >>> second_method()
    error
    '''
    mainlog.error('error')
