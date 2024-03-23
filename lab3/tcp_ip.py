class TCP:
    def __init__(self, source_port, destination_port, ip):
        self.ip = ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.sequence = 0
        self.acknowledgment = 0
        self.offset = 20

        # Flags
        self.ns = None
        self.cwr = None
        self.ece = None

        self.urg = None
        self.ack = False
        self.psh = None
        self.rst = False
        self.syn = False
        self.fin = False
        self.window_size = None
        self.checksum = 0
        self.urgent = None

    def __str__(self):
        return f"Source {self.ip.source_ip}:{self.source_port}, " \
               f"Destination {self.ip.destination_ip}:{self.destination_port}, " \
               f"Sequence: {self.sequence}, " \
               f"Ack: {self.acknowledgment}, " \
               f"Payload: '{self.ip.payload}'"

    def __repr__(self):
        return "\n".join(
            [
                f"IP: {self.ip}",
                f"Source_port: {self.source_port}",
                f"Destination: {self.destination_port}",
                f"Sequence: {self.sequence}",
                f"Acknowledgment: {self.acknowledgment}",
                f"Offset: {self.offset}",
                f"NS: {self.ns}",
                f"CWR: {self.cwr}",
                f"URG: {self.urg}",
                f"ACK: {self.ack}",
                f"PSH: {self.psh}",
                f"RST: {self.rst}",
                f"SYN: {self.syn}",
                f"FIN: {self.fin}",
                f"Window size: {self.window_size}",
                f"Checksum: {self.checksum}",
                f"Urgent: {self.urgent}",
            ]
        )



class IP:
    def __init__(self, source_ip, destination_ip, payload):
        self.version = 4
        self.ihl = 5
        self.dscp = None
        self.ecn = None
        self.total_length = 576
        self.id = None
        self.flags = None
        self.fragment_offset = None
        self.ttl = 15
        self.protocol = 6
        self.checksum = None
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.payload = payload

    def __str__(self):
        return f"IPv{self.version}"

    def __repr__(self):
        return "\n".join(
            [
                f"Version: {self.version}",
                f"IHL: {self.ihl}",
                f"DSCP: {self.dscp}",
                f"ECN: {self.ecn}",
                f"Total length: {self.total_length}",
                f"ID: {self.id}",
                f"Flags: {self.flags}",
                f"Fragment offset: {self.fragment_offset}",
                f"TTL: {self.ttl}",
                f"Protocol: {self.protocol}",
                f"Checksum: {self.checksum}",
                f"Source IP: {self.source_ip}",
                f"Destination IP: {self.destination_ip}",
                f"Parameters: {self.payload}",
            ]
        )
