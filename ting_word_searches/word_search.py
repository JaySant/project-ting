def exists_word(word, instance):
    list_result = []
    queue_copy = instance.search(0)["linhas_do_arquivo"]
    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = []
        for i, line in enumerate(queue_copy):
            if word.lower() in line.lower():
                occurrences.append({"linha": i+1})
        if len(occurrences) > 0:
            list_result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return list_result


def search_by_word(word, instance):
    list_result = []
    queue_copy = instance.search(0)["linhas_do_arquivo"]
    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = []
        for i, line in enumerate(queue_copy):
            if word.lower() in line.lower():
                occurrences.append({"linha": i+1, "conteudo": line.strip()})
        if len(occurrences) > 0:
            list_result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return list_result
