#!/usr/bin/env python
"""
Start Web_Serv.py on system

"""
import sys
from optparse import OptionParser
from web_serv import Web_Serv

def get_opts():
    """
    Process command line args, return options and args found on the command line

    """
    parse = OptionParser()
    parse.add_option("-a", "--address", dest="address", help="Address to bind web_serv to")
    parse.add_option("-p", "--port", dest="port", help="Port to bind web_serv")
    parse.add_option("-e", "--ext_prog", dest="ext_prog", help="External program to call")
    (options, args) = parse.parse_args()
    return (options, args)

def main():

    options, args = get_opts()

    if len(args) == 0:
        print "Missing start or stop verb"
        sys.exit(1)
    if not args[0].lower() in ('start', 'stop'):
        print 'Command option must be either \'start\' or \'stop\''
        sys.exit(1)
    else:
        if args[0].lower() == 'start':
            print 'Running Web_Serv.py....'
            server = Web_Serv(options.address, options.port, options.ext_prog)
            server.run()
        else:
            print 'Stop functionality is not yet supported'
            sys.exit(1)

if __name__ == "__main__":
    main()
