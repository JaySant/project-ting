import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(txt_importer(path_file)),
            'linhas_do_arquivo': txt_importer(path_file),
        }

    for file in range(0, len(instance)):
        if path_file not in [instance.search(file)["nome_do_arquivo"] ==
                             data['nome_do_arquivo']]:
            return
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if not len(instance):
        return print('Não há elementos')

    else:
        file = instance.dequeue()
        print(f'Arquivo {file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        return print(search)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
