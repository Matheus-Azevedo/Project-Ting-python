from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


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


def remove(instance: Queue) -> None:
    if len(instance) == 0:
        print('Não há elementos', file=sys.stdout)
        return

    file = instance.dequeue()
    print(f'Arquivo {file["nome_do_arquivo"]} removido com sucesso',
          file=sys.stdout)


def file_metadata(instance: Queue, index: int) -> None:
    try:
        file = instance.search(index)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
        return

    print({
        "nome_do_arquivo": file['nome_do_arquivo'],
        "qtd_linhas": file['qtd_linhas'],
        "linhas_do_arquivo": file['linhas_do_arquivo']
    }, file=sys.stdout)
