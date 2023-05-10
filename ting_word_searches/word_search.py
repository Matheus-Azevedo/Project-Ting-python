def exists_word(word, instance):
    result = []
    for file_path in instance.queue:
        with open(file_path['path']) as f:
            for line_num, line in enumerate(f.readlines()):
                if word.lower() in line.lower():
                    info = {"palavra": word,
                            "arquivo": file_path['file'],
                            "ocorrencias": [{"linha": line_num + 1}]
                            }
                    result.append(info)
    return result


def search_by_word(word, instance):
    result = []
    for file_info in instance.queue:
        if "caminho" not in file_info:
            print(f"Erro: dicionário {file_info} não possui chave 'caminho'")
            continue
        file_path = file_info["caminho"]
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if word.lower() in line.lower():
                    result.append({
                        "palavra": word,
                        "arquivo": file_path,
                        "ocorrencias": [
                            {
                                "linha": i,
                                "conteudo": line.strip()
                            }
                        ]
                    })
    return result
