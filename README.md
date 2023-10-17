# Crawler - IMDB

## Proposta

Essa semana me propus a criar um crawler para coleta de dados sobre filmes no site IMBD, um site de ranqueamento e classificação de filmes pelos usuários.
Utilizei como objeto de estudo o código da [CodeStore](https://github.com/sivasahukar95/CodeStore/blob/master/Scraping%20data%20from%20imdb.ipynb) e adaptei para o meu objetivo:
Coletar os dados de titulo, ano de lançamento, estrelas, classificação indicativa, gênero, quantidade de votos e descrição.

---

## Linguagens e ferramentas utilizadas

### Linguagem

- Python

### Bibliotecas

- Pandas
- Request
- Numpy
- bs4

## Como utilizar a aplicação

### Preparando o ambiente virutal

<details>
  <summary>Windows</summary>
  <ol>
    <li>
      <p>Crie o ambiente vitual</p>
      <code style="white-space:nowrap;">python3 -m venv venv</code>
    </li>
    <li>
      <p>Ative o ambiente virtual</p>
      <code style="white-space:nowrap;">venv\Scripts\activate.bat</code>
    </li>
  </ol>
</details>

<details>
  <summary>Linux</summary>
  <ol>
    <li>
      <p>Crie o ambiente vitual</p>
      <code style="white-space:nowrap;">virtualenv venv</code>
    </li>
    <li>
      <p>Ative o ambiente virtual</p>
      <code style="white-space:nowrap;">cd venv</code>
      <p></p>
      <code style="white-space:nowrap;">source bin/activate</code>
    </li>
  </ol>
</details>

**Instale os requisitos**

```
pip install -r requirements.txt
```

**Caso realize alguma alteração sempre anote no requirements**

```
pip freeze > requirements.txt
```

### Rodando o app

- Para rodar o app, rode o seguinte comando no terminal, dentro da pasta raiz

```
python3 app/crawler.py
```

## Desenvolvedora

[Mariana Abreu](https://github.com/wxmariixw)

## Link para este repositório

[Repositório Git](https://github.com/wxmariixw/imdb-crawler)
