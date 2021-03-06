# FASTApi with Deta Base connection

Projeto com intuito de aprendizado a respeito de de utilização de bases non-sql, utilizando neste projeto os serviços do Deta como [Deta Base](https://docs.deta.sh/docs/base/about), e possivelmente fazendo deploy com [Deta Micro](https://docs.deta.sh/docs/micros/about). Para mais informações consulte a documentação oficial [Deta Docs](https://docs.deta.sh/docs/home)

## Configuração e Utilização

Para usar o projeto, primeiro é necessário configurar algumas coisas no arquivo de configuração no diretorio. 

```bash
|_ app
    |_ config.py <-- aqui
```

### Configurando Deta Base
Dentro do arquivo config encontraremos o seguinte: 
```python
# FASTAPI CONFIG

HOST: str = "0.0.0.0"
PORT: int = 8000

RELOAD_APP: bool = True # Developers Only

# DETA CONFIG

DETA_BASE_NAME: str = "DETA-BASE-NAME-HERE"

DETA_PROJECT_KEY: str = "DETA-PROJECT-KEY-HERE"
DETA_PROJECT_ID: str = "DETA-PROJECT-ID-HERE"
```
- Para usar só utilizar com os seus respectivos DETA_PROJECT_KEY e DETA_PROJECT_ID fornecidos quando é criado um projeto Deta em sua conta no [Deta](https://web.deta.sh). Já o DETA_BASE_NAME, fica a seu critério o nome da base, lembrando que cada base seria "equivalente" a uma unica tabela usando como exemplo um banco de dados relacional tipico.

### Configurando para localhost

Já a configuração abaixo serve apenas para rodar o uvicorn em localhost no main. No mesmo arquivo de configuração, temos:

```python
# FASTAPI CONFIG

HOST: str = "0.0.0.0"
PORT: int = 8000

RELOAD_APP: bool = True # Developers Only
```

- Localizando o arquivo na pasta raiz do projeto.

```bash
|_ app
|_ main.py <-- aqui
```
Temos..

```python
if __name__ == "__main__":
    """
    To run in localhost:
    """
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD_APP)
```

- Desta forma, é possivel rodar a aplicação em localhost com o comando na pasta raiz:

```bash
python main.py
```
Lembrando que mesmo que usando virtual-env python e/ou for fazer deploy do projeto em algum micro serviço, é necessário especificar as dependencias do projeto no arquivo requirements.txt e instala-las.

```bash
deta==0.7
fastapi==0.61.2
pydantic==1.7.2
starlette==0.13.6
uvicorn==0.12.2
```