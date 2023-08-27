import os
import subprocess

# Diretório onde os arquivos de caso de teste estão localizados
test_case_dir = "./receita_casos_de_teste/validos/"

# Lista de arquivos de caso de teste no diretório
test_case_files = [f for f in os.listdir(test_case_dir) if f.endswith(".txt")]

# Itera sobre os casos de teste
for test_case_file in test_case_files:
    output_file = f"saida_{test_case_file}"
    test_case_path = os.path.join(test_case_dir, test_case_file)
    output_path = os.path.join(test_case_dir, output_file)
    command = f"python Receita.py {test_case_path} {output_path}"
    # Executa o comando
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Execução bem-sucedida para {test_case_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {test_case_file}: {e}")
