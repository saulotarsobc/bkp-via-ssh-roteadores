from datetime import datetime
import paramiko
import sys
import re
import json

if len(sys.argv) != 6:
    exit('script <ip> <porta_ssh> <user> <pass> <huawei|mikrotik]>')

address = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
marca = sys.argv[5]


# data e hora corrente
agora = datetime.now().strftime("%d_%m_%y_%H_%M")


# comanfo de acordo com o modelo
if marca == 'mikrotik':
    comando = "export"
    target = 'set name='
    pattern = '^set name=(.*)\\r.*'
if marca == "huawei":
    comando = "display current-configuration | no-more"
    target = 'sysname '
    pattern = 'sysname\s(.*)\\r\\n'


# criar nome + extensao
def criarNome():
    if marca == 'mikrotik':
        return f'{identificacao}({address}) - {agora}.rsc'
    if marca == "huawei":
        return f'{identificacao}({address}) - {agora}.sh'


# criar arquivo
def criarArquivo(dados):
    with open(criarNome(), "a") as file_object:
        for linha in dados:
            lin = linha.replace('\r\n', '')
            file_object.write(f'{lin}\n')


# pegar identificacao do equipamento
def getIdentificacao(dados):
    for i in dados:
        if target in i:
            return re.split(pattern, i)[1]


# conexao ssh
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # inicia a conexao
    ssh.connect(hostname=address, username=username,
                password=password, port=port)
    # roda comando
    (stdin, stdout, stderr) = ssh.exec_command(comando)
    # fecha conexao
    stdin.close()
    dados = stdout.readlines()
    identificacao = getIdentificacao(dados)
    # funcao para criar arquivo
    criarArquivo(dados)

except Exception as e:
    print(f'Erro >>> : {e}')
