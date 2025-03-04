#!/usr/bin/env python3

import socket
import sys
import argparse

class Knockit(object):
    def __init__(self, args: list):
        self._parse_args(args)

    def _parse_args(self, args: list):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--delay', type=int, default=200,
                            help='Delay between each knock. Default is 200 ms.')
        parser.add_argument('host', help='Hostname or IP address of the host.')
        parser.add_argument('ports', type=int, help='Port(s) to knock on', nargs='+')

        args = parser.parse_args(args)
        self.delay = args.delay / 1000
        self.ports = args.ports
        self.host= args.host

    def _log_knock(self, addrfamily, sockaddr):
        if addrfamily == socket.AF_INET6:
            print(f'[+] Knocking on port [{sockaddr[0]}]:{sockaddr[1]}')
        else:
            print(f'[+] Knocking on port {sockaddr[0]}:{sockaddr[1]}')

    def knockit(self):
        self.ports = list(map(int, self.ports))
        for port in self.ports:
            addrinfos = socket.getaddrinfo(self.host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            addrfamily, socktype, sockproto, _, sockaddr = addrinfos[0]
            
            self._log_knock(addrfamily, sockaddr)
            
            sock = socket.socket(addrfamily, socktype, sockproto)
            sock.settimeout(self.delay)
            sock.connect_ex(sockaddr)
            sock.close()


if __name__ == '__main__':
    Knockit(sys.argv[1:]).knockit()