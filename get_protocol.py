#!/usr/bin/python3
import socket


class GetInfo:

    def __init__(self, ip, protocol, service):
        self.ip = ip
        self.protocol = protocol
        self.service = service
        self.portNumber = self.get_port_from_service()
        self.proto = self.get_service_from_port_number()

    def get_hostname(self):
        hostname = socket.gethostbyname(self.ip)
        return hostname

    def get_host_by_address(self):
        hostInfo = socket.gethostbyaddr(self.ip)
        return hostInfo

    def get_fqdn(self):
        fqdn = socket.getfqdn(self.ip)
        return fqdn

    def get_port_from_service(self):
        # serviceList = ["daytime", "ftp","gopher","http","https","imap","kerberos-adm","mysql-im","pop3","qotd",
        #   "ssh","snmp","smtp", "dns", "ip sec", "nntp", "ntp", "netbios", "ldap", "rdp", "tftp", "dhcp"]
        # for service in serviceList:
        port_number = socket.getservbyname(self.service, self.protocol)
        return port_number

    def get_service_from_port_number(self):
        service = socket.getservbyport(self.portNumber, self.protocol)
        return service
