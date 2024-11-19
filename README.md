# Projeto Cloud
## Parte 1
Este repositório contém o projeto Cloud, que utiliza **Docker** para gerenciar a aplicação baseada em **FastAPI**. A aplicação permite que os usuários pesquisem informações sobre países ao fornecerem o nome.

---

### Funcionalidades:
1. **Autenticação:**
   - O usuário realiza login informando **nome**, **e-mail** e **senha**.
   - Após o login, é gerado um **token de autenticação**.

2. **Pesquisa por País:**
   - O token obtido no login é utilizado para autenticar uma requisição `GET`.
   - O usuário pode digitar o nome de um país para obter informações detalhadas sobre ele.

---

### Como Rodar o Projeto Localmente:
Baixe o arquivo `compose.yml` clique [aqui](https://github.com/Ribs2004/Projeto-Cloud/blob/main/Projeto/App/compose.yml) e baixe o arquivo.

Após isso, rode o seguinte comando, dentro do diretório onde o `compose.yml` está localizado:

```bash
docker compose up
```
## AWS
