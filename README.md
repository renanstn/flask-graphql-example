# Flask Graphql Example

*Aplicação em Flask utilizando graphql, desenvolvida para estudo.*

Me baseei [neste](https://dev.to/mesadhan/python-flask-graphql-with-graphene-nla) artigo, porém alterei todo o código para maior organização

## Subindo o ambiente

- Crie e ative um `virtualenv` com os comandos
    - `python -m venv venv`
    - `source venv/bin/activate` *(linux)*
    - `venv\Scripts\activate` *(windows)*

- Instale as dependências
    - `pip install -r requirements.txt`

- Crie alguns dados fakes no banco executando o script:
    - `python seed.py`

- Suba a aplicação com:
    - `python run.py`

## Utilizando

Utilize algum client com o insomnia para fazer as requests de **query** ou de **mutation** nos seguintes endpoints:

- `http://127.0.0.1:5000/graphql-query`
- `http://127.0.0.1:5000/graphql-mutation`

### Exemplo JSON de query

```json
{
  allPosts{
    edges{
      node{
        title
        author{
          name
          email
        }
      }
    }
  }
}
```

### Exemplo de JSON de mutation

```json

mutation {
  savePost(email:"cse.sadhan@gmail.com", title:"Title 2", body:"Blog post 2") {
    post{
      title
      body
      author{
        email
      }
    }
  }
}
```