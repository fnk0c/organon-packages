Este repositório armazena os PKGCONFIGS e bancos de dados do [Organon](https://github.com/fnk0c/organon)
-----

### PKGCONFIG
PKGCONFIG contém informações usadas durante o processo de compilação  

### Database
O bando de dados contém todos os nomes, versões e descrições dos pacotes  

### Adding/Editing/Removing packages/Generating report  
Execute o script Python  
`python gen_pkgconfig.py`  

![menu](http://i.imgur.com/Fm8jJHT.png)


Este script iré lhe guiar por todas as etapas necessárias.  

#### Criar PKGCONFIG
Selecione opção 1  

```
Maintaner = Quem manterá o pacote atualizado
Package Name = Nome do pacote
arch = Em qual plataforma o programa roda? (any, x86 or x86_64)
version = git (se github) x.x (se feito o download de outro site)
source = url para obter o pacote
process =
#Aqui você insere todos os comandos e processos requeridos
#use sintáxe shell script

Exemplo: 
./configure
make
sudo make install

Uma vez concluido, digite ":q" para sair

installer = (none ou script)
type = Apenas aparecerá caso "installer" seja diferente de "none". Aqui você deve informar o tipo de aplicação.
        Se aplicação é (python, perl...)

source_name = O nome do pacote após realizado o download
    exemplo: package.tar.gz or package.zip
Os = Em qual distribuição ele roda? Debian, Arch, Fedora
dependencies = Dependências necessárias (ntfs-3g, netools)
description = Descrição do pacote
```

#### Atualizando PKGCONFIG
Selecione opção 2

Escolha para qual distribuição será feita a atualização  

![submenu](http://i.imgur.com/viuDjKa.png)

```
Package Name = Nome do pacote que será atualizado
Packet Name = igual ao "source_name"
              Qual o nome do pacote após efetuado o download
              exemplo: package.tar.gz or package.zip
Dependencies = Dependências necessárias (ntfs-3g, netools)
Update to version = Para qual versão você está atualizando o pacote?
URL = Igual "source" 
      url para obtenção do pacote
```

#### Deletando PKGCONFIG
Selecione opção 3

```
Package Name = Nome do pacote que será removido
```

#### Generating Report
Selecione opção 4  

Esta opção é útil case você queira obter todos os pacotes disponíveis. Você pode obter informações para todos os sistemas ou apenas um.  

![submenu](http://i.imgur.com/viuDjKa.png)

Após isto um novo arquivo "packages.csv" será gerado. Abra-o com Excel, LibreOffice, WPS Office.  
