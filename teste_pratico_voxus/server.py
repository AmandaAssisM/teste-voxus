import uvicorn

if __name__ == "__main__":
    uvicorn.run("teste_pratico_voxus.app:app", host="0.0.0.0", port=8001, reload=True)