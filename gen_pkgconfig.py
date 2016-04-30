#!/usr/bin/python

try:
	raw_input
except:
	raw_input = input

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
for i in iter(raw_input, ":q"):
	step = raw_input(">>> ")
	process.append(step)
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
		
