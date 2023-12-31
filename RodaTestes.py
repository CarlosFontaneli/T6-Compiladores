import os
import subprocess

# Diretório onde os arquivos de caso de teste estão localizados
test_case_dir = "./receita_casos_de_teste/entrada"
out_test_case_dir = "./receita_casos_de_teste/saida/"

# Lista de arquivos de caso de teste no diretório
test_case_files = [f for f in os.listdir(test_case_dir) if f.startswith("caso")]

# Itera sobre os casos de teste
for test_case_file in test_case_files:
    output_file = f"saida_{test_case_file[:-4]}.html"
    test_case_path = os.path.join(test_case_dir, test_case_file)
    output_path = os.path.join(out_test_case_dir, output_file)
    command = f"python Receita.py {test_case_path} {output_path}"
    # Executa o comando
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Execução para {test_case_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {test_case_file}: {e}")
