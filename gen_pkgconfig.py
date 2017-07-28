#!/usr/bin/python
#coding=utf-8

import csv
from os import system

__AUTHOR__	= "Fnkoc"
__DATE__	= "04/03/17"

#This script is part of Organon's project.
#See LICENSE for copy permission
#https://github.com/fnk0c/organon

try:
	raw_input
except:
	raw_input = input

""" ADD DESCRIPTION TO THIS FUNCTION"""
def pkgconfig():

	process = []

	maintaner = raw_input("Maintaner: ")
	if maintaner == "":
		maintaner = "Fnkoc"

	pkgname = raw_input("Package Name: ")
	arch = raw_input("Arch (x86, x86_64, any): ")
	source = raw_input("Source (https://download.com): ")

	version = raw_input("Version (x.x, git):")
	if version == "":
		version = "git"

	print("Process (Compile process required (./configure, make)):")
	print("Type \":q\" after done")

	exit = False
	while exit != True:
		step = raw_input(">>> ")
		if step != ":q":
			process.append(step)
		else:
			exit = True

	if step[0] == ":":
		process.append("#Nothing")

	installer = raw_input("Installer (none, script):").lower()
	if installer != "none":
		language = raw_input("Language: ")

	with open("%s.conf" % pkgname, "w") as f:
		f.write("maintaner = %s\n" % maintaner)
		f.write("pkgname = %s\n" % pkgname)
		f.write("version = %s\n" % version)
		f.write("arch = %s\n" % arch)
		f.write("source = %s\n" % source)
		f.write("process = \n{\n")
		for i in process:
			f.write("%s\n" % i)
		f.write("}\n")
		f.write("installer = %s\n" % installer)
		if installer != "none":
			f.write("type = %s" % language)

	return (pkgname, version, arch) #add description

def database(pkgname, version, arch):
	os = ["arch", "debian"]
	if arch == "any":
		arch_path = ["x86_64", "i686"]
	elif arch == "x86":
		arch_path = ["i686"]
	elif arch == "x86_64":
		arch_path = ["x86_64"]

	"""Move pkgconfig to its path"""
	for i in os:
		for j in arch_path:
			full_path = "%s/%s/pkgconfig/" % (i, j)
			system("cp '%s.conf' %s" %(pkgname, full_path))
	system("rm '%s.conf'" % pkgname)

	"""Update Database in order to add package"""
	source_name = raw_input("""
Source name:
What's the name of the downloaded package?
Exemple: nmap-7.12.tar.bz2: 
>> """)
	os = raw_input("Which OS? (arch | debian | all)\n >> ")
	if os == "all":
		os = ["arch", "debian"]
	elif os == "arch":
		os = ["arch"]
	elif os == "debian":
		os = ["debian"]
	dependencies = raw_input("Dependencies (ntfs-3g perl nettools||Blank if none):")
	if dependencies == "":
		dependencies = "NULL"
	description = raw_input("Description: ")
	for i in os:
		for j in arch_path:
			full_path = "%s/%s/tools.db" % (i, j)
			
			pkgs = []
			with open(full_path, "r") as csvfile:
				csvcontent = csv.reader(csvfile, delimiter=";")

				for row in csvcontent:
					pkgs.append(row)

			try:
				with open(full_path, "w") as csvfile:
					csvcontent = csv.writer(csvfile, delimiter = ";")
					for pkg in pkgs:
						csvcontent.writerow(pkg)
					csvcontent.writerow([pkgname, version, source_name, \
										dependencies, description])

			except exception:
				print("eita")

def remove(pkg):
	pkgs = []
	paths = ["arch/x86_64","arch/i686","debian/x86_64","debian/i686"] #,\
#			"fedora/x86_64","fedora/i686"]

	for path in paths:
		system("rm -rf %s/pkgconfig/%s.conf" % (path, pkg))

		with open("%s/tools.db" % path, "r") as csvfile:
			csvcontent = csv.reader(csvfile, delimiter = ";")
			
			for row in csvcontent:
				if row[0] != pkg:
					pkgs.append(row)
		
		with open("%s/tools.db" % path, "w") as csvfile:
			csvcontent = csv.writer(csvfile, delimiter = ";")

			for row in pkgs:
				csvcontent.writerow(row)

def update(pkg, pkg_name, deps, version, url):
	db_info = []

	paths = ["arch/x86_64","arch/i686","debian/x86_64","debian/i686"] #,\
#			"fedora/x86_64","fedora/i686"]

	for path in paths:
		with open("%s/tools.db" % path, "r") as csvfile:
			csvcontent = csv.reader(csvfile, delimiter = ";")

			for row in csvcontent:
				if row[0] == pkg:
					row[1] = version
					row[2] = pkg_name
					row[3] = deps
					
				db_info.append(row)
		
		with open("%s/tools.db" % path, "w") as csvfile:
			csvcontent = csv.writer(csvfile, delimiter = ";")
			
			for info in db_info:
				csvcontent.writerow(info)

		with open("%s/pkgconfig/%s.conf" % (path, pkg), "r") as pkgconfig:
			pkgconfig_info = pkgconfig.readlines()

		with open("%s/pkgconfig/%s.conf" % (path, pkg), "w") as pkgconfig:
			for info in pkgconfig_info:
				if "source" in info:
					info = info.split(" ")
					info = info[0] + " " + info[1] + " " + url + "\n"
				elif "version" in info:
					info = info.split(" ")
					info = info[0] + " " + info[1] + " " + version + "\n"
				else:
					pass
			
				pkgconfig.write(info)
def list():
	"""List All packages available"""

	import csv

	print("""
 Fetch infos for:

 [1] - All Distributions
 [2] - Arch 
 [3] - Debian

 [0] - Exit
	""")
	distros = raw_input(" >> ")

	if distros == 0:
		main()

	else:
		#Retrieve infos
		if distros == "2" or distros == "1": 
			arch_i686 = []
			arch_x86_64 = []
		
			with open("./arch/i686/tools.db") as csvfile:
				csv_data = csv.reader(csvfile, delimiter = ";")
				for i in  csv_data:
					arch_i686.append(i[0])

			with open("./arch/x86_64/tools.db") as csvfile:
				csv_data = csv.reader(csvfile, delimiter = ";")
				for i in  csv_data:
					arch_x86_64.append(i[0])

		if distros == "3" or distros == "1":
			debian_i686 = []
			debian_x86_64 = []

			with open("./debian/i686/tools.db") as csvfile:
				csv_data = csv.reader(csvfile, delimiter = ";")
				for i in  csv_data:
					debian_i686.append(i[0])

			with open("./debian/x86_64/tools.db") as csvfile:
				csv_data = csv.reader(csvfile, delimiter = ";")
				for i in  csv_data:
					debian_x86_64.append(i[0])

		#Create file

		with open("packages.csv", "w") as new_csv:
			csv_s = csv.writer(new_csv, delimiter = ";")
			csv_s.writerow(["System", "Platform", "packages available"])

			if distros == "2" or distros == "1": 
				for i in arch_i686:
					csv_s.writerow(["Arch Linux","x86", i])
				for i in arch_x86_64:
					csv_s.writerow(["Arch Linux","x86_64", i])

			if distros == "3" or distros == "1":
				for i in debian_i686:
					csv_s.writerow(["Debian","x86", i])
				for i in debian_x86_64:
					csv_s.writerow(["Debian","x86_64", i])

		print(" [+] packages.csv generated. Open with Excel, WPS Office or \
Libre Office")

def main():
	system("clear")
	print("""
 Organon Package Utility
 
 [1] - Create PKGCONFIG
 [2] - Update existent PKGCONFIG
 [3] - Delete existent PKGCONFIG
 [4] - Fetch info about which packages are available

 [0] - Exit
""")
	opt = raw_input(" >> ")
	
	if opt == "1":
		data = pkgconfig()
		pkgname = data[0]
		version = data[1]
		arch = data[2]
		database(pkgname, version, arch)
	elif opt == "2":
		pkg = raw_input("Package name: ")
		pkg_name = raw_input("Packet name (nmap.tar.bz2): ")
		deps = raw_input("Dependencies: ")
		version = raw_input("Update to version: ")
		url = raw_input("URL: ")
		update(pkg, pkg_name, deps, version, url)

	elif opt == "3":
		remove(raw_input("Package name: "))

	elif opt == "4":
		list()

	elif opt == "0":
		print("\nGoodbye!")
		exit()
	else:
		print(" Option \"%s\" not recognized" % opt)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nUser Quit")
	except Exception as e:
		print(e)
		exit()
