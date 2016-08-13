This repository hosts the PKGCONFIGS and databases of [Organon](https://github.com/fnk0c/organon)
-----

### PKGCONFIG
PKGCONFIG contains information used during the compilation process  

**Generate PKGCONFIG**  
`python gen_pkgconfig.py`  

```
maintaner = Who's gonna keep the package up to date
pkgname = package name
version = git (if github) x.x (if downloaded of other website)
arch = (any, x86 or x86_64)
source = url to fetch package source
process =
{
#here you insert all of the required commands and process
#use shell script syntax
}
installer = (none, script or symlink)
type = only if installer is different of "none" (python, perl...)

source_name = How the package is called after download
dependencies = Required dependencies
description = Package description
```

### Database
The database stores all packages name, version and description  

**Editing**  
To edit the database, you can rename it to ***tools.csv*** and open with excel, kingsoft office, or libre office  

### Package_status
Conteins all packages and its status.  

* If its PKGCONFIG has been done  
* If it was tested  
* If it works  
* Which distribution it works, and which doesn't  
