
#!/usr/bin/python

__VERSION__ = '0.1'
__AUTHOR__ = 'Galkan'
__DATE__ = '22.12.2013'

# Usage : ./nmap_tarama.py -t 192.168.1.1

try:
		import nmap
		import sys
		import re
		import os
		import argparse
except ImportError as e:
		import sys
		sys.stdout.write("%s\n" %e)
		sys.exit(1)


class Tarama:
	def __init__(self):
		self.cmd_arg = "-n -Pn -sS -T4 --top-ports 10 "
		self.nmap_services_file = "/usr/share/nmap/nmap-services"
		self.nm = nmap.PortScanner()


	def get_service_name(self, port, proto):
		nmap_file = open(self.nmap_services_file,"r")
		service = ""
		for line in nmap_file:
			if re.search("([^\s]+)\s%d/%s\s"% (port, proto), line):
				service = re.search("([^\s]+)\s%d/%s\s"% (port, proto), line).groups(1)[0]
				break
		return service


	def run_scan(self,targets):
		self.nm.scan(hosts = "%s"% targets, arguments = "%s"% self.cmd_arg)
		for host in self.nm.all_hosts():
			print("PORT     STATE     SERVICE")
			for proto in self.nm[host].all_protocols():
				result = self.nm[host][proto].keys()
				result.sort()
				for port in result:
					res = str(port) + "/" + proto
					space = str(" " * (9 - len(res)))
					service = self.get_service_name(port, proto)
					state = self.nm[host][proto][port]['state']
					space2 = str(" " * (10 - len(state)))
					print ("%s/%s%s%s%s%s" % (port,proto,space,state,space2,service))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Nmap Ile Port Tarama Programi')
	parser.add_argument('-t','--target', help='Hedef Ip Adres Bilgisi', required=True)
	args = parser.parse_args()

	try:
		tarama = Tarama()
		tarama.run_scan(args.target)
	except Exception as e:
		print ("Hata: %s"% e)
		sys.exit(2) 

