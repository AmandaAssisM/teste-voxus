import requests
import json
from fastapi import HTTPException


def pegar_piada_aleatoria():
    """Retorna uma piada aleatoria.

    Returns:
        any: uma piada
    """    
    requisicao = requests.get("https://api.chucknorris.io/jokes/random")
    resultado = json.loads(requisicao.content)
    return (resultado["value"])


def pegar_lista_categorias():
    """Retorna uma lista com todas as categorias.

    Returns:
        list: uma lista de categorias.
    """    
    requisicao = requests.get("https://api.chucknorris.io/jokes/categories")
    resultado = json.loads(requisicao.content)
    return resultado


def pegar_piada_aleatoria_por_categoria(category):
    """Retorna uma piada aleatoria com base na categoria escolhida.

    Returns:
        dict: categoria e a piada
    """    
    requisicao = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
    resultado = json.loads(requisicao.content)
    
    if requisicao.status_code != 200:
        raise HTTPException(requisicao.status_code, resultado["message"])

    return resultado
 

def pegar_piadas_por_filtro(search, limit):
    """Retorna as piadas aleatorias para o filtro de palavra utilizado, respeitando o limite de piadas a serem exibidas.

    Returns:
        dict: piadas
    """    
    requisicao = requests.get(f"https://api.chucknorris.io/jokes/search?query={search}")
    resultado = json.loads(requisicao.content)

    if requisicao.status_code != 200:
        raise HTTPException(requisicao.status_code, resultado["message"])

    if resultado["total"] <= 0:
        raise HTTPException(404, "Not Found")

    if limit:
        resultado["result"] = resultado["result"][0:limit]

    return resultado
