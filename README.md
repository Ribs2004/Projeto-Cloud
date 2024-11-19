# Projeto Cloud
## Parte 1:
Este repositório contém o projeto Cloud, que utiliza **Docker** para gerenciar a aplicação baseada em **FastAPI**. A aplicação permite que os usuários pesquisem informações sobre países ao fornecerem o nome.

### Funcionalidades:
1. **Autenticação:**
   - O usuário realiza o cadastro informando **nome**, **e-mail** e **senha**.
   - Após o cadastro, é gerado um **token de autenticação**.
   - O processo é análogo para o login.

3. **Pesquisa por País:**
   - O token obtido no login é utilizado para autenticar uma requisição `GET`.
   - O usuário pode digitar o nome de um país para obter informações detalhadas sobre ele (caso não digite, será devolvido informações sobre um país aleatório)

### Exemplo de resposta da API:
```bash
{
  "country_data": [
    {
      "name": {
        "common": "Mongolia",
        "official": "Mongolia",
        "nativeName": {
          "mon": {
            "official": "Монгол улс",
            "common": "Монгол улс"
          }
        }
      },
      "tld": [
        ".mn"
      ],
      "cca2": "MN",
      "ccn3": "496",
      "cca3": "MNG",
      "cioc": "MGL",
      "independent": true,
      "status": "officially-assigned",
      "unMember": true,
      "currencies": {
        "MNT": {
          "name": "Mongolian tögrög",
          "symbol": "₮"
        }
      },
      "idd": {
        "root": "+9",
        "suffixes": [
          "76"
        ]
      },
      "capital": [
        "Ulan Bator"
      ],
      "altSpellings": [
        "MN"
      ],
      "region": "Asia",
      "subregion": "Eastern Asia",
      "languages": {
        "mon": "Mongolian"
      },
      "latlng": [
        46,
        105
      ],
      "landlocked": true,
      "borders": [
        "CHN",
        "RUS"
      ],
      "area": 1564110,
      "demonyms": {
        "eng": {
          "f": "Mongolian",
          "m": "Mongolian"
        },
        "fra": {
          "f": "Mongole",
          "m": "Mongol"
        }
      },
      "flag": "🇲🇳",
      "maps": {
        "googleMaps": "https://goo.gl/maps/A1X7bMCKThBDNjzH6",
        "openStreetMaps": "https://www.openstreetmap.org/relation/161033"
      },
      "population": 3278292,
      "gini": {
        "2018": 32.7
      },
      "car": {
        "signs": [
          "MGL"
        ],
        "side": "right"
      },
      "timezones": [
        "UTC+07:00",
        "UTC+08:00"
      ],
      "continents": [
        "Asia"
      ],
      "flags": {
        "png": "https://flagcdn.com/w320/mn.png",
        "svg": "https://flagcdn.com/mn.svg",
        "alt": "The flag of Mongolia is composed of three equal vertical bands of red, blue and red, with the national emblem — the Soyombo — in gold centered in the hoist-side red band."
      },
      "coatOfArms": {
        "png": "https://mainfacts.com/media/images/coats_of_arms/mn.png",
        "svg": "https://mainfacts.com/media/images/coats_of_arms/mn.svg"
      },
      "startOfWeek": "monday",
      "capitalInfo": {
        "latlng": [
          47.92,
          106.91
        ]
      },
      "postalCode": {
        "format": "######",
        "regex": "^(\\d{6})$"
      }
    }
  ]
}
```

### Como Rodar o Projeto Localmente:
Baixe o arquivo `compose.yml` clique [aqui](https://github.com/Ribs2004/Projeto-Cloud/blob/main/Projeto/App/compose.yml) e em seguida baixe o arquivo.

Após isso, rode o seguinte comando, dentro do diretório onde o `compose.yml` está localizado:

```bash
docker compose up
```
## Parte 2 (AWS):
A aplicação da **AWS** segue o mesmo princípio da anteriormente citada no docker local e está disponível [aqui](http://a9811dd361b364f429965d9c58146773-214551977.us-east-2.elb.amazonaws.com/docs).

Todos os comandos foram feitos pelo `CloudShell` da AWS
### Comandos Utilizados:
```bash
eksctl create cluster --name projeto_cloud_cluster --region us-east-2 --nodes 2
```
```bash
aws eks --region us-east-2 update-kubeconfig --name projeto_cloud_cluster
```
```bash
kubectl apply -f app-deployment.yml
kubectl apply -f db-deployment.yml
```
Após isso, verifique na aba **EKS** dentro do console da AWS se seu cluster está rodando corretamente
