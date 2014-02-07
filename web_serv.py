#!/usr/bin/env python
"""
Simple Socket based HTTP server

"""
import re
import sys
import socket
from subprocess import Popen, PIPE

server_info = 'Web_Serv.py v1.0'

class Web_Serv(object):
    """
    A simple socket based HTTP server

    """
    def __init__(self, address, port, ext_prog):
        self.server_info = 'Web_Serve.py v1.0'
        self.addr = address
        self.port = int(port)
        self.ext_prog = ext_prog

    def run(self):
        """
        Start Web_Serve on the specified address/port. Process HTTP requests
        as received. If request is valid, run ext_prog and return its output

        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            sock.close()
            print 'Could not open socket.'
            sys.exit(1)

        sock.bind((self.addr, self.port))
        sock.listen(1)
        conn, add = sock.accept()
        while True:
            data = conn.recv(1024)
            response = self.process_req(data)
            conn.send(response)
            if not data:
                break    
        conn.close()

    def call_ext_prog(self):
        """
        Call external program and return its output and return code
        
        """
        proc = Popen([self.ext_prog], stdout = PIPE)
        stdout, stderr = proc.communicate()       
        return proc.returncode, stdout        
            
    def process_req(self, http_req):
        """
        Process the http request, potentially call external program, and return
        string containing the http response 

        """
        http_regex = re.compile('(\S+)\s+(\S+)')
        http_code = http_resp = resp_body = ''
        cont_len = '0'
    
        http_match = re.search(http_regex, http_req)
        if not http_match:
            print 'Received a malformed HTTP request, exiting...'
            sys.exit(1)
        else:
            http_comm = http_match.group(1)
            http_uri = http_match.group(2)

        if not re.match('GET', http_comm):
            """ Return 405 """
            http_code = '405 Method Not Allowed'
            resp_body = 'ERROR - 405 Method Not Allowed'
            cont_len = str(len(resp_body))
        elif not re.match('^\/$', http_uri):
            """ Return 404 """
            http_code = '404 Not Found'
            resp_body = 'ERROR - 404 Not Found'
            cont_len = str(len(resp_body))
        else:
            ret_code, output = self.call_ext_prog() 
            
            if ret_code != 0:
                http_code = '500 Server Error'
                resp_body = 'ERROR - 500 Server Error'
                cont_len = str(len(resp_body))
            else:
                http_code = '200 OK'
                resp_body = output
                cont_len = str(len(resp_body))
        http_resp = 'HTTP/1.1 ' + http_code + '\r\n' + 'Server: ' + server_info + '\r\n' + 'Date: ' + '\r\n' + 'Content-Type: text/plain; charset=utf-8' + '\r\n' + 'Content-Length: ' + cont_len + '\r\n\r\n' + resp_body  
        return http_resp

