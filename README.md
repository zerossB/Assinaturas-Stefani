# Assinaturas-Stefani

Automatização da geração de assinaturas para a Cerâmica Stéfani S.A.

## Exemplo de Saida

![Exemplo de Assinatura](https://raw.githubusercontent.com/zerossB/Assinaturas-Stefani/master/sample-out.jpg)

## Dependências

- Python 3.6.4
- pip 9.0.1

Instalação de Dependências

`pip install depencencias.txt`

## Utilização
Criar um arquivo "Assinaturas.xlsx" dentro de uma pasta "xlsx", com a seguinte formatação:

![Exemplo Arquivo XLSX](https://raw.githubusercontent.com/zerossB/Assinaturas-Stefani/master/modelo-excel.png)

Após isso dar o comando abaixo:

`python3 main.py`

Irá gerar uma pasta chamada "jpg" dentro de app, lá estará todas as assinaturas

## TODO
- [ ] Argumentos Linha de comando
- [ ] Documentar
- [ ] Perder um tempo para arrumar as POG's