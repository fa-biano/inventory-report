# 📃 Projeto Inventory Report!

Esse projeto implementa a leitura de arquivos com dados de produtos armazenados e gera um relatório de estoque. </br>
Os arquivos podem estar nas extensões .csv, .xml ou .json. Ao executar o comando de gerar o relatório no terminal o algoritmo irá identificar a extensão do arquivo automaticamente e realizará o relatório chamando a classe com as funções apropriadas para o arquivo.

Exemplo de relatório gerado: </br>
`Data de fabricação mais antiga: 2020-09-06` </br>
`Data de validade mais próxima: 2023-09-17` </br>
`Empresa com mais produtos: Target Corporation` </br>
`Produtos estocados por empresa:` </br>
`- Target Corporation: 4` </br>
`- Galena Biopharma: 2` </br>
`- Cantrell Drug Company: 2` </br>
`- Moore Medical LLC: 1` </br>
`- REMEDYREPACK: 1` </br>


O principal objetivo foi treinar habilidades como:

* Realizar a manipulação de arquivos.
* Utilizar o Paradigma de Orientação a Objetos e seus conceitos em Python.
* Refatorar classes utilizando Design Patterns como Strategy e Iterator.
* Escrever testes com Pytest.

O desenvolvimento desse projeto foi realizado durante o curso de Desenvolvimento Web na [Trybe](https://www.betrybe.com/)!

## 🔥 Tecnologias utilizadas:

  * Pyhton
  * Pytest

## ✨ Inicializando:

  Clone o repositório: `git clone git@github.com:fa-biano/inventory-report.git`

  Execute no terminal `python3 -m venv .venv && source .venv/bin/activate` para habilitar o ambiente virtual

  Instale as dependências  com `python3 -m pip install -r dev-requirements.txt`. </br> 
  *(Algumas depedências do pytest precisam de pré-instalação de alguns pacotes, por isso, caso apresente algum erro no terminal, basta executar o comando de instalação novamente.)*

  Instale a raiz do projeto como um modulo python executando `pip install .` na raiz

  Execute o comando `inventory_report <caminho do arquivo> <tipo de relatório>` para executar o relatório de estoque. Exemplo: `inventory_report inventory_report/data/inventory.csv completo`

  Obs: Existem 3 arquivos disponíveis para avaliação dentro da pasta inventory_report/data com as extensões .csv, .xml e .json. E 2 opções de relatórios (simples e completo).
