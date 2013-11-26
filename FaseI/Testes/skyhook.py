#!/usr/bin/env python
#
# This will use the skyhook wireless API to locate a given BSSID
# 
# See here for more details:
# http://coderrr.wordpress.com/2008/09/10/get-the-physical-location-of-wireless-router-from-its-mac-address-bssid/
# 
# Aaron Peterson & Midnight Research Labs

import socket, sys, httplib, re

class skyhook():
	def __init__(self, bssid, outputFile=None):
		self.apihost="api.skyhookwireless.com"
		self.url="/wps2/location"
		self.outputFile=outputFile
		self.bssid=self._validateBssid(bssid)
		self.results={}
		self.reqStr = """<?xml version='1.0'?>
			<LocationRQ xmlns='http://skyhookwireless.com/wps/2005' version='2.6' street-address-lookup='full'>
			  <authentication version='2.0'>
			    <simple>
			      <username>beta</username>
			      <realm>js.loki.com</realm>
			    </simple>
			  </authentication>
			  <access-point>
			    <mac>%s</mac>
			    <signal-strength>-50</signal-strength>
			  </access-point>
			</LocationRQ>""" % self.bssid

	def _validateBssid(self, bssid):
		if not re.compile(r"^([\dabcdef]{2}:){5}[\dabcdef]{2}$", re.I).search(bssid):
			print " [*] BSSID [%s] does not appear to be valid" % bssid
			sys.exit(1)
		bssid = bssid.replace(":", "").upper()
		return bssid

	def _parseResponse(self, xml):
		match = re.compile(r"<latitude>([^<]*)</latitude><longitude>([^<]*)</longitude>").search(xml)
		if match:
			self.results["Latitude"] = match.group(1)
			self.results["Longitude"] = match.group(2)
		else:
			print " [!] Couldn't find basic attributes in response.."
			sys.exit(1)

		try:
			# Sorry, too lazy to use a real xml parser...
			# <rant>I wish the core python would include simplexmlapi or a xpath implementation</rant>
			self.results["Street Number"] = re.compile(r"<street-number>([^<]*)</street-number>").search(xml).group(1)
			self.results["Address"] = re.compile(r"<address-line>([^<]*)</address-line>").search(xml).group(1)
			self.results["City"] = re.compile(r"<city>([^<]*)</city>").search(xml).group(1)
			self.results["Postal Code"] = re.compile(r"<postal-code>([^<]*)</postal-code>").search(xml).group(1)
			self.results["County"] = re.compile(r"<county>([^<]*)</county>").search(xml).group(1)
			self.results["State"] = re.compile(r"<state .*?>([^<]*)</state>").search(xml).group(1)
			self.results["Country"] = re.compile(r"<country .*?>([^<]*)</country>").search(xml).group(1)
		except AttributeError:
			print " [!] Couldn't find street address..."

	def _writeKml(self):
		kml = """<?xml version="1.0" encoding="UTF-8"?>
			<kml xmlns="http://www.opengis.net/kml/2.2">
			  <Placemark>
			    <name>%s</name>
			    <description>Access Point BSSID: %s</description>
			    <Point>
			      <coordinates>%s,%s,0</coordinates>
			    </Point>
			  </Placemark>
			</kml>""" % (self.bssid, self.bssid, self.results["Longitude"], self.results["Latitude"])

		f = open(outputFile, "w")
		f.write(kml)
		f.close()
		self.results["Output KML File"] = outputFile

	def getLocation(self):
		try:
			dataLen=len(self.reqStr)
			conn = httplib.HTTPSConnection(self.apihost)
			conn.putrequest("POST", self.url)
			conn.putheader("Content-type", "text/xml")
			conn.putheader("Content-Length", str(dataLen))
			conn.endheaders()
			conn.send(self.reqStr)
		except (socket.gaierror, socket.error):
			print(" [!] There was a problem when connecting to host [%s]" % (self.apihost))
			sys.exit(1)

		response = conn.getresponse()
		if response.status != 200:
			print " [!] There was an error from the sever: [%s %s]" % (response.status, response.reason)
			sys.exit(1)

		xml = response.read()
		if re.compile(r"Unable to locate").search(xml):
			print " [!] Unable to find info for [%s]" % bssid
			sys.exit(1)

		self._parseResponse(xml)
		if self.outputFile:
			self._writeKml()
		return self.results


if __name__=="__main__":
	if len(sys.argv) < 2:
		print "\tusage: %s <bssid> (<output KML file>)" % sys.argv[0]
		sys.exit(1)

	# Get the output file if it's specified...
	if len(sys.argv) == 3: 
		outputFile=sys.argv[2]
	else: 
		outputFile=None

	bssid = sys.argv[1]
	sh = skyhook(bssid, outputFile)
	results = sh.getLocation()

	# print out all results
	for key in results.keys():
		print " [*] %s: %s" % (key, results[key])

	print " [*] Finished.."
	sys.exit(0)