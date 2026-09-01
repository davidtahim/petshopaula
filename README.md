# PROJETO PET SHOP

## Estrutura de Projeto Python + MySQL + Tkinter
**Disciplina:** Linguagem de Programação II
**Projeto:** Sistema de Gestão de Pet Shop
**Tecnologias:** Python + Tkinter + MySQL
**Tema:** Estrutura de projeto, separação de responsabilidades, banco de dados e primeira interface gráfica
**Duração sugerida:** 4 horas

---

# 1. PROBLEMA DO PROJETO
O Pet Shop **Amigo Fiel** precisa de um sistema desktop para controlar produtos e estoque.

O sistema deverá evoluir para permitir:

- cadastro de produtos;
- consulta de produtos;
- alteração;
- exclusão;
- pesquisa;
- entrada de estoque;
- saída de estoque;
- controle de estoque baixo;
- relatórios.

---

## Objetivo geral
Desenvolver uma aplicação desktop em Python utilizando a biblioteca Tkinter para gerenciar os produtos de um pet shop, com organização por camadas e integração futura com banco de dados MySQL.

## Objetivos específicos
- Estruturar o projeto em pastas e módulos;
- Separar responsabilidades em modelos, repositories e services;
- Criar uma interface inicial com Tkinter;
- Entender a lógica de cadastro e consulta de produtos;
- Preparar a aplicação para trabalhar com dados persistentes em MySQL.

---

## Estrutura sugerida do projeto

```text
petshopaula/
├── app/
│   ├── main.py
│   ├── models/
│   │   └── produto.py
│   ├── repositories/
│   ├── services/
│   └── utils/
├── data/
├── tests/
├── run.py
├── README.md
└── .gitignore
```

---

## Camadas do projeto

### app/main.py
Arquivo principal da aplicação. É responsável por iniciar a interface e orquestrar os módulos.

### app/models/
Representa as entidades do sistema, como o modelo de produto.

### app/repositories/
Responsável pelas operações de acesso aos dados, como salvar, consultar e atualizar registros.

### app/services/
Contém a lógica de negócio do sistema, como validações e regras de operação.

### app/utils/
Armazena funções auxiliares e utilitários gerais.

### data/
Pasta para armazenar arquivos de dados, como banco ou CSVs, caso necessário.

### tests/
Local para testes automatizados e validações do sistema.

### run.py
Arquivo de execução para iniciar a aplicação.

---

## Requisitos do sistema

### Funcionalidades iniciais
- Cadastrar produto;
- Listar produtos;
- Buscar produto por código ou nome;
- Atualizar dados do produto;
- Excluir produto;
- Validar campos obrigatórios;
- Controlar quantidade em estoque.

### Requisitos técnicos
- Python 3.x;
- Tkinter para interface gráfica;
- MySQL para persistência futura;
- Organização por módulos e pacotes.

---

## Fluxo de desenvolvimento
1. Criar a estrutura de pastas do projeto;
2. Definir a entidade Produto;
3. Criar a interface inicial em Tkinter;
4. Implementar regras de negócio no service;
5. Preparar a camada de acesso a dados;
6. Conectar com banco MySQL;
7. Testar operações de cadastro, consulta e alteração.

---

## Exemplo de entidade Produto
A classe Produto pode conter atributos como:
- codigo
- nome
- categoria
- preco
- quantidade_estoque
- fornecedor

---

## Critérios de avaliação
- Organização da estrutura do projeto;
- Uso correto de módulos e pacotes;
- Separação entre model, repository e service;
- Funcionamento da interface gráfica;
- Clareza no código;
- Persistência e consistência de dados.

---

## Observação
Este projeto serve como base para a construção de um sistema real de gestão de pet shop, com evolução para banco de dados MySQL e melhorias na interface e nas funcionalidades.
