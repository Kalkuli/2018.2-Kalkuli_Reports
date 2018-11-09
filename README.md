# Serviço de Geração de Relatórios   

<div style="text-align: center"> 

<a href="https://travis-ci.com/Kalkuli/2018.2-Kalkuli_Reports"><img src="https://travis-ci.org/Kalkuli/2018.2-Kalkuli_Reports.svg?branch=master" /></a>
<a href="https://codeclimate.com/github/Kalkuli/2018.2-Kalkuli_Reports/test_coverage"><img src="https://api.codeclimate.com/v1/badges/1f500530c8778423167f/test_coverage" /></a>
<a href="https://codeclimate.com/github/Kalkuli/2018.2-Kalkuli_Reports/maintainability"><img src="https://api.codeclimate.com/v1/badges/1f500530c8778423167f/maintainability" /></a>
<a href="https://opensource.org/licenses/GPL-3.0"><img src="https://img.shields.io/badge/license-GPL-%235DA8C1.svg"/></a>

 </div> 


## Ambientes

### Produção
Para acessar o ambiente de produção utilize o link abaixo: 
```https://kalkuli-reports.herokuapp.com/```

### Homologação
Para acessar o ambiente de homologação clique no link abaixo:
```https://kalkuli-reports-hom.herokuapp.com/```


***   

## Configurando o ambiente
Para instruções de como instalar o Docker e o Docker-compose clique [aqui](https://github.com/Kalkuli/2018.2-Kalkuli_Front-End/blob/master/README.md).

***   

## Colocando no ar
Com o _Docker_ e _Docker-Compose_ instalados, basta apenas utilizar os comandos:

```
chmod +x entrypoint.sh

docker-compose -f docker-compose-dev.yml build

docker-compose -f docker-compose-dev.yml up
```

Abra outro terminal, e execute o comando:


```
docker-compose -f docker-compose-dev.yml run base python manage.py recreatedb
```

Acesse o servidor local no endereço apresentado abaixo:


[localhost:5004](http://localhost:5004/)    

Agora você já pode começar a contribuir!

***   

## Testando

```
docker-compose -f docker-compose-dev.yml run base python manage.py test
```  

Execute o comando abaixo para checar a cobertura:   

```
docker-compose -f docker-compose-dev.yml run base python manage.py cov   
```