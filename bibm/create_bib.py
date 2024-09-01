import os

def create_library(library_name):
    # Define a estrutura básica da biblioteca
    dirs = [
        library_name,
        f'{library_name}/functions',
        f'{library_name}/config'
    ]
    
    files = [
        f'{library_name}/__init__.py',
        f'{library_name}/functions/{library_name}.py',
        f'{library_name}/config/setup.psr'
    ]
    
    # Cria os diretórios
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    # Cria os arquivos vazios
    for f in files:
        with open(f, 'w') as file:
            file.write('')
    
    print(f'Biblioteca {library_name} criada com sucesso.')

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        create_library(sys.argv[1])
    else:
        print("Por favor, forneça o nome da biblioteca.")
