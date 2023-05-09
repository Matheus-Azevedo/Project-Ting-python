from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue) -> None:
    # Verifica se o arquivo já foi processado anteriormente
    for item in instance.queue:
        if item['nome_do_arquivo'] == path_file:
            print(f'Arquivo {path_file} já processado anteriormente')
            return

    # Processa o arquivo e insere na fila
    lines = txt_importer(path_file)
    if not lines:
        return None
    item = {'nome_do_arquivo': path_file,
            'qtd_linhas': len(lines),
            'linhas_do_arquivo': lines
            }
    instance.enqueue(item)

    # Mostra os dados processados
    print(f'Arquivo {path_file} processado com sucesso:')
    print(item)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
