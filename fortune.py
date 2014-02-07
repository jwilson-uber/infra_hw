#!/usr/bin/env python

import sys
from optparse import OptionParser 
from random import randint

def main():

    fortunes = ['Don\'t hesitate to tackle a difficult problem.',
                'Pursue your dreams with vigor.',
                'Don\'t wait for success to come - go find it!',
                'Fame and fortune lie ahead.',
                'A healthy body will benefit you for life.',
                'Love like you\'ve never been hurt.',
                'Dance like nobody\'s watching.']
    rand = randint(0,6)
    print 'YOUR FORTUNE: %s' % fortunes[rand]

if __name__ == "__main__":
    main()
