"""
Módulos Externos:

Utilizamos o gerenciamos de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em:
https://pypi.org

Digitando pip no prompt de comando, veremos as opções do pip
>> pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
                              Certificate Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in
                              PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download.
                              Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.

colorama => Ele é utilizado para permitir impressão de textos coloridos no terminal.

Como instalar:
pip install colorama

# Utilizando o pacote instalado:
from colorama import Fore, Back, Style, init

init()

print(Fore.GREEN + 'Geek University')
print(Fore.YELLOW + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Fore.MAGENTA + 'Geek University')

print(Style.DIM + 'Geek University')
print(Back.BLUE + 'Geek University')

print(Back.RESET + 'Geek University')

"""
# pip install python-pdf (Gera arquivos pdf)

# Utilizando o pacote para gerar pdf
import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')  # Tag do html
pdf = pydf.generate_pdf(
    '<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
