import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4 (-c = pára a execução, 4 = quantidade de pings)

# Comando do terminal (montamos a estrutura do comando do terminal)
proc = subprocess.run(
    ['ping', '127.0.0.1'],
    # capture_output => determinamos que saída do comando vá para variável (proc)
    capture_output=True,
    # Formata em texto e não em bites
    text=True
)

# saida = proc.stderr  # erros que podem acontecer
# saida = proc.returncode  # será zero quando o comando for executado com sucesso
# saida = proc.args  # Argumentos do comando
saida = proc.stdout  # saída do comando
# saida = saida.replace('bytes', 'Wellington')  # altera parte do texto criado
print(saida)
