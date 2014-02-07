web_serv-ctl.py --help for details.

An example call:

./web_serv-ctl.py -a 127.0.0.1 -p 8000 -e ./fortune.py start
Running Web_Serv.py....

telnet 127.0.0.1 8000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.1
HTTP/1.1 200 OK
Server: Web_Serv.py v1.0
Date: 
Content-Type: text/plain; charset=utf-8
Content-Length: 59

YOUR FORTUNE: Don't wait for success to come - go find it!
GET / HTTP/1.1
HTTP/1.1 200 OK
Server: Web_Serv.py v1.0
Date: 
Content-Type: text/plain; charset=utf-8
Content-Length: 60

YOUR FORTUNE: Don't hesitate to tackle a difficult problem.
GET / HTTP/1.1
HTTP/1.1 200 OK
Server: Web_Serv.py v1.0
Date: 
Content-Type: text/plain; charset=utf-8
Content-Length: 48

YOUR FORTUNE: Love like you've never been hurt.
GET / HTTP/1.1
HTTP/1.1 200 OK
Server: Web_Serv.py v1.0
Date: 
Content-Type: text/plain; charset=utf-8
Content-Length: 60

YOUR FORTUNE: Don't hesitate to tackle a difficult problem.
GET / HTTP/1.1
HTTP/1.1 200 OK
Server: Web_Serv.py v1.0
Date: 
Content-Type: text/plain; charset=utf-8
Content-Length: 60

YOUR FORTUNE: Don't hesitate to tackle a difficult problem.
GET / HTTP/1.1
HTTP/1.1 200 OK
Server: Web_Serv.py v1.0
Date: 
Content-Type: text/plain; charset=utf-8
Content-Length: 45

YOUR FORTUNE: Pursue your dreams with vigor.
^CConnection closed by foreign host.
