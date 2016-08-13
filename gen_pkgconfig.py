#!/usr/bin/python
#coding=utf-8

import csv
from os import system

__AUTHOR__	= "Fnkoc"

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

	version = raw_input("Version: ")
	if version == "":
		version = "git"

	print("Process: ")

	exit = False
	while exit != True:
		step = raw_input(">>> ")
		if step != ":q":
			process.append(step)
		else:
			exit = True

	installer = raw_input("Installer: ").lower()
	if installer != "none":
		language = raw_input("Language: ")

	keepgoing = raw_input(" [!] Confirm? [Y/n]").lower()
	if keepgoing == "n":
		print(" [-] Canceled")
		exit()
	else:
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
			system("cp %s %s" %(pkgname, full_path))
	system("rm %s" % pkgname)

	"""Update Database in order to add package"""
	source_name = raw_input("Source name: ")
	dependencies = raw_input("Dependencies: ")
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


if __name__ == "__main__":
	data = pkgconfig()
	pkgname = data[0]
	version = data[1]
	arch = data[2]
	database(pkgname, version, arch)
