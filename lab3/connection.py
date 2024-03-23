import json
import time


class Connection:
    def __init__(self, members, middlewares):
        self.members = members
        self.middlewares = middlewares
        self.closed = False
        self.connected = False

    def __find_receiver(self, package):
        for member in self.members:
            if member.ip_address == package.ip.destination_ip and member.tcp_port == package.destination_port:
                return member

    def connect(self, package):
        self.connected = True
        self.process(package)

    def process(self, package):
        if not self.connected or self.closed:
            return

        print_package(package)

        for middleware in self.middlewares:
            package = middleware.change(package)

        if package.rst:
            print("Next package:")
            print(json.dumps({
                "Source": f"{package.ip.source_ip}:{package.source_port}",
                "Destination": f"{package.ip.destination_ip}:{package.destination_port}",
                "Sequence": package.sequence,
                "Ack": package.acknowledgment,
                "Flags": {
                    "SYN": package.syn,
                    "ACK": package.ack,
                    "RST": package.rst,

                },
                "Payload": package.ip.payload
            }, indent=4))
            print('RTS flag is TRUE')
            self.close()
            return


        receiver = self.__find_receiver(package)
        if receiver is None:
            print('Unknown destination {}:{}'.format(package.ip.destination_ip, package.destination_port))
            self.close()
            return

        package = receiver.receive(package)
        if package is None:
            print('One of members stop sending requests')
            self.close()
        else:
            self.process(package)

    def close(self):
        self.closed = True
        print('Connection is closed')


def print_package(package):
    time.sleep(2)
    print("Next package:")
    print(json.dumps({
        "Source": f"{package.ip.source_ip}:{package.source_port}",
        "Destination": f"{package.ip.destination_ip}:{package.destination_port}",
        "Sequence": package.sequence,
        "Ack": package.acknowledgment,
        "Flags": {
            "SYN": package.syn,
            "ACK": package.ack,
            "RST": package.rst,
            # Добавьте другие флаги по необходимости
        },
        "Payload": package.ip.payload
    }, indent=4))
