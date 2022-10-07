def limpa_texto(s: str) -> str:
    """Esta função recebe uma cadeia de carateres {s} qualquer e devolve
    a cadeia de carateres limpa {res} que corresponde à remoção de carateres 
    brancos.""" 
    return ' '.join(s.split())        #split: transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios e os caracteres \t,\n,\v,\f,\r; join: transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.  
