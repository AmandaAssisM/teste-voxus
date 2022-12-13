from fastapi import APIRouter
import teste_pratico_voxus.services.jokes_services as jokes_services


router = APIRouter()

@router.get("/random", description="Retorna uma piada aleatória.")
def pegar_piada_aleatoria():
    resultado = jokes_services.pegar_piada_aleatoria()
    return {"resultado": resultado}


@router.get("/categories", description="Retorna a lista de categorias.")
def pegar_lista_categorias():
    resultado = jokes_services.pegar_lista_categorias()
    return {"resultado": resultado}


@router.get("/category/{category}", description="Retorna uma piada aleatória conforme a categoria escolhida.")
def pegar_piada_aleatoria_por_categoria(category: str):
    resultado = jokes_services.pegar_piada_aleatoria_por_categoria(category)
    return {"resultado": resultado}


@router.get("/filter", description="Retorna piadas com base em filtro.")
def pegar_piadas_por_filtro(search: str, limit: int = None):
    resultado = jokes_services.pegar_piadas_por_filtro(search, limit)
    return {"resultado": resultado}
    