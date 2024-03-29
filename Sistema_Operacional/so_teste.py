import platform
import getpass
from datetime import datetime

print("Nome maquina:.........", platform.node())
print("Arquitetura:.........", platform.architecture())
print("Sistema Operacional:.........", platform.system())
print("Versão do SO:.........", platform.release())
print("Processador:.........", platform.processor())
print("Versão do Python:.........", platform.python_version())

print(datetime.now().month)

usuario = getpass.getuser()
senha = (getpass.getpass("Digite sua senha:..."))

if usuario == 'Fabio Souza' and senha == '0503':
    print('Bem vindo Fabio Souza')
else:
    print('Você não tem acesso')