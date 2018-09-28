[![Build Status](https://travis-ci.org/Kalkuli/2018.2-Kalkuli_Reports.svg?branch=master
)](https://travis-ci.com/Kalkuli/2018.2-Kalkuli_Reports)


# Configurando o ambiente
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


## Testando

```
docker-compose -f docker-compose-dev.yml run base python manage.py test
```  

Execute o comando abaixo para checar a cobertura:   

```
docker-compose -f docker-compose-dev.yml run base python manage.py cov   
```