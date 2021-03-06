#!/usr/bin/env python3

import sys
from results import *

def report(dir):
    r = Results()
    r.read_all(dir)
    print("Hosts vulnerable to Bluekeep:")
    for key in filter_by_bluekeep(r.hosts):
        print('  %s'%key)
    print('\nHosts vulnerable to MS17-010:')
    for key in filter_by_ms17010(r.hosts):
        print('  %s'%key)


if __name__=='__main__':
    report(sys.argv[1])
