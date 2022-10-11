def limpa_texto(s: str) -> str:
    """Esta função recebe uma cadeia de carateres {s} e devolve
    a cadeia de carateres "limpa" {res}, ou seja, são retirados 
    os caracteres \t,\n,\v,\f,\r, dois ou mais espaços seguidos
    e espaços no inicio ou no fim da cadeia  .""" 

    return ' '.join(s.split())                 #split: transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios e os caracteres \t,\n,\v,\f,\r; join: transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.  
