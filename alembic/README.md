# Instruções de uso do alembic

Sempre que fizer uma modificação na estrutura do banco de dados executar:

```
alembic revision --autogenerate -m "NomeDaVersão"
```

Para avançar o banco de dados para a nova versão executar:

```
alembic upgrade head
```

Para voltar o banco de dados para uma verão anterior executar:

```
alembic downgrade -1
```