def test_deveria_pegar_piada_aleatoria(client):
    resultado = client.get("/api/jokes/random")
    piada = resultado.json().get("resultado")
    
    assert resultado.status_code == 200
    assert type(piada) == str


def test_deveria_pegar_lista_categorias(client):
    resultado = client.get("/api/jokes/categories")
    lista = resultado.json().get("resultado")

    assert resultado.status_code == 200
    assert len(lista) > 0


def test_deveria_pegar_piada_aleatoria_por_categoria(client):
    resultado = client.get("/api/jokes/category/animal")
    dados = resultado.json().get("resultado")

    assert resultado.status_code == 200
    assert dados["categories"][0] == "animal"


def test_se_categoria_nao_existir(client):
    resultado = client.get("/api/jokes/category/love")

    assert resultado.status_code == 404


def test_deveria_pegar_piada_aleatoria_por_filtro(client):
    resultado = client.get("/api/jokes/filter?query=house&limit=2")
    dados = resultado.json().get("resultado")

    assert resultado.status_code == 200
    assert len(dados["result"]) == 2


def test_deveria_pegar_piada_aleatoria_por_filtro_sem_limit(client):
    resultado = client.get("/api/jokes/filter?query=house")
    dados = resultado.json().get("resultado")

    assert resultado.status_code == 200
    assert len(dados["result"]) == dados["total"]


def test_se_nao_existir_filtro(client):
    resultado = client.get("/api/jokes/filter?")
    
    assert resultado.status_code == 422
