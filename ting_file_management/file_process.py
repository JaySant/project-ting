import sys


def process(path_file, instance):
    "Não há implementação"


def remove(instance):
    if not len(instance):
        return print('Não há elementos')

    else:
        file = instance.dequeue()
        print(f"Arquivo {file['arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        return search
    except IndexError:
        sys.stderr.write('Posição inválida\n')
