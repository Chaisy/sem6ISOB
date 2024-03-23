import time

from connection import Connection, print_package
from client import Client, Hacker


class RSTMiddleware:
    def __init__(self):
        self.call_number = 0

    def change(self, package):
        self.call_number += 1
        if self.call_number == 7:
            package.rst = True
        return package


class FakeIpAddressMiddleware:
    def __init__(self, ip_address, tcp_port):
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.call_number = 0

    def change(self, package):
        self.call_number += 1
        if self.call_number == 7:
            package.ip.destination_ip = self.ip_address
            package.destination_port = self.tcp_port
        return package


def run_attacks():
    client = Client(111, 1)
    server1 = Client(222, 2)
    server2 = Hacker(333, 3)

    fake_ip_address_middleware = FakeIpAddressMiddleware(333, 3)
    rst_middleware = RSTMiddleware()
    connection = Connection([client, server1, server2], [fake_ip_address_middleware])

    client.call_any_other(connection)


run_attacks()
